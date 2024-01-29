import matplotlib.pyplot as plt
import numpy as np

# X-axis
n = np.linspace(0, 7, 8)

# Y-axis
x = np.loadtxt("11_9_3_30cout.txt")

# Plot graph
plt.stem(n, x)

# Plot (2, 120) and (4, 480) in a separate color and mark them.
plt.stem(2, 120, linefmt="C2", label="$x(2)$")
plt.stem(4, 480, linefmt="C3", label="$x(4)$")
plt.annotate("120", (2, 120), ha="center", va="bottom", xytext=(0, 10), textcoords="offset points")
plt.annotate("480", (4, 480), ha="center", va="bottom", xytext=(0, 10), textcoords="offset points")

# Label axes
plt.xlabel("n")
plt.ylabel("x(n)")

plt.legend()

plt.savefig("../figs/11_9_3_30.png")
