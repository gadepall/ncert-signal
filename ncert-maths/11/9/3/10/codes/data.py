file_path = "data.dat"

with open(file_path, "r") as file:
    data = [list(map(float, line.strip().split())) for line in file]

n_values = [item[0] for item in data]
x = [item[1] for item in data]

print(sum(x))

