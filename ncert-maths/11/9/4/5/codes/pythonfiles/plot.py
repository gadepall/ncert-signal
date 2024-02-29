import matplotlib.pyplot as plt

with open('theoretical.txt', 'r') as file:
    gp_values = [float(line.strip()) for line in file if line.strip()]

with open('convolution.txt', 'r') as file:
    gp_sum_values = [float(line.strip()) for line in file if line.strip()]

plt.stem(range(len(gp_values)), gp_values, markerfmt='r^', linefmt='-', basefmt='b', label='On convolution')
plt.scatter(range(len(gp_sum_values)), gp_sum_values, color='black', marker='o',label='Theoretical')

# Highlight the 22nd term
highlight_index = 16
plt.scatter(highlight_index, gp_sum_values[highlight_index], color='red', marker='x', s=100, label='y(15)')

plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid(True)
plt.legend()
plt.savefig('plot.png')
plt.show()
