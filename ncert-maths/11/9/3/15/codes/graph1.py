import matplotlib.pyplot as plt
import numpy as np
with open(r"C:\\MyCodes\Azgar\\values.dat") as file:
    data_str = file.read()
sequences = data_str.split('\n')
sequences = np.array(sequences)[np.where(np.array(sequences) != "")].tolist()
data_array = np.array(list(map(np.vectorize(float), map(lambda line: line.split('\t'), sequences))))
n = data_array[:, 0].astype(int) #term number
x = data_array[: , 1]    #x(n) (n+1)th term
y = data_array[:, 2]     #y(n) sum of n+1 terms
plt.xlim(0, 20)
plt.ylim(0, 2500)
plt.stem(n,y, markerfmt='o', linefmt='b-', basefmt='b-') 
plt.scatter(n, y, color='blue')  
plt.xlabel("n")
plt.ylabel("y(n)")
plt.xticks(np.arange(0, 21, 1))
plt.yticks(np.arange(0, 2500, 100))

index_y6 = np.where(n == 6)[0][0]
plt.stem(n[index_y6], y[index_y6], markerfmt='o', linefmt='r-', basefmt='r-')

plt.legend()
#plt.grid(True)
#plt.savefig("Figure_1.png")
plt.show()
plt.clf()
plt.xlim(0,20)
plt.ylim(0, 750)
plt.stem(n, x,markerfmt='o')
#plt.title("Plotting x(n)")
plt.xlabel("n")
plt.ylabel("x(n)")
plt.xticks(np.arange(0,21, 1))
plt.yticks(np.arange(0,750, 50))
#plt.grid(True)
#plt.savefig("Figure_2.png")
plt.show()
