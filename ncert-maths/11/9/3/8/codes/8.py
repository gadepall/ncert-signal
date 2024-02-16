import matplotlib.pyplot as plt
with open('gp_values.tex', 'r') as file:
    gp_values = [float(line.strip()) for line in file]
    
with open('gp_sum_values.tex', 'r') as file:
    gp_sum_values = [float(line.strip()) for line in file]
    
    
plt.stem(range(len(gp_values)), gp_values, markerfmt='r^', linefmt='-', basefmt='b', label='Stem plot')
plt.scatter(range(len(gp_sum_values)), gp_sum_values, color='black', marker='o',label='y(n) using formulae')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid(True)
plt.legend()

plt.show()
