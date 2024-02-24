import numpy as np
import matplotlib.pyplot as plt

# Function to generate AP terms using numpy
def generate_ap_numpy(start, end, common_difference):
    ap_terms = np.arange(start, end + 1, common_difference)
    return ap_terms

# Generate AP terms using numpy
start_term = 105
end_term = 994
common_difference = 7
ap_terms = generate_ap_numpy(start_term, end_term, common_difference)

# Plotting the stem plot with dots at the top
plt.stem(ap_terms, linefmt='b-', markerfmt='bo', basefmt='k-', bottom=105)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()