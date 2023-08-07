import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def on_button_click():
    label.config(text="Merhaba, Tkinter!")

# Ana uygulama penceresini oluşturmak için Tkinter'ı başlat
root = tk.Tk()
root.title("Tkinter Örnek")

# Etiket oluşturmak
label = tk.Label(root, text="Python arayüzüne hoş geldiniz!", font=("Helvetica", 16))
label.pack(pady=20)

# Buton oluşturmak
button = tk.Button(root, text="Tıkla", command=on_button_click)
button.pack()

# İki seçenekli radyo butonlar oluşturmak
selected_option = tk.StringVar()
option_frame = ttk.Frame(root)
option_frame.pack(pady=10)

option1 = ttk.Radiobutton(option_frame, text="Seçenek 1", variable=selected_option, value="option1")
option1.grid(row=0, column=0, padx=5)

option2 = ttk.Radiobutton(option_frame, text="Seçenek 2", variable=selected_option, value="option2")
option2.grid(row=0, column=1, padx=5)

# Resim eklemek için bir boşluk oluşturmak
def load_image():
    image = Image.open("resim.png")  # 'resim.png' yerine kendi resim dosyanızın adını verin
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo  # Resmi global olarak saklamak için bu satırı ekliyoruz

image_label = tk.Label(root)
image_label.pack(pady=10)

load_image()  # Resmi yüklemek için fonksiyonu çağırıyoruz

# Ana döngüyü başlatmak
root.mainloop()