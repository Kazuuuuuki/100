import func3 as f
import re
#相変わらず題意がわからないので、File:もしくはファイル；以降のファイル名を取得できるようにした。
data = f.Engrand_data()
lines = data.split("\n")
p = re.compile('File:')
values = []
for i in range(len(lines)):
    if (p.search(lines[i])):
        s = p.search(lines[i])
        start_i = s.end()
        p2 = re.compile('\|')
        s2 = p2.search(lines[i])
        end_i = s2.start()
        values.append(lines[i][start_i:end_i])

p = re.compile('ファイル:')
for i in range(len(lines)):
    if (p.search(lines[i])):
        s = p.search(lines[i])
        start_i = s.end()
        p2 = re.compile('.\|')
        s2 = p2.search(lines[i])
        end_i = s2.start()
        values.append(lines[i][start_i:end_i+1])

print(values)