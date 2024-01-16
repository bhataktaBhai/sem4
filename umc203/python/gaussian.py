import matplotlib.pyplot as plt
from random import normalvariate

N = 100_000
x = [normalvariate(0, 1) for i in range(N)]
y = [normalvariate(0, 1) for i in range(N)]
plt.scatter(x, y, s=0.1)
plt.show()
