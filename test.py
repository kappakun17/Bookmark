from backend.database import Database

db = Database()

db.rebuildDB()
db.consistOfDB()

# categoryはありません。
print(db.select_category_id(1))

# category を作ります
db.insert_category("Japan")

# categoryはあります
print(db.select_category_id(1))

# folderを三つ作ります
db.insert_folder("Japanese Food", 1)
db.insert_folder("Japanese Music", 1)
db.insert_folder("Japanese Temples", 1)

print(",".join([str(folder) for folder in db.select_relate_category_folder(1)]))

db.insert_bookmark("Tabelog", "http://tabelog.com", "Good restaurant ranking", 1)
db.insert_bookmark("Gurunavi", "http://gurunavi.com", "Also good restaurant ranking", 1)
db.insert_bookmark("Google Maps", "http://maps.google.com", "Find where good restaurants are", 1)

print(",".join([
    str(bookmark)
    for bookmark in db.select_relate_folder_bookmark(1)
]))

# すべて返す

print(db.all_select_data())

db.close()