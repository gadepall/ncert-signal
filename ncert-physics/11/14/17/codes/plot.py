import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 10000)

x = np.loadtxt("111417cout.txt")

plt.plot(t, x)

plt.xlabel("Time ($t$)")
plt.ylabel("Displacement ($\\theta$)")

plt.savefig("plot.png")
