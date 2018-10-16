import pandas as pd
import requests
import bs4
import re
import sys
import os
import math

# constant parameter
END = 47 * 8
MAX_LEN = 30
URL_ID1 = '&search_type=xlos&pageID=0/ClassSkeletownController.php?action=area&emx=1&isp=&pageID='
# ------

def ReadTable(url):
    url = url + "1"
    df = pd.read_html(url)
    prefecture_category = df[0].drop(1)
    # print(prefecture_category)


# Progress Bar function
# progress_bar --> get_progressbar_str --> fresh
def get_progressbar_str(progress):
    BAR_LEN = int(MAX_LEN * progress)
    return ('[' + '=' * BAR_LEN +
            ('>' if BAR_LEN < MAX_LEN else '') +
            ' ' * (MAX_LEN - BAR_LEN) +
            '] %.1f%%' % (progress * 100.))
def fresh():
    sys.stderr.write('\n')
    sys.stderr.flush()

def progress_bar(curr_progress):
    progress = 1.0 * curr_progress / END
    sys.stderr.write('\r\033[K' + get_progressbar_str(progress))
    sys.stderr.flush()
# _______


# Main function
if __name__ == "__main__" :
    # 標準出力 -> ファイル出力の切り替え
    # fo = open('Wi2log.txt', 'w')
    # sys.stdout = fo
    progress_count= 0
    # urlの基礎パーツを定義
    for prefecture_id in range(1, 48):
        url_head = 'http://300.wi2.co.jp/area/1/?prefecture=' + str(prefecture_id)
        for category_id in range(1, 9):
            Category = '&str_category=a%253A1%253A%257Bi%253A0%253Bs%253A1%253A%2522' + str(category_id) + '%2522%253B%257D&'
            if category_id == 1:
                str_small_category = ('str_small_category=a%253A8%253A%257Bi%253A0%253Bs%253A3%253A%25221%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25221%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25221%252C4%2522%253Bi%253A3%253Bs%253A3%253A%25221%252C6%2522%253Bi%253A4%253Bs%253A3%253A%25221%252C7%2522%253Bi%253A5%253Bs%253A3%253A%25221%252C8%2522%253Bi%253A6%253Bs%253A3%253A%25221%252C9%2522%253Bi%253A7%253Bs%253A4%253A%25221%252C10%2522%253B%257D')
            elif category_id ==2:
                str_small_category = ('str_small_category=a%253A5%253A%257Bi%253A0%253Bs%253A3%253A%25222%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25222%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25222%252C3%2522%253Bi%253A3%253Bs%253A3%253A%25222%252C4%2522%253Bi%253A4%253Bs%253A3%253A%25222%252C5%2522%253B%257D')
            elif category_id ==3:
                str_small_category = ('str_small_category=a%253A10%253A%257Bi%253A0%253Bs%253A3%253A%25223%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25223%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25223%252C3%2522%253Bi%253A3%253Bs%253A3%253A%25223%252C4%2522%253Bi%253A4%253Bs%253A3%253A%25223%252C5%2522%253Bi%253A5%253Bs%253A3%253A%25223%252C6%2522%253Bi%253A6%253Bs%253A3%253A%25223%252C7%2522%253Bi%253A7%253Bs%253A3%253A%25223%252C9%2522%253Bi%253A8%253Bs%253A4%253A%25223%252C10%2522%253Bi%253A9%253Bs%253A3%253A%25223%252C8%2522%253B%257D')
            elif category_id ==4:
                str_small_category = ('str_small_category=a%253A5%253A%257Bi%253A0%253Bs%253A3%253A%25224%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25224%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25224%252C3%2522%253Bi%253A3%253Bs%253A3%253A%25224%252C4%2522%253Bi%253A4%253Bs%253A3%253A%25224%252C5%2522%253B%257D')
            elif category_id ==5:
                str_small_category = ('str_small_category=a%253A10%253A%257Bi%253A0%253Bs%253A3%253A%25225%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25225%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25225%252C3%2522%253Bi%253A3%253Bs%253A3%253A%25225%252C4%2522%253Bi%253A4%253Bs%253A3%253A%25225%252C5%2522%253Bi%253A5%253Bs%253A3%253A%25225%252C6%2522%253Bi%253A6%253Bs%253A3%253A%25225%252C7%2522%253Bi%253A7%253Bs%253A3%253A%25225%252C9%2522%253Bi%253A8%253Bs%253A4%253A%25225%252C10%2522%253Bi%253A9%253Bs%253A3%253A%25225%252C8%2522%253B%257D')
            elif category_id ==6:
                str_small_category = ('str_small_category=a%253A5%253A%257Bi%253A0%253Bs%253A3%253A%25226%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25226%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25226%252C3%2522%253Bi%253A3%253Bs%253A3%253A%25226%252C5%2522%253Bi%253A4%253Bs%253A3%253A%25226%252C4%2522%253B%257D')
            elif category_id ==7:
                str_small_category = ('str_small_category=a%253A3%253A%257Bi%253A0%253Bs%253A3%253A%25227%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25227%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25227%252C3%2522%253B%257D')
            elif category_id ==8:
                str_small_category = ('str_small_category=a%253A6%253A%257Bi%253A0%253Bs%253A3%253A%25228%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25228%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25228%252C3%2522%253Bi%253A3%253Bs%253A3%253A%25228%252C4%2522%253Bi%253A4%253Bs%253A3%253A%25228%252C5%2522%253Bi%253A5%253Bs%253A3%253A%25228%252C6%2522%253B%257D')
            else:
                print ('Error category_id')
            # 同一パラメータ
            progress_count += 1
            URL_path = url_head + Category +str_small_category + URL_ID1
            # print (str(prefecture_id) + " :" + str(category_id))
            ReadTable(URL_path)
            progress_bar(progress_count)


fresh()


        # URLパスを渡して読み込み関数の呼び出し。

# ページの読み込みの数に関して
# もし、next pageタグがあればlast pageタグを探索(単に"次へ"という文字列の有無で判断してもいいかもしれない)
# あればlast pageの文字を取得。最大値とする。
# なければnext pageの手前の数を取得
# next pageもなければ1ページのみと判断して終了


#
#
#     forでurlを逐次変更して処理に繋げる
#
#
#
#     1つ目のテーブル取得
#
#
#     都道府県名とカテゴリの文字列取得
#     全ステップの都道府県とカテゴリが同一か調べる。
#
#     2つ目のテーブルを取得
#     前回の結果と比較
#
#     表が前回と同じなら終了
