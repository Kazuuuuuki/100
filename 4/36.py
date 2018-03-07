import func4 as f
values = {}
data = f.morpheme()

for i in range(len(data)):
    for j in range(len(data[i])):
        values[data[i][j]["surface"]] = 0


for i in range(len(data)):
    for j in range(len(data[i])):
        values[data[i][j]["surface"]] += 1



print(sorted(values.items(), key=lambda x: -x[1]))