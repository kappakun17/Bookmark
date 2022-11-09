import json
import sqlite3
from .model import Category, Folder, Bookmark, Category_Folders

class Database:
    DATABASE_SCHEMA = '''
        BEGIN TRANSACTION;
        CREATE TABLE IF NOT EXISTS "bookmark" (
            "id"	INTEGER NOT NULL UNIQUE,
            "name"	TEXT,
            "url"	TEXT NOT NULL,
            "memo"	TEXT,
            "folder_id"	INTEGER NOT NULL,
            "icon" BLOB,
            PRIMARY KEY("id" AUTOINCREMENT),
            FOREIGN KEY(folder_id) REFERENCES folder(id)
            ON UPDATE CASCADE ON DELETE CASCADE
        );
        CREATE TABLE IF NOT EXISTS "category" (
            "id"	INTEGER NOT NULL UNIQUE,
            "name"	TEXT NOT NULL UNIQUE,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
        CREATE TABLE IF NOT EXISTS "folder" (
            "id"	INTEGER NOT NULL UNIQUE,
            "name"	TEXT NOT NULL UNIQUE,
            "category_id"	INTEGER NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT),
            FOREIGN KEY(category_id) REFERENCES category(id)
            ON UPDATE CASCADE ON DELETE CASCADE
        );
        CREATE TABLE IF NOT EXISTS "setting" (
            "key"  TEXT NOT NULL UNIQUE,
            "value" TEXT
        );
        COMMIT;
    '''

    DELETE_DATABASE = '''
        BEGIN TRANSACTION;
        DROP TABLE IF EXISTS "bookmark";
        DROP TABLE IF EXISTS "category";
        DROP TABLE IF EXISTS "folder";
        DROP TABLE IF EXISTS "setting";
        COMMIT;
    '''

    def __init__(self) -> None:
        self.db = "sqlite3.db"
        self.con = sqlite3.connect(self.db, check_same_thread=False)
        self.con.execute("PRAGMA foreign_keys = ON")
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def close(self):
        self.cur.close()
        self.con.close()

    def consistOfDB(self):
        self.cur.executescript(self.DATABASE_SCHEMA)

    def rebuildDB(self):
        # 一度削除
        self.cur.executescript(self.DELETE_DATABASE)

        self.consistOfDB()

    def all_select_data(self):
        res = self.cur.execute("SELECT id, name FROM category")
        categories = [Category(row['id'], row['name']) for row in res]

        res = self.cur.execute("SELECT id, name, category_id FROM folder")
        folders = [Folder(row['id'], row['name'], row['category_id']) for row in res]
        [print(folder.dict()) for folder in folders]

        res = self.cur.execute("SELECT id, name, url, memo, folder_id, icon FROM bookmark")
        bookmarks = [Bookmark(row['id'], row['name'], row['url'], row['memo'], row['folder_id'], row['icon']) for row in res]

        selected_data = {
            'category': [category.dict() for category in categories],
            'folder': [folder.dict() for folder in folders],
            'bookmark': [bookmark.dict() for bookmark in bookmarks],
        }
        return json.dumps(selected_data, indent = 4, ensure_ascii=False)
    
    def select_all_categorys_and_folders(self):
        res_category = self.cur.execute("SELECT id, name FROM category")
        rows_category = res_category.fetchall()
        categorys = [Category(row['id'], row['name']) for row in rows_category]
        
        selected_data = []
        for category in categorys:
            folders = self.select_relate_category_folder(category.id)
            
            for folder in folders:
                print(folder.id, folder.name)
     
            
            data = Category_Folders(category, folders)
            selected_data.append(data.dict())
        
        return json.dumps(selected_data, indent = 4, ensure_ascii=False)


    def select_category_id(self, category_id):
        res = self.cur.execute("SELECT id, name FROM category WHERE id = ?", (category_id,))
        row = res.fetchone()
        if row is None:
            return None
        return Category(row['id'], row['name'])

    def select_relate_category_folder(self, category_id):
        res = self.cur.execute("SELECT id, name, category_id FROM folder WHERE category_id = ?", (category_id,))
        return [Folder(row['id'], row['name'], row['category_id']) for row in res]

    def insert_category(self, category_name):
        self.cur.execute("INSERT INTO category(name) VALUES (?)", (category_name,))
        self.con.commit()

    def update_categoryName(self, category_id, category_name):
        self.cur.execute("UPDATE category SET name = ? WHERE id = ?", (category_name, category_id))
        self.con.commit()

    def delete_category(self, category_id):
        self.cur.execute("DELETE FROM category WHERE id = ?", (category_id,))
        self.con.commit()

    def select_folder_id(self, folder_id):
        res = self.cur.execute("SELECT id, name, category_id FROM folder WHERE id = ?", (folder_id,))
        row = res.fetchone()
        if row is None:
            return None
        return Folder(row['id'], row['name'], row['category_id'])

    def select_relate_folder_bookmark(self, folder_id):
        res = self.cur.execute("SELECT id, name, url, memo, folder_id, icon FROM bookmark WHERE folder_id = ?", (folder_id,))
        bookmarks =  [Bookmark(row['id'], row['name'], row['url'], row['memo'], row['folder_id'], row['icon']) for row in res]
        selected_data = [bookmark.dict() for bookmark in bookmarks]
        return json.dumps(selected_data, indent=4, ensure_ascii=False)
       
    
    def insert_folder(self, folder_name, category_id):
        self.cur.execute("INSERT INTO folder(name, category_id) VALUES (?,?)", (folder_name, category_id))
        self.con.commit()

    def update_folderName(self, folder_id, folder_name):
        self.cur.execute("UPDATE folder SET name = ? WHERE id = ?", (folder_name, folder_id))
        self.con.commit()

    def delete_folder(self, folder_id):
        self.cur.execute("DELETE FROM folder WHERE id = ?", (folder_id,))
        self.con.commit()

    def select_bookmark_id(self, bookmark_id):
        res = self.cur.execute("SELECT id, name, url, memo, folder_id, icon FROM bookmark WHERE id = ?", (bookmark_id,))
        row = res.fetchone()
        if row is None:
            return None
        return Bookmark(row['id'], row['name'], row['url'], row['memo'], row['folder_id'], row['icon'])

    def insert_bookmark(self, bookmark_name, bookmark_url, bookmark_memo, folder_id, icon):
        self.cur.execute("INSERT INTO bookmark(name, url, memo, folder_id, icon) VALUES (?,?,?,?,?)", (bookmark_name, bookmark_url, bookmark_memo, folder_id, icon))
        self.con.commit()

    def update_bookmark(self, bookmark_id, bookmark_name, bookmark_url, bookmark_memo, folder_id, icon):
        self.cur.execute("UPDATE bookmark SET name = ?, url = ?, memo = ?, folder_id = ?, icon = ? WHERE id = ?", (bookmark_name, bookmark_url, bookmark_memo, folder_id, icon, bookmark_id))
        self.con.commit()

    def delete_bookmark(self, bookmark_id):
        self.cur.execute("DELETE FROM bookmark WHERE id = ?", (bookmark_id,))
        self.con.commit()

    def get_setting(self, key):
        res = self.cur.execute("SELECT value FROM setting WHERE key = ?", (key,))
        row = res.fetchone()
        if row is None:
            return None
        return row['value']

    def update_setting(self, key, value):
        self.cur.execute("INSERT INTO setting (key, value) VALUES(?, ?) ON CONFLICT(key) DO UPDATE SET value=excluded.value", (key, value))
        self.con.commit()
