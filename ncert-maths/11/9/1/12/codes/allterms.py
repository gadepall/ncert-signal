import math
import matplotlib.pyplot as plt

# Defining x(n)
def x_n(n):
    if n < 0:
        return 0
    else:
        return (-1) / math.factorial(n)

# Get N from the user
print("//This program will plot the terms of the sequence up to x(n)// \n")
N = int(input("Enter the value of n: "))

# Generate the sequence up to N
print("...\nx( -1 ) = 0\n")
for x in range(N+1):
    {    
        print("x(", x, ") = ", x_n(x), "\n")
    }
print("...\n")

# Generate the sequence up to N
n_values = list(range(-2, N+1))
x_values = [x_n(n) for n in n_values]

# Plot the terms
plt.stem(n_values, x_values, markerfmt='o', linefmt='b-', basefmt='r-')
plt.title('Terms of the Sequence x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()
plt.savefig("allterms.png")

