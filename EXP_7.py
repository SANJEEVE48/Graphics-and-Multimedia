import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from playsound import playsound
import cv2
import threading

class MultimediaApp:
    def __init__(self, master):
        self.master = master
        master.title("Enhanced Multimedia App")
        master.geometry("400x450")

        self.panel = tk.Label(master)
        self.panel.pack(pady=10)

        self.btn_img = tk.Button(master, text="Select and Show Image", command=self.select_image)
        self.btn_img.pack(pady=5)

        self.btn_audio = tk.Button(master, text="Select and Play Audio", command=self.select_audio)
        self.btn_audio.pack(pady=5)

        self.btn_video = tk.Button(master, text="Select and Play Video", command=self.select_video)
        self.btn_video.pack(pady=5)

        # For video playback inside tkinter window
        self.video_window = None
        self.cap = None

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if file_path:
            try:
                img = Image.open(file_path)
                img = img.resize((300, 300))
                img_tk = ImageTk.PhotoImage(img)
                self.panel.configure(image=img_tk)
                self.panel.image = img_tk
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image:\n{e}")

    def select_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav")])
        if file_path:
            threading.Thread(target=lambda: playsound(file_path)).start()

    def select_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mov")])
        if file_path:
            self.play_video(file_path)

    def play_video(self, file_path):
        if self.cap is not None:
            self.cap.release()
        self.cap = cv2.VideoCapture(file_path)

        if self.video_window is None or not self.video_window.winfo_exists():
            self.video_window = tk.Toplevel(self.master)
            self.video_window.title("Video Player")
            self.video_label = tk.Label(self.video_window)
            self.video_label.pack()

        self.show_frame()

    def show_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert BGR (OpenCV) to RGB (PIL)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
            self.video_window.after(30, self.show_frame)
        else:
            self.cap.release()
            self.video_window.destroy()
            self.video_window = None

if __name__ == "__main__":
    root = tk.Tk()
    app = MultimediaApp(root)
    root.mainloop()
