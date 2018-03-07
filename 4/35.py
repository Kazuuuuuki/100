import func4 as f
values = set()
data = f.morpheme()

tmp = ""
for i in range(len(data)):
    for j in range(len(data[i])):
        if(j == (len(data[i]) - 1) and tmp != ""):
            if(data[i][j]["pos"] == "名詞"):
                tmp += data[i][j]["surface"]
            values.add(tmp)
            break

        if(data[i][j]["pos"] != "名詞" and tmp != ""):
            values.add(tmp)
            tmp = ""

        if(data[i][j]["pos"] == "名詞"):
            tmp += data[i][j]["surface"]


print(values)