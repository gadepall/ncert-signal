import numpy
import matplotlib.pyplot as plt

# X-axis
n = numpy.arange(0, 31, 1)

# Y-axis
x = 5000 + 200 * n

# Plot graph
plt.stem(n, x)

# Mark (0,5000) and (10, 7000) in red
plt.stem([0, 10], [5000, 7000], linefmt="C3")

# Label axes
plt.xlabel("n")
plt.ylabel("x(n)")

# Label (0, 5000) and (10, 7000)
plt.annotate("5000", (0, 5000), ha="center", va="bottom", xytext=(0, 10), textcoords="offset points")
plt.annotate("7000", (10, 7000), ha="center", va="bottom", xytext=(0, 10), textcoords="offset points")

# Save x(n) vs n graph
plt.savefig("../figs/10_5_2_19.png")
