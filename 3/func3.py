import gzip
import json
import re

def Engrand_data():
    value = ""
    #謎のエラーが解決しなかったのでネットで色々参考にした。なぜダメだったのかわからない(解凍してから普通に行ごとにロードしようとすると失敗する)#
    with gzip.open('/Users/Kazuki/programming/100/3/jawiki-country.json.gz', 'rt') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                value = data_json['text']
                break
    return value

def category_lines():
    data = Engrand_data()
    lines = data.split("\n")
    p = re.compile('\[\[Category:')
    values = []

    for i in range(len(lines)):
        if (p.match(lines[i])): values.append(lines[i])

    return lines
