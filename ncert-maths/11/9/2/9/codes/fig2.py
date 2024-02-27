import matplotlib.pyplot as plt
a = 7.5  # First term
d = 9 # Common difference
n = 25
ap_series = [a + i * d for i in range(n)]
plt.stem(range(0, n ), ap_series, linefmt='-', markerfmt='o', basefmt=' ')
plt.xlabel('n')
plt.ylabel('$x_1(n)$')
plt.grid(True)
plt.savefig('figs/fig2.png')
plt.show()

