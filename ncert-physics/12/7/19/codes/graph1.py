import numpy as np
import matplotlib.pyplot as plt

# Function definition
def magnitude_H(f):
    return np.sqrt(225 + (2 * np.pi * f * 0.08 - 1 / (2 * np.pi * f * 0.00006))**2)

# Frequency range
f_values_positive = np.linspace(1, 50, 250)  # Positive frequencies
f_values_negative = -f_values_positive[::-1]  # Negative frequencies

# Calculate magnitude of H(2*pi*j*f) for each frequency
magnitude_values_positive = magnitude_H(f_values_positive)
magnitude_values_negative = magnitude_H(f_values_negative)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(f_values_positive, magnitude_values_positive, color='blue', label='Magnitude')
plt.plot(f_values_negative, magnitude_values_negative, color='blue')
plt.xlabel('Frequency (Hz)', color='blue')
plt.ylabel('|H(2πjf)|', color='blue')
plt.title('Magnitude of |H(2πjf)| vs Frequency')
plt.grid(True)

# Set x-axis limits
plt.xlim(-50, 50)

# Set y-axis limits
plt.ylim(-1000, 1000)

# Set x-axis and y-axis to have the same color
ax = plt.gca()
ax.spines['bottom'].set_color('blue')
ax.spines['left'].set_color('blue')

plt.legend()
plt.show()

