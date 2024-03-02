import matplotlib.pyplot as plt

# Read data from the DAT file
data = []
with open('output.dat', 'r') as file:
    for line in file:
        line = line.strip().split('\t')
        data.append([int(line[0]), int(line[1])])
n =  list(range(0, 10)) 
x = [entry[0] for entry in data]
y = [entry[1] for entry in data]

plt.stem(n, y, use_line_collection=True,label='by using convultion')
plt.scatter(n,x, color='r', marker='x', s=100, label='simulation')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)

save_path = 'main.png'  # Update this path
plt.savefig(save_path)
plt.show()
