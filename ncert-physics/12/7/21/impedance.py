import matplotlib.pyplot as plt
import numpy as np


# Function |H(jω)|
def magnitude_H(omega, R, L, C):
    return np.sqrt(R**2 + (omega * L - 1/(omega * C))**2)

R_value = 7.4
L_value = 3
C_value = 0.000027


omega_values = np.linspace(100, 200, 10000)

magnitude_values = magnitude_H(omega_values, R_value, L_value, C_value)

min_index = np.argmin(magnitude_values)
min_omega = omega_values[min_index]
H_jomega0 = magnitude_values[min_index]


plt.plot(omega_values, magnitude_values, label='|H(jω)|')

plt.scatter(min_omega, H_jomega0, color='red')
plt.annotate(f'$H(j\\omega_0)={H_jomega0:.2f}$', xy=(min_omega, H_jomega0), xytext=(min_omega-0.5, H_jomega0 - 0.3))


plt.xlabel('Angular Frequency ($\omega$)')
plt.ylabel('|H(j$\omega$)|')
plt.title('Magnitude Plot of H(j$\omega$) for an RLC Circuit')

plt.ylim(6, 10)
plt.xlim(108, 115)

plt.legend()
plt.grid(True)
plt.savefig('h_plot.png', dpi = 300, bbox_inches = 'tight')
