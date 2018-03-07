import re
def morpheme():
    p = re.compile('記号-空白')
    p2 = re.compile('記号-句点')
    p3 = re.compile('-')
    end = re.compile('EOS\n')
    values = []
    values.append([])
    with open("/Users/Kazuki/programming/100/4/neko.txt.mecab", "r") as f:
        lines = f.readlines()
        flag = 0
        for i in range(len(lines)):
            if (p.search(lines[i])): continue;
            if (end.search(lines[i])): continue;
            if(p2.search(lines[i])):
                flag += 1
                values.append([])
            else:
                data = lines[i].split('\t')
                obj = {}
                obj["surface"] = data[0]
                obj["base"] = data[2]
                if(p3.search(data[3])):
                    data = data[3].split("-")
                    obj["pos"] = data[0]
                    obj["pos1"] = data[1]
                else:
                    obj["pos"] = data[3]
                    obj["pos1"] = data[3]
                values[flag].append(obj)

        return values