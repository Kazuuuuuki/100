import func4 as f
values = set()
data = f.morpheme()

for i in range(len(data)):
    for j in range(len(data[i])):
        if(data[i][j]["pos"] == "名詞" and data[i][j]["pos1"] == "サ変接続"):
            values.add(data[i][j]["surface"])


print(values)