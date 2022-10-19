
class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "Category(" + self.name + ")"
    
    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class Folder:
    def __init__(self, id, name, category_id):
        self.id = id
        self.name = name
        self.category_id = category_id

    def __str__(self):
        return "Folder(" + self.name + ")"

    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category_id': self.category_id,
        }

class Category_Folders:
    def __init__(self, category, folders):
        self.category = category
        self.folders = folders
    
    def __str__(self):
        return self.category + "/" + str(len(self.folders)) + "Folders"
    
    def dict(self):
        return {
            'id': self.category.id,
            'name': self.category.name,
            'folders':[folder.dict() for folder in self.folders]
        }

class Bookmark:
    def __init__(self, id, name, url, memo, folder_id, icon):
        self.id = id
        self.name = name
        self.url = url
        self.memo = memo
        self.folder_id = folder_id,
        self.icon = icon


    def __str__(self):
        return "Bookmark(" + self.name + ")"

    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'memo': self.memo,
            'folder_id': self.folder_id,
            'icon': self.icon
        }
