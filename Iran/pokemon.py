#!/usr/bin/env python

import pygame
import sys
from random import choice
import pprint
pp = pprint.PrettyPrinter(depth=3, indent=2)

pygame.init()
asurf = pygame.image.load('test.jpg')
asurf_rect = asurf.get_rect()
black = 0, 0, 0
red = 255, 0, 0

screen = pygame.display.set_mode([1200, 600])

cells = []

for y in range(0, 24):
    for x in range(0, 24):
        subsurf = asurf.subsurface(pygame.Rect(x * 400, y * 400, 400, 400))
        avg = pygame.transform.average_color(subsurf)
        if avg != (255, 255, 255, 0):
            avgsurf = pygame.Surface((400, 400))
            avgsurf.fill(avg)
            cells.append({'id': [x, y], 'surf': subsurf, 'avg': avg, 'avgsurf': avgsurf })

dictionary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

dictmap = {}

for avg in set(list([x['avg'] for x in cells])):
    if not avg in dictmap:
        dictmap[avg] = dictionary.pop(0)
    print(avg)

print(len(set(list([x['avg'] for x in cells]))))

print(''.join([dictmap[cell['avg']] for cell in cells]))

# def chunks(l, n):
#     """Yield successive n-sized chunks from l."""
#     for i in range(0, len(l), n):
#         yield l[i:i + n]

# pairs = list(chunks([dictmap[cell['avg']] for cell in cells], 2))
# print(pairs)

# dictionary = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# dictmap = {}

font = pygame.font.Font(None, 12)
lock = font.render("LOCK", True, red)

rebuilt_surf = pygame.Surface([9600, 9600])
colored_surf = pygame.Surface([9600, 9600])

x = 0
y = 0
for cell in cells:
    rebuilt_surf.blit(cell['surf'], [x, y])
    colored_surf.blit(cell['avgsurf'], [x, y])
    x += 400
    if x >= 9600:
        x = 0
        y += 400

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    screen.blit(pygame.transform.scale(rebuilt_surf, (600, 600)), [0, 0])
    screen.blit(pygame.transform.scale(colored_surf, (600, 600)), [600, 0])
    pygame.display.flip()
