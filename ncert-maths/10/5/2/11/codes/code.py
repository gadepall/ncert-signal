import matplotlib.pyplot as plt

filename = 'ap_data.txt'

# Read data from the file
with open(filename, 'r') as file:
    ap_sequence = [int(line.strip()) for line in file]

# Plot the AP using a stem plot
plt.stem(range(1, len(ap_sequence) + 1), ap_sequence, basefmt='b-', linefmt='b-', markerfmt='bo')
plt.title('Arithmetic Progression')
plt.xlabel('Term Number')
plt.ylabel('Value')
plt.grid(True)
plt.savefig('fig1.png')

