import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
from tkinter import filedialog
import os
import urllib.request
import tkinter.font as tkFont
from zipfile import ZipFile
from PIL import  ImageDraw, ImageFont
def download_font(font_name, font_url):
    # Font dosyasını indir
    font_zip_path = f"{font_name}.zip"
    urllib.request.urlretrieve(font_url, font_zip_path)
    
    # Zip dosyasını aç
    with ZipFile(font_zip_path, 'r') as zipObj:
        # Zip dosyasındaki tüm dosyaları çıkar
        zipObj.extractall()
    
    # Zip dosyasını sil
    os.remove(font_zip_path)

    # Resim eklemek için bir boşluk oluşturmak
def load_image():
        image = Image.open("resim.png")  # 'resim.png' yerine kendi resim dosyanızın adını verin
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo  # Resmi global olarak saklamak için bu satırı ekliyoruz

def on_button_click():
    folder_path = filedialog.askdirectory()
    if folder_path:
        progress_window = tk.Toplevel(root)
        progress_window.title("Yükleniyor...")
        progress_window.configure(bg='black')
        
        loading_label = tk.Label(progress_window, text="LOADING.", font=("Hotel De Paris", 16), bg='black', fg='white')

        loading_label.pack(pady=20)
        
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("white.Horizontal.TProgressbar", troughcolor='black', bordercolor='black', background='white', lightcolor='white', darkcolor='white')
        
        progress_bar = ttk.Progressbar(progress_window, style="white.Horizontal.TProgressbar", orient="horizontal", length=300, mode="determinate")
        progress_bar.pack(pady=10)
        
        for i in range(101):
            time.sleep(0.05)
            progress_bar["value"] = i
            progress_bar.update()
        
        progress_window.destroy()



# Ana uygulama penceresini oluşturmak için Tkinter'ı başlat
root = tk.Tk()
if os.path.exists("PressStart2P-Regular.ttf"):
    download_font("PressStart2P-Regular.ttf", "https://fonts.google.com/download?family=Press%20Start%202P")
else:
    print("indirildi")
    
root.title("Tkinter Örnek")

label = tk.Label(root, text="Python arayüzüne hoş geldiniz!", font=("Hotel De Paris", 16))
label.pack(pady=20)
print(tk.font.families())

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


image_label = tk.Label(root)
image_label.pack(pady=10)

load_image()  # Resmi yüklemek için fonksiyonu çağırıyoruz

# Ana döngüyü başlatmak
root.mainloop()