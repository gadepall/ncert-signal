import numpy as np
import matplotlib.pyplot as plt

# Define the function for current I
def current(omega):
    return 1e-4 * 110 * omega * np.sqrt(2) / np.sqrt(1 + (40 * omega * 1e-4)**2)

# Generate values for omega
omega_values = np.linspace(0, 5000, 1000)  # Adjust the range as per your requirement

# Calculate corresponding values of I
current_values = current(omega_values)

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(omega_values, current_values, label='I vs omega')
plt.xlabel('$\omega$')
plt.ylabel('Current (I)')
plt.title('Graph of I vs $\omega$')
plt.grid(True)
plt.legend()
plt.show()
