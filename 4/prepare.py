import MeCab
mecab = MeCab.Tagger("-Ochasen")
with open("/Users/Kazuki/programming/100/4/neko.txt", "r") as f:
    data = f.read()
    with open("/Users/Kazuki/programming/100/4/neko.txt.mecab", "w") as f:
        f.write(mecab.parse(data))

