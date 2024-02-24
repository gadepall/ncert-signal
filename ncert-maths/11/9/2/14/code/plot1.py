import numpy as np
import matplotlib.pyplot as plt

# Define AP parameters
first_term = 8
last_term = 26
num_terms = 7

# Generate the terms of the AP using linspace
ap_terms = np.linspace(first_term, last_term, num_terms)

# Plotting the AP serie
plt.stem(range(num_terms), ap_terms, markerfmt='bo', linefmt='b-', basefmt='b-', label='AP Series')
plt.stem(0, first_term, markerfmt='ro',linefmt='b-',basefmt='b-', label='First Term = 8')
plt.stem(num_terms-1, last_term, markerfmt='go',linefmt='b-',basefmt='b-', label='Last Term = 26')

plt.xlabel('n')
plt.ylabel('x(n)')
plt.legend()
plt.grid(True)
plt.savefig('plot1.png')


