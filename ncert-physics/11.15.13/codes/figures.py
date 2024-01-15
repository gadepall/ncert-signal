import numpy as np
import matplotlib.pyplot as plt

# Define the time range from 0 to 3 seconds with small time intervals
t = np.linspace(0, 3, 1000)

# Define three different values for x
x_values = [1, 2, 3]

# Create a figure and axis with grid lines
fig, ax = plt.subplots()
ax.grid(True)

# Plot the graph for each x value
for x in x_values:
    y = 2 * np.cos(3 * x) * np.sin(10 * t)
    ax.plot(t, y, label=f'x={x}')

# Add labels and a legend
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Displacement (y)')
ax.set_title('Stationary Wave: y = 2*cos(3x)*sin(10t)')
ax.legend()

# Show the plot
plt.savefig('a.png')

# Define the wave velocity
v = 1.0  # You can adjust the velocity as needed

# Define the time range from 0 to 5 seconds with small time intervals
t = np.linspace(0, 5, 1000)

# Define three different values for x
x_values = [1, 3, 5]

# Create a figure and axis with grid lines
fig, ax = plt.subplots()
ax.grid(True)

# Plot the graph for each x value
for x in x_values:
    y = np.sqrt(x - v * t)
    ax.plot(t, y, label=f'x={x}')

# Add labels and a legend
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Displacement (y)')
ax.set_title('Wave: $y = \sqrt{x - vt}$')
ax.legend()

# Show the plot
plt.savefig('b.png')


# Define the time range from 0 to 10 seconds with small time intervals
t = np.linspace(0, 10, 1000)

# Define three different values for x
x_values = [1, 2, 3]

# Create a figure and axis with grid lines
fig, ax = plt.subplots()
ax.grid(True)

# Plot the graph for each x value
for x in x_values:
    y = 3 * np.sin(5 * x - 0.5 * t) + 4 * np.cos(5 * x - 0.5 * t)
    ax.plot(t, y, label=f'x={x}')

# Add labels and a legend
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Displacement (y)')
ax.set_title('Travelling Harmonic Wave: $y = 3\sin(5x - 0.5t) + 4\cos(5x - 0.5t)$')
ax.legend()

# Show the plot
plt.savefig('c.png')

# Define the time range from 0 to 2*pi seconds with small time intervals
t = np.linspace(0, 2 * np.pi, 1000)

# Define three different values for x
x_values = [np.pi/6, np.pi/4, np.pi/3]

# Create a figure and axis with grid lines
fig, ax = plt.subplots()
ax.grid(True)

# Plot the graph for each x value
for x in x_values:
    y = np.cos(x) * np.sin(t) + np.cos(2 * x) * np.sin(2 * t)
    ax.plot(t, y, label=f'x={x:.2f}')

# Add labels and a legend
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Displacement (y)')
ax.set_title('Superimposed Stationary Wave: $y = \cos(x)\sin(t) + \cos(2x)\sin(2t)$')
ax.legend()

# Show the plot
plt.savefig('d.png')

































