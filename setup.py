from cx_Freeze import setup, Executable
import sys

name = "ITL Bookmark"
version = "1.1.0"
description = "The app that it's efficient work for the url user manage"
author = "Ruri Shibata and Ren Murayama"
url = "https://github.com/shibainu1986/Bookmark"

# UUIDは一度決めたら変更しない
upgrade_code = "{7A37B0C0-64E1-479D-A64C-6CCFCB2E1149}"

# ----------------------------------------------------------------
# セットアップ
# ----------------------------------------------------------------
shortcut_table = [
    ('DesktopShortcut',        # Shortcut
     'DesktopFolder',          # Directory_
     "ITL Bookmark",               # Name
     'TARGETDIR',              # Component_
     '[TARGETDIR]ITL Bookmark.exe',   # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR',              # WkDir
    )
    ]

# Table dictionary
msi_data = {'Shortcut': shortcut_table}

# 追加モジュールで必要なものを packages に入れる
build_exe_options = {'packages': ["asyncio"],
                     'excludes': [
                         ],
                     'includes': [],
                     'include_files': [".venv/", "icons/", "backend/", "frontend/"]
}

bdist_msi_options = {'upgrade_code': upgrade_code,
                     'add_to_path': False,
                     'data': msi_data
}

options = {
    'build_exe': build_exe_options,
    'bdist_msi': bdist_msi_options
}

# CUI : None
# base = None 
base = 'Win32GUI' if sys.platform == 'win32' else None

icon = "icons/icon.ico"

# exe にしたい python ファイルを指定
exe = Executable(script="main.py",
                 targetName="ITL Bookmark.exe",
                 base=base,
                 icon=icon
                 )

# セットアップ
setup(name=name,
      version=version,
      author=author,
      url=url,
      description=description,
      options=options,
      executables=[exe]
      )