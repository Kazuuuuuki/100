import func3 as f
import re
##data全体ではなくて、25の処理に追加するのに直す
data = f.Engrand_data()
lines = data.split("\n")
p = re.compile('{{基礎情報')
p2 = re.compile('}}')
p3 = re.compile('=')
p4 = re.compile('\*')
values = {}
#こうやって大きな値で設定するのは競プロとかしか使えない手かもしれない
start_line = 100000
for i in range(len(lines)):
    if (p.search(lines[i]) and start_line == 100000):
        start_line = i
    if(i > start_line):
        lines[i] = lines[i].replace('\'\'\'\'\'', '')
        lines[i] = lines[i].replace('\'\'\'', '')

        if(p3.search(lines[i])):
            s = p3.search(lines[i])
            start_id = s.start()
            values[lines[i][1:start_id-1]] = lines[i][start_id + 2:]
            tmp = lines[i][1:start_id-1]
        if(p4.match(lines[i])):
            s = p4.search(lines[i])
            end_id = s.end()
            values[tmp] = values[tmp] + lines[i][end_id + 1:]

    if (p2.match(lines[i]) and i > start_line):
        break

print(values)