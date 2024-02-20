import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)  

theta = np.sin(4.187 * t)

max_value = np.max(theta)
min_value = np.min(theta)

plt.figure(figsize=(8, 6))
line, = plt.plot(t, theta, color='blue')  
plt.axhline(y=max_value, color='gray', linestyle='--')  
plt.axhline(y=min_value, color='red', linestyle='--')  
plt.text(0.1, max_value * 1.05, r'$\theta^\prime(0)$', fontsize=12, color='blue')  
plt.text(0.1, min_value * 0.95, r'$-\theta^\prime(0)$', fontsize=12, color='red')  
plt.xlabel('t')
plt.ylabel('θ(t)')
yticks = np.arange(min_value, max_value * 1.2, max_value * 0.25)
format_label = np.vectorize(lambda val: '{:.2f}($\Theta\'(0)$)'.format(val))
yticklabels = format_label(yticks)
plt.yticks(yticks, yticklabels)
plt.grid(True)

plt.legend([line], [r'$\theta(t) = \theta^\prime(0) \, \sin(4.187t)$'], loc='upper right', bbox_to_anchor=(1, 1.02))

plt.show()

