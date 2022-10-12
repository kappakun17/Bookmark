import sqlite3


DATABASE_SCHEMA = '''
    BEGIN TRANSACTION;
    CREATE TABLE IF NOT EXISTS "bookmark" (
        "id"	INTEGER NOT NULL UNIQUE,
        "name"	TEXT,
        "url"	TEXT NOT NULL,
        "memo"	TEXT,
        "folder_id"	INTEGER NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
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
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    COMMIT;
'''



db = "../../sqlite3.db"
con = sqlite3.connect(db)

cur = con.cursor()
cur.executescript(DATABASE_SCHEMA)
cur.close()
