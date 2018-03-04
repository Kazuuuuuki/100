import func3 as f
import re

data = f.Engrand_data()
lines = data.split("\n")
p = re.compile('(\[\[)([^]#\|]*)(]])')
p2 = re.compile('(\[\[)([^]\|]*)(\|)([^]\|]*)(]])')
for i in range(len(lines)):
    tmp = re.sub(p, r'\2', lines[i])
    tmp = re.sub(p2, r'\4', tmp)
    lines[i] = tmp
    print(lines[i])

