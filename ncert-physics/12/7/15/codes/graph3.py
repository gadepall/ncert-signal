import numpy as np
import matplotlib.pyplot as plt

# Define the formula for I_0
def calculate_I_0(V_0):
    return V_0 / np.sqrt(1600 + (10**6 / (144 * np.pi**2)))

# Generate a range of values for V_0
V_0_values = np.linspace(0, 100, 100)  # Adjust the range as needed

# Calculate corresponding I_0 values
I_0_values = calculate_I_0(V_0_values)

# Plot the graph
plt.plot(V_0_values, I_0_values, label=r'$I_0 = \frac{V_0}{\sqrt{1600 + \frac{10^6}{144 \pi^2}}}$')
plt.xlabel(r'$V_0$')
plt.ylabel(r'$I_0$')
plt.title('$I_0$ vs $V_0$')
plt.legend()
plt.grid(True)
plt.show()
