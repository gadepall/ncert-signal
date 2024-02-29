import matplotlib.pyplot as plt

# Read data from the file
with open("values.txt", "r") as file:
    data = file.readlines()

# Convert data to float
data = [float(value.strip()) for value in data]

# Generate time values (assuming each value corresponds to a time step of 0.01 seconds)
time = [i * 0.01 for i in range(len(data))]

# Plot the graph
plt.plot(time, data)
plt.xlabel('Time (s)')
plt.ylabel('Current(I)')
plt.grid(True) 
plt.legend()
plt.savefig('polt1.png')
plt.show()

