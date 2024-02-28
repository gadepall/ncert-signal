import numpy as np
import matplotlib.pyplot as plt

# Given values for LC circuit
L = 50e-6  # Inductance in Henry (50 uH)
C = 50e-6  # Capacitance in Farad (50 uF)

# Generate frequency values up to 4000 Hz
frequencies = np.linspace(1, 4000, 990)  # Adjust the number of points as needed

# Convert frequencies to angular frequencies (rad/s)
angular_frequencies = 2 * np.pi * frequencies

# Calculate impedance for the LC circuit
impedance = np.abs(2 * np.pi * frequencies * L - 1 / (2 * np.pi * frequencies * C))

# Find the natural frequency
natural_frequency = 1 / np.sqrt(L * C)

# Find the angular frequency at which minimum impedance occurs
min_impedance_angular_frequency = angular_frequencies[np.argmin(impedance)]

plt.clf()
# Plotting |Z| vs ω with log scale for y-axis
plt.figure(figsize=(8, 6))
plt.plot(angular_frequencies, impedance, label='|Z| vs ω', linestyle='-', color='blue', linewidth=2)

# Mark the resonant angular frequency on the plot
resonant_frequency_index = np.argmin(impedance)
plt.scatter(min_impedance_angular_frequency, impedance[resonant_frequency_index], color='red', s=100, label='Resonant Frequency')

# Annotate the value at the marked resonant angular frequency
plt.text(min_impedance_angular_frequency, impedance[resonant_frequency_index], f'(w_0={min_impedance_angular_frequency:.2f} rad/s)',
         color='black', fontsize=10, ha='right', va='bottom')

plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('|Z| (Impedance Magnitude) - Log Scale')
plt.title('Impedance Magnitude vs Angular Frequency for LC Circuit ')
plt.legend(loc='upper right')
plt.grid(True)
plt.yscale('log')  # Set log scale for the y-axis

plt.savefig("impedance_plot.png")
