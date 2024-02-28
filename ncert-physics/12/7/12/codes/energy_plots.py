import numpy as np
import matplotlib.pyplot as plt

# Load data from the text file
data = np.loadtxt('data.txt', skiprows=1)

# Extract columns from the data
time = data[0:200, 0]
capacitor_energy = data[0:200, 4]
inductor_energy = data[0:200, 5]

# Plotting without smoothing
fig, ax = plt.subplots(figsize=(8, 6)) 

ax.plot(time, capacitor_energy, label='Capacitor Energy', linestyle='-', color='blue', linewidth=2)
ax.plot(time, inductor_energy, label='Inductor Energy', linestyle='-', color='red', linewidth=2)
# Draw horizontal line at y=1
ax.axhline(y=1, color='green', linestyle='--', label='Energy Conservation')
# Set labels and title
ax.set_xlabel('Time (s)')
ax.set_ylabel('Energy (Joules)')

# Set legend at the corner
ax.legend(loc='upper left')

# Show the plot
plt.grid(True)
plt.title('Energy Across Capacitor and Inductor in LC Circuit')
plt.savefig("Plot_energy.png")
plt.clf()


fig, ax = plt.subplots(figsize=(8, 6)) 
ax.plot(time, capacitor_energy, label='Capacitor Energy', linestyle='-', color='blue', linewidth=2)
ax.plot(time, inductor_energy, label='Inductor Energy', linestyle='-', color='red', linewidth=2)

# Draw horizontal line at y=0.5 when both capacitor and indcutor have same energy
ax.axhline(y=0.5, color='brown', linestyle='--', label='Equal energy 0.5 J each')

# Set labels and title
ax.set_xlabel('Time (s)')
ax.set_ylabel('Energy (Joules)')

# Set legend at the corner
ax.legend(loc='upper left')

# Show the plot
plt.grid(True)
plt.title('Energy Across Capacitor and Inductor in LC Circuit')
plt.savefig("Plot_equal_enrgy.png")