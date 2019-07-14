#!/usr/bin/env python

import pygame
import sys
from random import choice
from random import shuffle
import pprint
import itertools
pp = pprint.PrettyPrinter(depth=3, indent=2)

pygame.init()
black = 0, 0, 0
red = 255, 0, 0

asurf = pygame.image.load('shuffled_images/2.pgm')
slices = []
idx = 0
for row in range(64):
  for col in range(16):
    subsurf = asurf.subsurface(pygame.Rect(col * 4, row, 4, 1))
    slices.append({"surf": subsurf, "id": idx})
    idx += 1

def regen(screen):
  rebuilt_surf1 = pygame.Surface((64, 64))

  for aslice in slices:
    best_distance = None
    best_switch = None
    for row in range(64):
      for col in range(16):
        curr_slice = slices[row * 16 + col]
        right_slice = None
        left_slice = None
        top_slice = None
        bottom_slice = None

        # if col > 0:
        #   left_slice = slices[row * 16 + col - 1]
        # if col < 15:
        #   right_slice = slices[row * 16 + col - 1]
        if row > 0:
          top_slice = slices[(row - 1) * 16 + col]
        if row < 63:
          # print(row)
          bottom_slice = slices[(row + 1) * 16 + col]

        distances = []
        if right_slice:
          p1 = right_slice['surf'].get_at([3, 0])
          p2 = aslice['surf'].get_at([0, 0])
          distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        if left_slice:
          p1 = left_slice['surf'].get_at([0, 0])
          p2 = aslice['surf'].get_at([3, 0])
          distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        if top_slice:
          for n in range(4):
            p1 = top_slice['surf'].get_at([n, 0])
            p2 = aslice['surf'].get_at([n, 0])
            distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        if bottom_slice:
          for n in range(4):
            p1 = bottom_slice['surf'].get_at([n, 0])
            p2 = aslice['surf'].get_at([n, 0])
            distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        mean = sum(distances) / len(distances)
        # score = sum(distances)
        score = mean
        if best_distance == None or score < best_distance:
          best_distance = score
          best_switch = curr_slice
    
    if best_switch != aslice:
      switch_index = slices.index(best_switch)
      curr_index = slices.index(aslice)
      slices[switch_index] = aslice
      slices[curr_index] = best_switch

    x = 0
    y = 0
    for aslice in slices:
      rebuilt_surf1.blit(aslice['surf'], [x, y])
      x += 4
      if x >= 64:
        x = 0
        y += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          print([x['id'] for x in slices])

    screen.fill(black)
    screen.blit(pygame.transform.scale(asurf, (256, 256)), [0, 0])
    screen.blit(pygame.transform.scale(rebuilt_surf1, (256, 256)), [0, 256])
    pygame.display.flip()

  for aslice in slices:
    best_distance = None
    best_switch = None
    for row in range(64):
      for col in range(16):
        curr_slice = slices[row * 16 + col]
        right_slice = None
        left_slice = None
        top_slice = None
        bottom_slice = None

        if col > 0:
          left_slice = slices[row * 16 + col - 1]
        if col < 15:
          right_slice = slices[row * 16 + col - 1]
        if row > 0:
          top_slice = slices[(row - 1) * 16 + col]
        if row < 63:
          # print(row)
          bottom_slice = slices[(row + 1) * 16 + col]

        distances = []
        if right_slice:
          p1 = right_slice['surf'].get_at([3, 0])
          p2 = aslice['surf'].get_at([0, 0])
          distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        if left_slice:
          p1 = left_slice['surf'].get_at([0, 0])
          p2 = aslice['surf'].get_at([3, 0])
          distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        if top_slice:
          for n in range(4):
            p1 = top_slice['surf'].get_at([n, 0])
            p2 = aslice['surf'].get_at([n, 0])
            distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        if bottom_slice:
          for n in range(4):
            p1 = bottom_slice['surf'].get_at([n, 0])
            p2 = aslice['surf'].get_at([n, 0])
            distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        mean = sum(distances) / len(distances)
        # score = sum(distances)
        score = mean
        if best_distance == None or score < best_distance:
          best_distance = score
          best_switch = curr_slice
    
    if best_switch != aslice:
      switch_index = slices.index(best_switch)
      curr_index = slices.index(aslice)
      slices[switch_index] = aslice
      slices[curr_index] = best_switch

    x = 0
    y = 0
    for aslice in slices:
      rebuilt_surf1.blit(aslice['surf'], [x, y])
      x += 4
      if x >= 64:
        x = 0
        y += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          print([x['id'] for x in slices])

    screen.fill(black)
    screen.blit(pygame.transform.scale(asurf, (256, 256)), [0, 0])
    screen.blit(pygame.transform.scale(rebuilt_surf1, (256, 256)), [0, 256])
    pygame.display.flip()

def regen3(screen):
  # asurf_rect = asurf.get_rect()

  rebuilt_surf1 = pygame.Surface((64, 64))
  # rebuilt_surf2 = pygame.Surface((64, 64))

  # y = 0
  # x = 0
  # curr_slice = slices.pop(0)
  # rebuilt_surf1.blit(curr_slice, [x, y])
  # y += 1

  # while len(slices) > 0 and y < 64:
  #   best_match = None
  #   best_score = None
  #   for aslice in slices:
  #     score = 0
  #     distances = []
  #     for col in range(4):
  #       p1 = curr_slice.get_at([col, 0])
  #       p2 = aslice.get_at([col, 0])
  #       distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))
  #       # distances.append()
  #     mean = sum(distances) / len(distances)
  #     score = mean
  #     # print(score)
  #     if best_score == None or score < best_score:
  #       best_match = aslice
  #       best_score = score
  #   curr_slice = best_match
  #   slices.remove(curr_slice)
  #   rebuilt_surf1.blit(curr_slice, [x, y])
  #   y += 1

  # for row in range(64):
  #   for col in range(16):
  #     print(row * 64 + col)
  #     curr_slice = slices[row * 16 + col]
  #     right_slice = None
  #     left_slice = None

  # for aslice in slices:
  thisslice = slices[0]
  while True:
    best_distance = None
    best_switch = None
    for row in range(64):
      for col in range(16):
        curr_slice = slices[row * 16 + col]
        right_slice = None
        left_slice = None
        top_slice = None
        bottom_slice = None

        if col > 0:
          left_slice = slices[row * 16 + col - 1]
        if col < 15:
          right_slice = slices[row * 16 + col - 1]
        if row > 0:
          top_slice = slices[(row - 1) * 16 + col]
        if row < 63:
          # print(row)
          bottom_slice = slices[(row + 1) * 16 + col]

        distances = []
        if right_slice:
          p1 = right_slice['surf'].get_at([3, 0])
          p2 = thisslice['surf'].get_at([0, 0])
          distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        if left_slice:
          p1 = left_slice['surf'].get_at([0, 0])
          p2 = thisslice['surf'].get_at([3, 0])
          distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        if top_slice:
          for n in range(4):
            p1 = top_slice['surf'].get_at([n, 0])
            p2 = thisslice['surf'].get_at([n, 0])
            distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        if bottom_slice:
          for n in range(4):
            p1 = bottom_slice['surf'].get_at([n, 0])
            p2 = thisslice['surf'].get_at([n, 0])
            distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        mean = sum(distances) / len(distances)
        # score = sum(distances)
        score = mean
        if best_distance == None or score < best_distance:
          best_distance = score
          best_switch = curr_slice
    
    if best_switch != thisslice:
      switch_index = slices.index(best_switch)
      curr_index = slices.index(thisslice)
      slices[switch_index] = thisslice
      slices[curr_index] = best_switch
      thisslice = best_switch
    else:
      curr_index = slices.index(thisslice)
      if curr_index + 1 < len(slices):
        thisslice = slices[curr_index + 1]
      else:
        thisslice = choice(slices)      

    x = 0
    y = 0
    for aslice in slices:
      rebuilt_surf1.blit(aslice['surf'], [x, y])
      x += 4
      if x >= 64:
        x = 0
        y += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          print([x['id'] for x in slices])

    screen.fill(black)
    screen.blit(pygame.transform.scale(asurf, (256, 256)), [0, 0])
    screen.blit(pygame.transform.scale(rebuilt_surf1, (256, 256)), [0, 256])
    pygame.display.flip()

def regen2(screen):
  # asurf_rect = asurf.get_rect()

  rebuilt_surf1 = pygame.Surface((64, 64))
  # rebuilt_surf2 = pygame.Surface((64, 64))

  # y = 0
  # x = 0
  # curr_slice = slices.pop(0)
  # rebuilt_surf1.blit(curr_slice, [x, y])
  # y += 1

  # while len(slices) > 0 and y < 64:
  #   best_match = None
  #   best_score = None
  #   for aslice in slices:
  #     score = 0
  #     distances = []
  #     for col in range(4):
  #       p1 = curr_slice.get_at([col, 0])
  #       p2 = aslice.get_at([col, 0])
  #       distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))
  #       # distances.append()
  #     mean = sum(distances) / len(distances)
  #     score = mean
  #     # print(score)
  #     if best_score == None or score < best_score:
  #       best_match = aslice
  #       best_score = score
  #   curr_slice = best_match
  #   slices.remove(curr_slice)
  #   rebuilt_surf1.blit(curr_slice, [x, y])
  #   y += 1

  # for row in range(64):
  #   for col in range(16):
  #     print(row * 64 + col)
  #     curr_slice = slices[row * 16 + col]
  #     right_slice = None
  #     left_slice = None

  for aslice in slices:
    best_distance = None
    best_switch = None
    for row in range(64):
      for col in range(16):
        curr_slice = slices[row * 16 + col]
        right_slice = None
        left_slice = None
        top_slice = None
        bottom_slice = None

        if col > 0:
          left_slice = slices[row * 16 + col - 1]
        if col < 15:
          right_slice = slices[row * 16 + col - 1]
        if row > 0:
          top_slice = slices[(row - 1) * 16 + col]
        if row < 63:
          # print(row)
          bottom_slice = slices[(row + 1) * 16 + col]

        distances = []
        if right_slice:
          p1 = right_slice['surf'].get_at([3, 0])
          p2 = aslice['surf'].get_at([0, 0])
          distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        if left_slice:
          p1 = left_slice['surf'].get_at([0, 0])
          p2 = aslice['surf'].get_at([3, 0])
          distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        if top_slice:
          for n in range(4):
            p1 = top_slice['surf'].get_at([n, 0])
            p2 = aslice['surf'].get_at([n, 0])
            distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        if bottom_slice:
          for n in range(4):
            p1 = bottom_slice['surf'].get_at([n, 0])
            p2 = aslice['surf'].get_at([n, 0])
            distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))

        mean = sum(distances) / len(distances)
        # score = sum(distances)
        score = mean
        if best_distance == None or score < best_distance:
          best_distance = score
          best_switch = curr_slice
    
    if best_switch != aslice:
      switch_index = slices.index(best_switch)
      curr_index = slices.index(aslice)
      slices[switch_index] = aslice
      slices[curr_index] = best_switch

    x = 0
    y = 0
    for aslice in slices:
      rebuilt_surf1.blit(aslice['surf'], [x, y])
      x += 4
      if x >= 64:
        x = 0
        y += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          print([x['id'] for x in slices])

    screen.fill(black)
    screen.blit(pygame.transform.scale(asurf, (256, 256)), [0, 0])
    screen.blit(pygame.transform.scale(rebuilt_surf1, (256, 256)), [0, 256])
    pygame.display.flip()


def regen1(screen):
  asurf = pygame.image.load('shuffled_images/800.pgm')
  asurf_rect = asurf.get_rect()

  rebuilt_surf1 = pygame.Surface((64, 64))
  rebuilt_surf2 = pygame.Surface((64, 64))

  slices = []
  print(asurf_rect)
  for row in range(64):
    for col in range(16):
      subsurf = asurf.subsurface(pygame.Rect(col * 4, row, 4, 1))
      slices.append(subsurf)

  # shuffle(slices)
  y = 0
  x = 0
  curr_slice = slices.pop(0)
  rebuilt_surf1.blit(curr_slice, [x, y])
  while len(slices) > 0:
    y += 1
    if y >= 64:
      y = 0
      x += 4
    best_match = None
    best_score = None
    for aslice in slices:
      score = 0
      distances = []
      for col in range(4):
        p1 = curr_slice.get_at([col, 0])
        p2 = aslice.get_at([col, 0])
        distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))
        # distances.append()
      mean = sum(distances) / len(distances)
      score = mean
      # print(score)
      if best_score == None or score < best_score:
        best_match = aslice
        best_score = score
    curr_slice = best_match
    slices.remove(curr_slice)
    rebuilt_surf1.blit(curr_slice, [x, y])

  slices = []
  for col in range(16):
    subsurf = rebuilt_surf1.subsurface(pygame.Rect(col * 4, 0, 4, 64))
    slices.append(subsurf)

  y = 0
  x = 0
  curr_slice = slices.pop(0)
  rebuilt_surf2.blit(curr_slice, (x, y))
  while len(slices) > 0:
    x += 4
    best_match = None
    best_score = None
    for aslice in slices:
      score = 0
      distances = []
      for row in range(64):
        p1 = curr_slice.get_at([3, row])
        p2 = aslice.get_at([0, row])
        distances.append(sum((a-b)**2 for a, b in zip(p1, p2))**(.5))
      mean = sum(distances) / len(distances)
      score = mean
      # print(score)
      if best_score == None or score < best_score:
        best_match = aslice
        best_score = score
    curr_slice = best_match
    slices.remove(curr_slice)
    rebuilt_surf2.blit(curr_slice, [x, y])

  screen.fill(black)
  screen.blit(pygame.transform.scale(asurf, (256, 256)), [0, 0])
  screen.blit(pygame.transform.scale(rebuilt_surf1, (256, 256)), [0, 256])
  screen.blit(pygame.transform.scale(rebuilt_surf2, (256, 256)), [256, 256])
  pygame.display.flip()

# for oslice in slices:
#   for tslice in slices:
#     if oslice == tslice:
#       continue
    
#     score = 0
#     distances = []
#     for col in range(4):
#       # print(col)
#       distances.append(oslice['surf'].get_at([col, 0]) == tslice['surf'].get_at([col, 0]))
#       # if oslice['surf'].get_at([col, 0]) == tslice['surf'].get_at([col, 0]):
#         # score += 1
#     mean = sum(distances) / len(distances)
#     score = mean
#     oslice['vdistances'] = { 'surf': tslice, 'score': score }


screen = pygame.display.set_mode([512, 512])
# font = pygame.font.Font(None, 12)
# lock = font.render("LOCK", True, red)

# ordered_slices = []



iternum = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        # elif event.type == pygame.KEYDOWN:
          # regen(screen)
    iternum += 1
    print('Gen', iternum)
    regen(screen)


          # distances.append()
      # for aslice in first_slice[vdistances]:
      # best_match = max(curr_slice['vdistances'], key=lambda x: x['score'])


      


    # for perm in itertools.permutations(slices):
    #   for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #       sys.exit()

    #   x = 0
    #   y = 64
    #   for aslice in perm:
    #     screen.blit(aslice['surf'], [x, y])
    #     x += 4
    #     if x >= 64:
    #       x = 0
    #       y += 1

    #   pygame.display.flip()
    
    # slices.insert(0, slices.pop())
    # pygame.display.flip()
