from PIL import Image, ImageTk
import tkinter as tk
import threading

class GifPlayer(threading.Thread):
    def __init__(self, path: str, label: tk.Label):
        super().__init__(daemon=True)
        self._please_stop = False
        self.path = path
        self.label = label
        self.duration = []  # フレーム表示間隔
        self.frame_index = 0
        self.frames = []  # 読み込んだGIFの画像フレーム
        self.last_frame_index = None
        # フレームの読み込み
        self.load_frames()

    def load_frames(self):
        if isinstance(self.path, str):
            img = Image.open(self.path)
            frames = []
            duration = []
        else:
            return

        frame_index = 0
        is_not_duration = False  # drationの指定がないとき
        try:
            while True:
                frames.append(ImageTk.PhotoImage(img.copy()))
                img.seek(frame_index)
                frame_index += 1
                try:
                    # フレーム表示間隔情報を保存
                    duration.append(img.info['duration']) 
                # durationの指定がないとき
                except KeyError:
                    # フラグをON
                    is_not_duration = True
        except EOFError:
            # フラグがONならフレームぶんのdurationを作成する
            if is_not_duration:
                duration = [0] * len(frames)
            self.frames = frames
            self.duration = duration
            self.last_frame_index = frame_index -1

    def run(self):
        self.next_frame()

    def next_frame(self):
        if not self._please_stop:
            # configでフレーム変更
            self.label.configure(image=self.frames[self.frame_index])
            self.frame_index += 1
            # 最終フレームになったらフレームを０に戻す
            if self.frame_index > self.last_frame_index:
                self.frame_index = 0
        # durationミリ秒あとにコールバック
        self.label.after(self.duration[self.frame_index], self.next_frame)

    def stop(self):
        self._please_stop = True


class TkGif():
    def __init__(self, path, label: tk.Label) -> None:
        self.path = path
        self.label = label

    def play(self):
        self.player = GifPlayer(self.path, self.label)
        self.player.start()

    def stop_loop(self):
        """loopを止める"""
        self.player.stop()


# if __name__ == '__main__':

#     path = './frontend/src/img/loading/test.gif'

#     root = tk.Tk()
#     root.geometry('800x800')
#     root.configure(bg='#FCFCFF')

#     main_frame = tk.Frame(root)
#     main_frame.pack()

#     label = tk.Label(main_frame, borderwidth=0)
#     label.pack()

#     gif_player = TkGif(path, label)
#     gif_player.play()

#     root.mainloop()