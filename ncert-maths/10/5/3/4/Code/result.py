import matplotlib.pyplot as plt

# Function to compute x(n) for the series
def x_n(n):
    return 9 + (n - 1) * 8  # nth term of the series

# Number of terms in the series
num_terms = 20

# Generate values for n and x(n)
n_values = list(range(1, num_terms + 1))
x_values = [x_n(n) for n in n_values]

# Plot the stem graph
plt.stem(n_values, x_values, linefmt='b-', markerfmt='bo', basefmt=' ')

# Mark the first 12 terms in a different color
plt.stem(n_values[:12], x_values[:12], linefmt='r-', markerfmt='ro', basefmt=' ')

# Add text annotation for the sum near the 12th term
plt.text(12, 636, 'Sum = 636', fontsize=10, ha='center', va='bottom', color='green')

# Add labels and title
plt.xlabel('n')
plt.ylabel('x(n)')

# Show the plot
plt.grid(True)
plt.show()

