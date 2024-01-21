import numpy as np
import matplotlib.pyplot as plt

# Function for intensity
def intensity(r):
    return np.cos(np.pi * r) ** 2

# Range of r values
r_values = np.linspace(0, 2, 1000)

# Calculate intensity for each r
intensity_values = intensity(r_values)

# Plot the intensity
plt.plot(r_values, intensity_values, label=r'$\cos^2(\pi r)$')
plt.xlabel('r', fontsize=14)
plt.ylabel('Intensity', fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title('Plot of Intensity vs r',fontsize = 14)
plt.legend()
plt.grid(True)

# Mark intensity values for r = 1 and r = 1/3
r_1 = 1
r_1_3 = 1/3
intensity_1 = intensity(r_1)
intensity_1_3 = intensity(r_1_3)

plt.scatter([r_1, r_1_3], [intensity_1, intensity_1_3], color='red')
plt.annotate(f'r = {r_1}', xy=(r_1, intensity_1), xytext=(r_1 + 0.25, intensity_1 - 0.1),
             arrowprops=dict(facecolor='black', arrowstyle='->'),fontsize=12)
plt.annotate('r = $\\frac{1}{3}$', xy=(r_1_3, intensity_1_3), xytext=(r_1_3 - 0.35, intensity_1_3 - 0.1),
             arrowprops=dict(facecolor='black', arrowstyle='->'),fontsize=14)

# Save the plot
plt.savefig('intensity_plot.png', dpi=600)

# Show the plot
plt.show()
