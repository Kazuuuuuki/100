import func3 as f
import re


data = f.dic_of_template_26()
p = re.compile('(\[\[)([^]#\|]*)(]])')
p2 = re.compile('(\[\[)([^]\|]*)(\|)([^]\|]*)(]])')
for key in data:
    tmp = re.sub(p, r'\2', data[key])
    tmp = re.sub(p2, r'\4', tmp)
    data[key] = tmp
    print(key + ": " + data[key])