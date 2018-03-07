import func4 as f
values = set()
data = f.morpheme()

for i in range(len(data)):
    for j in range(len(data[i])):
        if(j > len(data[i]) - 3): break
        cond = (data[i][j]["pos"] == "名詞" and data[i][j+2]["pos"] == "名詞" \
               and data[i][j+1]["pos1"] == "連体化" and data[i][j+1]["surface"] == "の")
        if(cond):
            values.add(data[i][j]["surface"] + "の" + data[i][j+2]["surface"])


print(values)