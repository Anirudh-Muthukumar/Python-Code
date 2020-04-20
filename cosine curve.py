import math
import matplotlib.pyplot as plt

x = 140
y = 3

for degree in range(0, 45):
    print(degree, x*math.cos(math.radians(degree)), y*math.sin(math.radians(180-90-degree)))

# plt.figure()
# plt.plot([i for i in range(0, 181)], cos)
# plt.show()