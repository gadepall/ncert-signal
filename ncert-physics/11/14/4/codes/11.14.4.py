import matplotlib.pyplot as plt
import numpy as np

def plot_and_save(file_path, function_label, save_filename):
    data = np.loadtxt(file_path)
    t = data[:, 0]
    function_data = data[:, 1]
    plt.plot(t, function_data)
    plt.xlabel('Time (t)')
    plt.ylabel('Function Value')
    plt.title(function_label)
    plt.grid(True)
    plt.savefig(save_filename)
    plt.clf()

# Plot and save each function in a separate graph
plot_and_save('11.14.4 fd1.txt', r'$\sin(\omega t) - \cos(\omega t)$', 'fig1.png')
plot_and_save('11.14.4 fd2.txt', r'$\sin^3(\omega t)$', 'fig2.png')
plot_and_save('11.14.4 fd3.txt', r'$3\cos\left(\frac{\pi}{4} - 2\omega t\right)$', 'fig3.png')
plot_and_save('f11.14.4 fd4.txt', r'$\cos(\omega t) + \cos(3\omega t) + \cos(5\omega t)$', 'fig4.png')
plot_and_save('11.14.4 fd5.txt', r'$\exp(-\omega^2 t^2)$', 'fig5.png')
plot_and_save('11.14.4 fd6.txt', r'$1 + \omega t + \omega^2 t^2$', 'fig6.png')

