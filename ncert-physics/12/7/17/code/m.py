import numpy as np
import matplotlib.pyplot as plt

# Define the components values
R = 40  # Resistance in ohms
L = 5  # Inductance in henrys
C = 0.00008  # Capacitance in farads

# Define the range of angular frequencies
omega = np.linspace(0.1, 100, 1000)  # Adjust the range as needed

# Calculate impedance
Z_total = 1 / (1/R + 1/(1j*omega*L) + 1/(1/(1j*omega*C)))

# Find resonance frequency and maximum impedance
resonance_freq = omega[np.argmax(np.abs(Z_total))]
max_impedance = np.max(np.abs(Z_total))

# Plotting
plt.axvline(x=resonance_freq, color='r', linestyle='--', label=f'Resonance Frequency = {resonance_freq:.2f} rad/s')
plt.axhline(y=max_impedance, color='g', linestyle='--', label=f'Maximum Impedance = {max_impedance:.2f} ohms')

plt.plot(omega, np.abs(Z_total))
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('|H(jω)|')
plt.title('|H(jω)| of Parallel RLC Circuit vs Angular Frequency')
plt.grid(True)

# Annotate the maximum point
plt.annotate(f'Max: ({resonance_freq:.2f}, {max_impedance:.2f})',
             xy=(resonance_freq, max_impedance),
             xytext=(resonance_freq + 10, max_impedance + 0.1),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.legend()
plt.savefig('m.png')
plt.show()
