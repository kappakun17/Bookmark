from backend.database import Database

def test_data(db):
    db.insert_category("Training");

    db.insert_folder("Programming", 1)   #1
    db.insert_folder("Excel", 1)        #2
    db.insert_folder("Word", 1)         #3

    db.insert_bookmark("Angular", "https://angular.io/", "The frontend library Google provide", 1, None)
    db.insert_bookmark("React", "https://ja.reactjs.org/", "The frontend library Meta provide", 1, None)
    db.insert_bookmark("Vue", "https://jp.vuejs.org/index.html", "The frontend library by Evan You", 1, None)

    db.insert_bookmark("マクロの始め方", "https://my-tax-nology.com/the-way-of-starting-excel-vba-anyway", "マクロの始め方。", 2, None)
    db.insert_bookmark("秒で帰れる裏技集", "https://wanko.fun/1516/", "秒で買えるための裏技を発見。", 2, None)
    db.insert_bookmark("マクロのデータ型一覧", "https://www.tipsfound.com/vba/02008", "Byte, Integer, Long, Single, Doubleなど記載。", 2, None)

    db.insert_category("英語")

    db.insert_folder("文法",2)          #4
    db.insert_folder("単語",2)          #5

    db.insert_bookmark("English Labo", "https://www.rarejob.com/englishlab/column/20211027_02/", "英語の文法の覚え方！", 4, None)
    db.insert_bookmark("文法本ランキング一覧", "https://www.amazon.co.jp/%E4%BA%BA%E6%B0%97%E3%81%AE%E8%8B%B1%E8%AA%9E-%E6%96%87%E6%B3%95%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0/s?k=%E4%BA%BA%E6%B0%97%E3%81%AE%E8%8B%B1%E8%AA%9E+%E6%96%87%E6%B3%95%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0", "一番初めの英文法気になるなあ", 4, None)
    db.insert_bookmark("単語帳", "https://www.eigo-duke.com/tango/tangoindex.html", "効率的に英単語を学べるサイトを発見。", 5, None)

# db = Database()

# db.rebuildDB()
# db.consistOfDB()

# test_data(db)

# # print(db.select_all_categorys_and_folders())
# print(db.select_relate_folder_bookmark(2))