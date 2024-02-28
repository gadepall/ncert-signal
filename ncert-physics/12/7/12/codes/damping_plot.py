import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt('data_for_damping.txt', skiprows=1)

time = data[:, 0]
current = data[:, 1]
power = data[:, 2]

# Plotting Current
plt.plot(time, current, label='Current', color='tab:orange')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.title('Current as a function of time')
plt.grid(True)
plt.legend()
plt.savefig("Current_in_circuit_during_damping.png")
plt.clf()

# Plotting Power
plt.plot(time, power, label='Power', color='tab:red')
plt.xlabel('Time (s)')
plt.ylabel('Power (W)')
plt.title('Power as a function of time')
plt.grid(True)
plt.legend()
plt.text(0.5, 0.9, 'Area = 1 Joule', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
plt.savefig("Power_Dissipated_across_Resistor.png")
plt.clf()
