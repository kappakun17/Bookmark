import tkinter as tk

INTRODUCTION_TEXT = """
このアプリは、ITLでよく使用するリンクを保存するアプリです。

ITLでは、トレーニングやイベント等で多くのリンクを使用します。
必要なリンクがすぐに見つけられなかったり、
お気に入り登録等で保存していても乱雑になりがちです。

そこで、リンクを簡単に保存、追加、削除できる「ITL Bookmark」アプリを開発しました。

「ITL Bookmark」の3つの特徴

①カテゴリー別に保存できる
②視覚的に分かりやすく表示できる（アイコンの表示、メモ機能）
③アプリ内で直接webページを開いて閲覧ができるようにWebView機能がついている
"""


class my_Dialogs_IntroductionScreen(tk.Frame):
    def __init__(self, master=None, title=None, cnf={}, db=None, **kw):
        super().__init__(master, cnf, **kw)
        super().configure(bg='#ffffff')

        self.db = db

        introduction_label = tk.Label(self, text=INTRODUCTION_TEXT, bg='#ffffff', borderwidth=0, highlightthickness=0,
                                      relief="flat", activebackground='#ffffff', font=("HGPｺﾞｼｯｸE", "12"), foreground='#000000', justify='left', padx=20)
        introduction_label.grid(
            column=0,
            columnspan=2,
            row=0,
        )

        self.example_image = tk.PhotoImage(
            file="frontend/src/img/dialog/dialog_introduction_example.png")
        example_label = tk.Label(
            self, image=self.example_image, relief="flat", padx=20, pady=20)
        example_label.grid(
            column=0,
            columnspan=2,
            row=1,
        )

        dismiss_btn = tk.Button(self, text='この説明を次回から省略する', cursor='hand2', bg='#D9D9D9',
                                borderwidth=0, highlightthickness=0, relief="flat", activebackground='#fffdf8', font=("HGPｺﾞｼｯｸE", "18"), padx=50, pady=30, command=lambda: self.hide_introduction_action())
        dismiss_btn.grid(
            column=0,
            row=2,
        )

        close_btn = tk.Button(self, text='閉じる', cursor='hand2', bg='#D9D9D9',
                              borderwidth=0, highlightthickness=0, relief="flat", activebackground='#fffdf8', font=("HGPｺﾞｼｯｸE", "18"), padx=50, pady=30, command=lambda: master.destroy())
        close_btn.grid(
            column=1,
            row=2,
        )

        self.pack(padx=0, fill='x')

    def hide_introduction_action(self):
        self.db.update_setting('hide_introduction', 'true')
        self.master.destroy()
