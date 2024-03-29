import matplotlib.pyplot as plt
import numpy as np
with open("values.dat") as file:
    data_str = file.read()
sequences = data_str.split('\n')
sequences = np.array(sequences)[np.where(np.array(sequences) != "")].tolist()
data_array = np.array(list(map(np.vectorize(float), map(lambda line: line.split('\t'), sequences))))
x = data_array[:, 0].astype(int)
y1 = data_array[:, 1]
y2 = data_array[:, 2]
plt.xlim(0,20)
plt.ylim(0, 150)
plt.stem(x, y1,markerfmt='o')
#plt.title("Plotting x(n)")
plt.xlabel("n")
plt.ylabel("x(n)")
plt.xticks(np.arange(0,21, 1))
plt.yticks(np.arange(0,150, 5))
plt.savefig("Figure_1.png")
plt.show()
plt.clf()
plt.xlim(0,20)
plt.ylim(-125,25)
plt.stem(x, y2,markerfmt='o')
#plt.title("Plotting x(n)")
plt.xlabel("n")
plt.ylabel("x(n)")
plt.xticks(np.arange(0,21, 1))
plt.yticks(np.arange(-125,26, 5))
plt.savefig("Figure_2.png")
plt.show()
