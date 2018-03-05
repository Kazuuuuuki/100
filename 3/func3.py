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

    return values

def dic_of_template():
    data = Engrand_data()
    lines = data.split("\n")
    p = re.compile('{{基礎情報')
    p2 = re.compile('}}')
    p3 = re.compile('=')
    p4 = re.compile('\*')
    values = {}
    # こうやって大きな値で設定するのは競プロとかしか使えない手かもしれない
    start_line = 100000
    for i in range(len(lines)):
        if (p.search(lines[i]) and start_line == 100000):
            start_line = i
        if (i > start_line):
            if (p3.search(lines[i])):
                s = p3.search(lines[i])
                start_id = s.start()
                values[lines[i][1:start_id]] = lines[i][start_id + 2:]
                tmp = lines[i][1:start_id]
            if (p4.match(lines[i])):
                s = p4.search(lines[i])
                end_id = s.end()
                values[tmp] = values[tmp] + lines[i][end_id + 1:]

        if (p2.match(lines[i]) and i > start_line):
            break

    return values

def dic_of_template_26():
    data = Engrand_data()
    lines = data.split("\n")
    p = re.compile('{{基礎情報')
    p2 = re.compile('}}')
    p3 = re.compile('=')
    p4 = re.compile('\*')
    values = {}
    # こうやって大きな値で設定するのは競プロとかしか使えない手かもしれない
    start_line = 100000
    for i in range(len(lines)):
        if (p.search(lines[i]) and start_line == 100000):
            start_line = i
        if (i > start_line):
            lines[i] = lines[i].replace('\'\'\'\'\'', '')
            lines[i] = lines[i].replace('\'\'\'', '')

            if (p3.search(lines[i])):
                s = p3.search(lines[i])
                start_id = s.start()
                values[lines[i][1:start_id-1]] = lines[i][start_id + 2:]
                tmp = lines[i][1:start_id-1]
            if (p4.match(lines[i])):
                s = p4.search(lines[i])
                end_id = s.end()
                values[tmp] = values[tmp] + lines[i][end_id + 1:]

        if (p2.match(lines[i]) and i > start_line):
            break

    return values


