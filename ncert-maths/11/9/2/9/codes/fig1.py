import matplotlib.pyplot as plt
a = 4.5  # First term
d = 5  # Common difference
n = 25
ap_series = [a + i * d for i in range(n)]
plt.stem(range(0, n ), ap_series, linefmt='-', markerfmt='o', basefmt=' ')
plt.xlabel('n')
plt.ylabel('$x_2(n)$')
plt.grid(True)
plt.savefig('figs/fig1.png')
plt.show()

