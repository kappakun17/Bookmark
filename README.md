# Bookmark
このアプリは、よく使用するリンクを保存するアプリです。

必要なリンクがすぐに見つけられなかったり、お気に入り等で保存していても乱雑になりがちなリンクを

簡単に保存、追加、削除できます。

- **Bookmarkアプリの３つの特徴**

  ①カテゴリー別に保存できる

  ②メモ機能がついている

  ③アプリ内で直接webページを開いて閲覧できるようにWebView機能がついている


![Component 2](https://user-images.githubusercontent.com/107255635/200999425-e8d8f1c6-534f-4e50-9f8a-b30dc16c2c82.png)


## アプリのダウンロード
ITL関係者のみ、以下のアプリをダウンロードすることが可能です。

ダウンロードは[こちら](https://microsoft.sharepoint.com/:u:/t/JPITLAllMember/ETNWFP6O_OxItFWpmvOzyc0Bf2Al45ZuBdo_IdcCCfqjjg)から。


## 開発者向け🚀

このコードを利用し、カスタマイズや、アップデートに挑戦したい方は以下のステップを踏んでください。

1.pythonを持っていない方は、python3 の[インストール](https://www.python.org/downloads/)


2.ITL Bookmarkレポジトリをクローン

```
git clone https://github.com/shibainu1986/Bookmark.git
```

3.仮想環境構築
```
py -m venv .venv
```

4.仮想環境に入る
```
.venv\Scripts\activate
```

5.必要なライブラリーをインストール
```
py -m pip install -r requirement.txt
```

6.アプリ起動

```
py main.py
```

※アプリのパッケージ化は以下の通りです。

```
py setup.py bdist_msi
```