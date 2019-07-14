import itertools

def A001045():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, b+2*a

sequence = A001045()
n = 234612846789231 - 1
print(next(itertools.islice(sequence, n - 1, n - 1 + 1)))
# print([next(sequence) for i in range(20)])