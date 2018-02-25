import func3 as f
import re
#==?==を1, ===?===を２、====?====を３とする。

#繰り返しが多いクソコードなので、再利用する場合は戻って直す
data = f.Engrand_data()
lines = data.split("\n")
p = re.compile('====.*====')
values3 = []
used = set()
for i in range(len(lines)):
    if (p.search(lines[i])):
        values3.append(lines[i][4:len(lines[i]) - 4])
        used.add(i)



values2 = []
p = re.compile('===.*===')
for i in range(len(lines)):
    if (p.search(lines[i]) and not(i in used)):
        values2.append(lines[i][3:len(lines[i]) - 3])
        used.add(i)



values1 = []
p = re.compile('==.*==')
for i in range(len(lines)):
    if (p.search(lines[i]) and not(i in used)):
        values1.append(lines[i][2:len(lines[i]) - 2])


for i in range(len(values1)):
    print(values1[i] + ": 1")


for i in range(len(values2)):
    print(values2[i] + ": 2")


for i in range(len(values3)):
    print(values3[i] + ": 3")





