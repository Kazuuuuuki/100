import func4 as f
values = set()
data = f.morpheme()

for i in range(len(data)):
    for j in range(len(data[i])):
        if(data[i][j]["pos"] == "動詞"):
            values.add(data[i][j]["base"])


print(values)