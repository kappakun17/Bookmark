from backend.database import Database

def initialize_dataset(db):
    db.insert_category("Welcome");

    db.insert_folder("To", 1)   #1

    db.insert_bookmark("ITL Bookmark", "https://github.com/shibainu1986/Bookmark", "ようこそ、ITL Bookmarkへ。このアプリを使うことで、URLの管理が円滑になります。こちらのブックマークはカテゴリーごと削除して、お使いください。", 1, None)
   