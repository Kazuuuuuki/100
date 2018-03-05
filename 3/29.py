#わからなかったのでググった(cheatした)
#cheatしたので、それぞれ自分で使えるように調べた
#反省: apiの仕様をちゃんと読もう！

import urllib.parse, urllib.request
import json
import func3 as f
data = f.dic_of_template_26()
file = data['国旗画像']
#URLエンコード
title = urllib.parse.quote(file)
url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + title \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

request = urllib.request.Request(url,
    headers={'User-Agent': 'NLP100_Python(@watanabe)'})
connection = urllib.request.urlopen(request)
#バイト文字列からdecode()で文字列に変換する必要がある。
data = json.loads(connection.read().decode())
url = data['query']['pages']['-1']['imageinfo'][0]['url']
print(url)