import requests
import bs4
import re
import sys
import os

res = requests.get('http://300.wi2.co.jp/area/1/?prefecture=11&str_category=a%253A1%253A%257Bi%253A0%253Bs%253A1%253A%25227%2522%253B%257D&str_small_category=a%253A3%253A%257Bi%253A0%253Bs%253A3%253A%25227%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25227%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25227%252C3%2522%253B%257D&search_type=xlos&pageID=0/ClassSkeletownController.php?action=area&emx=1&isp=&postKey=099ababb4bc7d8c7b4eb375983b2bd9a')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
# elems = soup.select('.details')
elems = soup.find_all("a")
regex = r'^(?=\[.*[0-9]*\]|[0-9])(?!.*[a-zA-Z]).*$'
# [0-9]*|^(?!.*[a-zA-Z])'
lastPage = 1
# 標準出力 -> ファイル出力の切り替え
fo = open('Wi2log.txt', 'w')
sys.stdout = fo
pattern = re.compile(regex)
for elem in elems:
    match_txt = pattern.search(elem.text)
    if match_txt:
        integer = match_txt.group()
        integer = integer.replace('[', '').replace(']', '')
        pageNo = int(integer)
        if pageNo > lastPage: lastPage = pageNo


print(lastPage)
    # if not "地図" in elem.text:
    #     print(elem.text)


# aタグ内のテキストを取得。
# 英字, 日本語は除外し数字と記号のみ取得
# []は削除して数値を取得
# 取得した数字の最大値からページ数を割り出す。
# 多分上記のやり方が一番早いと思う。
# ただ、同じ処理が2回回っているのでどうやって効率化するか今後の課題
#
# aタグ内のテキストを取得
# pythonのinなどを駆使して数字のみ取り出す。
# 数字の最大値からページ数を割り出す。
#
# ページの読み込みの数に関して
# もし、next pageタグがあればlast pageタグを探索(単に"次へ"という文字列の有無で判断してもいいかもしれない)
# あればlast pageの文字を取得。最大値とする。
# なければnext pageの手前の数を取得
# next pageもなければ1ページのみと判断して終了
