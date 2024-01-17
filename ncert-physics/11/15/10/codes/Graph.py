import numpy as np
import matplotlib.pyplot as plt

path_diff = [400, 50, 62.5, 93.75]
phase_diff = []

for i in range(0, 4):
    phase_diff.append(2*3.14*0.008*path_diff[i])
    
#print(phase_diff)

# Define the function
def equation(x):
    return 2 * np.cos(2 * np.pi * (-0.008 * x))

# Plot the first graph
plt.figure(figsize=(8, 5))

# Generate x values
x_values = np.linspace(0, 450, 1000)

# Calculate y values
y_values = equation(x_values)

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.plot(0, 0, 'ro', markersize=8, label='x_1')
plt.plot(400, 0, 'ro', markersize=8, label='x_2')

plt.text(-0.8, -0.3, '  $x_1$', verticalalignment='bottom', horizontalalignment='right', color='black')
plt.text(395, -0.2, '  $x_2$ ', verticalalignment='bottom', horizontalalignment='right', color='black')

plt.text(0, -0.2, '  (0, 0)', verticalalignment='top', horizontalalignment='left', color='black')
plt.text(380, -0.3, ' (400, 0)', verticalalignment='top', horizontalalignment='left', color='black')

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = 2cos2π(10t -0.008x +0.35)')
plt.grid(True)

arrow_start = (0, -2)
arrow_end = (400, -2)
plt.annotate('', xy=arrow_start, xytext=arrow_end,
             arrowprops=dict(facecolor='purple', arrowstyle='<->'))
plt.text(200, -2.2, '  $400cm$ ', verticalalignment='bottom', horizontalalignment='right', color='purple')

plt.savefig('graph1.png', bbox_inches='tight', pad_inches=0.2)

# Plot the second graph
plt.figure(figsize=(8, 5))

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.plot(100, 0, 'ro', markersize=8, label='x_1')
plt.plot(150, 0, 'ro', markersize=8, label='x_2')

plt.text(89, -0.2, '  $x_1$', verticalalignment='bottom', horizontalalignment='right', color='black')
plt.text(180, -0.2, '  $x_2$ ', verticalalignment='bottom', horizontalalignment='right', color='black')

plt.text(80, -0.2, '  (100, 0)', verticalalignment='top', horizontalalignment='left', color='black')
plt.text(152, 0.3, ' (150, 0)', verticalalignment='top', horizontalalignment='left', color='black')

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = 2cos2π(10t - 0.008x +0.35)')
plt.grid(True)

arrow_start = (100, -2)
arrow_end = (150, -2)
plt.annotate('', xy=arrow_start, xytext=arrow_end,
             arrowprops=dict(facecolor='purple', arrowstyle='<->'))
plt.text(145, -2.2, '  $50cm$ ', verticalalignment='bottom', horizontalalignment='right', color='purple')

plt.savefig('graph2.png', bbox_inches='tight', pad_inches=0.2)

# Plot the third graph
plt.figure(figsize=(8, 5))

# Generate x values
x_values = np.linspace(0, 250, 1000)

# Calculate y values
y_values = equation(x_values)

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.plot(0, 0, 'ro', markersize=8, label='x_1')
plt.plot(65, 0, 'ro', markersize=8, label='x_2')

plt.text(-0.5, -0.3, '  $x_1$', verticalalignment='bottom', horizontalalignment='right', color='black')
plt.text(70, -0.3, '  $x_2$ ', verticalalignment='bottom', horizontalalignment='right', color='black')

plt.text(-0.9, -0.2, ' (0, 0)', verticalalignment='top', horizontalalignment='left', color='black')
plt.text(70, 0.3, ' ($\\frac{\\lambda}{2}$, 0)', verticalalignment='top', horizontalalignment='left', color='black')

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = 2cos2π(10t - 0.008x +0.35)')
plt.grid(True)

arrow_start = (0, -2)
arrow_end = (65, -2)
plt.annotate('', xy=arrow_start, xytext=arrow_end,
             arrowprops=dict(facecolor='purple', arrowstyle='<->'))
plt.text(40, -2, '$\\frac{\\lambda}{2}cm$', verticalalignment='bottom', horizontalalignment='right', color='purple')

plt.savefig('graph3.png', bbox_inches='tight', pad_inches=0.2)

# Plot the fourth graph
plt.figure(figsize=(8, 5))

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.plot(0, 0, 'ro', markersize=8, label='x_1')
plt.plot(93, 0, 'ro', markersize=8, label='x_2')

plt.text(1, -0.3, '  $x_1$', verticalalignment='bottom', horizontalalignment='left', color='black')
plt.text(104, -0.3, '  $x_2$ ', verticalalignment='bottom', horizontalalignment='right', color='black')

plt.text(0.9, 0.2, ' (0, 0)', verticalalignment='top', horizontalalignment='left', color='black')
plt.text(68, 0.3, ' ($\\frac{3\\lambda}{4}$, 0)', verticalalignment='top', horizontalalignment='left', color='black')

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = 2cos2π(10t - 0.008x +0.35)')
plt.grid(True)

arrow_start = (0, -2)
arrow_end = (94, -2)
plt.annotate('', xy=arrow_start, xytext=arrow_end,
             arrowprops=dict(facecolor='purple', arrowstyle='<->'))
plt.text(50, -2, '$\\dfrac{3\\lambda}{4}cm$', verticalalignment='bottom', horizontalalignment='right', color='purple')

plt.savefig('graph4.png', bbox_inches='tight', pad_inches=0.2)
