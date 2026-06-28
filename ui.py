import customtkinter as ctk
from tkinter import filedialog
from converter import convert_to_mp3
import threading, os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Video → MP3")
        self.geometry("500x300")
        self.input_path = ""

        ctk.CTkLabel(self, text="Video to MP3 Converter", font=("Arial", 20, "bold")).pack(pady=20)

        self.btn_select = ctk.CTkButton(self, text="Select Video", command=self.select_file)
        self.btn_select.pack(pady=10)

        self.label_file = ctk.CTkLabel(self, text="No file selected", wraplength=400)
        self.label_file.pack()

        self.progress = ctk.CTkProgressBar(self, width=400)
        self.progress.set(0)
        self.progress.pack(pady=10)

        self.btn_convert = ctk.CTkButton(self, text="Convert", command=self.start_conversion, state="disabled")
        self.btn_convert.pack(pady=10)

        self.label_status = ctk.CTkLabel(self, text="")
        self.label_status.pack()

    def select_file(self):
        path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.mkv *.avi *.mov *.webm")])
        if path:
            self.input_path = path
            self.label_file.configure(text=os.path.basename(path))
            self.btn_convert.configure(state="normal")

    def start_conversion(self):
        self.btn_convert.configure(state="disabled")
        self.progress.start()
        self.label_status.configure(text="Converting...")
        threading.Thread(target=self.run_conversion, daemon=True).start()

    def run_conversion(self):
        out = self.input_path.rsplit(".", 1)[0] + ".mp3"
        success, err = convert_to_mp3(self.input_path, out)
        self.progress.stop()
        self.progress.set(1 if success else 0)
        if success:
            self.label_status.configure(text=f"✅ Saved: {os.path.basename(out)}")
        else:
            # Show full error in a popup so you can read it
            import tkinter.messagebox as mb
            mb.showerror("Conversion Error", f"FFmpeg error:\n\n{err}")
            self.label_status.configure(text="❌ Conversion failed")
        self.btn_convert.configure(state="normal")

if __name__ == "__main__":
    App().mainloop()