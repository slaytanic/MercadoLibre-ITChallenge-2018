import math

N = 2
probUnique = 1.0

for k in range(1, 3):
    probUnique = probUnique * (N - (k - 1)) / N
    print(k, 1 - probUnique, 1 - math.exp(-0.5 * k * (k - 1) / N))
