import matplotlib.pyplot as plt

def plot_GP_from_file(filename):
  """
  Plots the data from a file as a stem plot.

  Args:
      filename: The name of the file containing the data.
  """
  n_values = []
  term_values = []

  # Read data from file
  with open(filename, 'r') as file:
    # Skip the header
    file.readline()
    # Read data line by line
    for line in file:
      n, term = map(int, line.strip().split('\t'))
      n_values.append(n)
      term_values.append(term)

  # Plot the graph as a stem plot
  plt.stem(n_values, term_values, linefmt='b-', markerfmt='bo', basefmt='r-')
  for i in range(len(n_values)):
    plt.text(n_values[i], term_values[i], f'({n_values[i]}, {term_values[i]})', verticalalignment='bottom', horizontalalignment='right', fontsize=8, color='black')
  plt.xlabel('Term Number n')
  plt.ylabel('Term Value x(n)')
  plt.grid(True)
  plt.show()

if __name__ == "__main__":
  filename1 = "gp_data1.txt"  # Specify the first filename
  filename2 = "gp_data2.txt"  # Specify the second filename
  plot_GP_from_file(filename1)  # Call for first plot
  plot_GP_from_file(filename2)  # Call for second plot

