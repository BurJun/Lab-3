import tkinter as tk
from PIL import Image, ImageTk
import random

APP_W = 680 
APP_H = 380
BG_PATH = "/Users/evgeniaburtseva/Downloads/image43.jpg"  


#генерация ключа
def gen_key():
    p1, p2 = sorted(random.sample(range(1, 27), 2))
    letters = [chr(64+i) for i in range(p1, p2+1)]
    mid = "".join(random.choice(letters) for _ in range(7))
    key = f"{p1:02d} {mid} {p2:02d}"
    key_var.set(key)
    root.clipboard_clear(); root.clipboard_append(key)


def init_frames(root):
    root.title("Ключ")
    root.geometry(f"{APP_W}x{APP_H}")
    root.resizable(False, False)
    img = Image.open(BG_PATH).resize((APP_W, APP_H))
    bg_img = ImageTk.PhotoImage(img)
    bg_lbl = tk.Label(root, image=bg_img)
    bg_lbl.image = bg_img
    bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)
    card = tk.Frame(root, bg="#1b1e24")
    card.place(relx=0.5, rely=0.5, anchor="center", width=520, height=170)
    return card


def init_ui(card):
    tk.Label(card, text="ГЕНЕРАТОР КЛЮЧЕЙ",
             fg="#e8f0ff", bg="#1b1e24",
             font=("Segoe UI", 16, "bold")).pack(pady=(16, 8))
    ent = tk.Entry(card, textvariable=key_var,
                   font=("Consolas", 18, "bold"),
                   justify="center", relief="flat",
                   bg="#0f1116", fg="#e8f0ff")
    ent.pack(padx=20, fill="x")
    btns = tk.Frame(card, bg="#1b1e24"); btns.pack(pady=12)
    tk.Button(btns,text="Сгенерировать",
              command=gen_key,width=16,
              bg="#2b6cff",fg="#1b1e24",  
              highlightthickness=0,relief="flat",).grid(row=0, column=0, padx=6)
    tk.Button(btns, text="Скопировать",
              command=lambda: (root.clipboard_clear(),
                               root.clipboard_append(key_var.get())),
              width=12, bg="#2b6cff", fg="#1b1e24",
              activebackground="#3a404a", relief="flat").grid(row=0, column=1, padx=6)
    root.bind("<Return>", lambda e: gen_key())


if __name__ == "__main__":
    root = tk.Tk()
    key_var = tk.StringVar()
    card = init_frames(root)
    init_ui(card)
    gen_key()
    root.mainloop()
