import pandas as pd
index = list(range(1, 4))
index_max = max(index)
for i in index:
    url =  'http://300.wi2.co.jp/area/1/?prefecture=04&str_category=a%253A1%253A%257Bi%253A0%253Bs%253A1%253A%25226%2522%253B%257D&str_small_category=a%253A5%253A%257Bi%253A0%253Bs%253A3%253A%25226%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25226%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25226%252C3%2522%253Bi%253A3%253Bs%253A3%253A%25226%252C5%2522%253Bi%253A4%253Bs%253A3%253A%25226%252C4%2522%253B%257D&search_type=xlos&pageID=0/ClassSkeletownController.php?action=area&emx=1&isp=&pageID=' +str(i)

    df = pd.read_html(url, match='スポット')
    # print(len(df))
    # print(df[0])
    df[0] = df[0].drop(columns='地図')
    if i == 1:
        df[0].to_csv("/Users/abekeishi/Public/Programing/Python3/Wi2Map/Wi2Map_宮城県_オッフィス・学校.csv", index=False)
    elif i != 1:
        df[0].to_csv("/Users/abekeishi/Public/Programing/Python3/Wi2Map/Wi2Map_宮城県_オッフィス・学校.csv", mode = 'a', header =False, index=False)

    print('Now Loading.... >>> {0: 3.0f}%'.format(i/index_max*100))
# ^---------これまでのプログラム
# ↓新コード
# 実行の様子を標準出力しながらログに残したい

# urlの基礎パーツを定義
for Prefecture_Id in range(1, 48):
    url_head = 'http://300.wi2.co.jp/area/1/?prefecture=' + str(Prefecture_Id)
    for Category_ID in range(1, 9):
        Category = '&str_category=a%253A1%253A%257Bi%253A0%253Bs%253A1%253A%2522' + str(Category_ID) + '%2522%253B%257D&'
        if Category_ID == 1:
            StrSmallCategory = ('str_small_category=a%253A8%253A%257Bi%253A0%253Bs%253A3%253A%25221%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25221%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25221%252C4%2522%253Bi%253A3%253Bs%253A3%253A%25221%252C6%2522%253Bi%253A4%253Bs%253A3%253A%25221%252C7%2522%253Bi%253A5%253Bs%253A3%253A%25221%252C8%2522%253Bi%253A6%253Bs%253A3%253A%25221%252C9%2522%253Bi%253A7%253Bs%253A4%253A%25221%252C10%2522%253B%257D')
        elif Category_ID ==2:
            StrSmallCategory = ('str_small_category=a%253A5%253A%257Bi%253A0%253Bs%253A3%253A%25222%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25222%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25222%252C3%2522%253Bi%253A3%253Bs%253A3%253A%25222%252C4%2522%253Bi%253A4%253Bs%253A3%253A%25222%252C5%2522%253B%257D')
        elif Category_ID ==3:
            StrSmallCategory = ('str_small_category=a%253A10%253A%257Bi%253A0%253Bs%253A3%253A%25223%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25223%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25223%252C3%2522%253Bi%253A3%253Bs%253A3%253A%25223%252C4%2522%253Bi%253A4%253Bs%253A3%253A%25223%252C5%2522%253Bi%253A5%253Bs%253A3%253A%25223%252C6%2522%253Bi%253A6%253Bs%253A3%253A%25223%252C7%2522%253Bi%253A7%253Bs%253A3%253A%25223%252C9%2522%253Bi%253A8%253Bs%253A4%253A%25223%252C10%2522%253Bi%253A9%253Bs%253A3%253A%25223%252C8%2522%253B%257D')
        elif Category_ID ==4:
            StrSmallCategory = ('str_small_category=a%253A5%253A%257Bi%253A0%253Bs%253A3%253A%25224%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25224%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25224%252C3%2522%253Bi%253A3%253Bs%253A3%253A%25224%252C4%2522%253Bi%253A4%253Bs%253A3%253A%25224%252C5%2522%253B%257D')
        elif Category_ID ==5:
            StrSmallCategory = ('str_small_category=a%253A10%253A%257Bi%253A0%253Bs%253A3%253A%25225%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25225%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25225%252C3%2522%253Bi%253A3%253Bs%253A3%253A%25225%252C4%2522%253Bi%253A4%253Bs%253A3%253A%25225%252C5%2522%253Bi%253A5%253Bs%253A3%253A%25225%252C6%2522%253Bi%253A6%253Bs%253A3%253A%25225%252C7%2522%253Bi%253A7%253Bs%253A3%253A%25225%252C9%2522%253Bi%253A8%253Bs%253A4%253A%25225%252C10%2522%253Bi%253A9%253Bs%253A3%253A%25225%252C8%2522%253B%257D')
        elif Category_ID ==6:
            StrSmallCategory = ('str_small_category=a%253A5%253A%257Bi%253A0%253Bs%253A3%253A%25226%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25226%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25226%252C3%2522%253Bi%253A3%253Bs%253A3%253A%25226%252C5%2522%253Bi%253A4%253Bs%253A3%253A%25226%252C4%2522%253B%257D')
        elif Category_ID ==7:
            StrSmallCategory = ('str_small_category=a%253A3%253A%257Bi%253A0%253Bs%253A3%253A%25227%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25227%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25227%252C3%2522%253B%257D')
        elif Category_ID ==8:
            StrSmallCategory = ('str_small_category=a%253A6%253A%257Bi%253A0%253Bs%253A3%253A%25228%252C1%2522%253Bi%253A1%253Bs%253A3%253A%25228%252C2%2522%253Bi%253A2%253Bs%253A3%253A%25228%252C3%2522%253Bi%253A3%253Bs%253A3%253A%25228%252C4%2522%253Bi%253A4%253Bs%253A3%253A%25228%252C5%2522%253Bi%253A5%253Bs%253A3%253A%25228%252C6%2522%253B%257D')
        else:
            print ('Error Category_ID')
        # 同一パラメータ
        url_ID1 ='&search_type=xlos&pageID=0/ClassSkeletownController.php?action=area&emx=1&isp=&pageID='
        URL_path = url_head + Category +StrSmallCategory
        while :
            TablePageID += 1
            URL_path = URL_path + str(TablePageID)
            #URLの完成
            # 表の読み込み関数を呼び出しURLを渡す。

ページの読み込みの数に関して
もし、next pageタグがあればlast pageタグを探索(単に"次へ"という文字列の有無で判断してもいいかもしれない)
あればlast pageの文字を取得。最大値とする。
なければnext pageの手前の数を取得
next pageもなければ1ページのみと判断して終了


def ReadTable(str: URL):


    forでurlを逐次変更して処理に繋げる



    1つ目のテーブル取得


    都道府県名とカテゴリの文字列取得
    全ステップの都道府県とカテゴリが同一か調べる。

    2つ目のテーブルを取得
    前回の結果と比較

    表が前回と同じなら終了
