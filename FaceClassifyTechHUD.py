import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
from tkinter import filedialog
import os
import urllib.request
import tkinter.font as tkFont
from zipfile import ZipFile
from PIL import  ImageDraw, ImageFont, Image, ImageTk
from UmutAtac_KadirYildiz import *
from tkinter import filedialog
from PIL import Image, ImageTk

def open_file(file_path):
    new_window = tk.Toplevel(root)
    img = Image.open(file_path)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(new_window, image=photo)
    label.image = photo
    label.pack()

# Tkinter arayüzü kodları
# ...
# Tkinter arayüzü kodları devam eder...
kilit = []
folder_path = ""
kisiler = []
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
def load_image(resim):
        image = Image.open(resim)  # 'resim.png' yerine kendi resim dosyanızın adını verin
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo  # Resmi global olarak saklamak için bu satırı ekliyoruz
def integrate_face_recognition(folder_path):
    # Burada yüz tanıma işlemleri yapılacak
    # ...

    # Elde edilen sonuçları tkinter arayüzünde göstermek için bir fonksiyon çağırabiliriz
    # Tkinter penceresi oluşturma
    root = tk.Tk()
    root.title("Yüz Tanıma Sonuçları")
    # Resimleri göstermek için bir frame oluşturma
    image_frame = tk.Frame(root)
    image_frame.pack(padx=10, pady=10)
    # Her bir resmi ImageTk formatına dönüştürüp gösterme
    for i, image_path in enumerate(folder_path):
        img = Image.open(image_path)
        img = img.resize((200, 200), Image.ANTIALIAS)  # Resmi istediğiniz boyuta küçültmek için
        photo = ImageTk.PhotoImage(img)
        
        label = tk.Label(image_frame, image=photo)
        label.image = photo  # Referansı saklamak için bu satırı ekliyoruz
        label.grid(row=i // 4, column=i % 4, padx=10, pady=10)  # Örnek olarak 4 sütunlu bir düzen kullanıyoruz

    root.mainloop()
# Örnek bir fonksiyon, gerçek sonuçları buraya ekleyebilirsin


def kontrol(dizi, explorer):
    global kilit
    kilit = biseyler(explorer, kisiler, kilit)

    for i, image in enumerate(os.listdir(explorer)):
        if dizi[i][0] == i + 1:
            folder = "galeri/" + image
            open_file(folder)

def on_button_click():
    folder_path = filedialog.askdirectory()
    okuma(folder_path, kisiler)
    global kilit
    kilit = biseyler(folder_path, kisiler, kilit)
    kontrol(kilit,folder_path);
    if folder_path:
        progress_window = tk.Tk()
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

# Buton oluşturmak
button = tk.Button(root, text="Ara", command=on_button_click)
button.pack()

# İki seçenekli radyo butonlar oluşturmak
selected_option = tk.StringVar()
option_frame = ttk.Frame(root)
option_frame.pack(pady=10)

option1 = ttk.Radiobutton(option_frame, text="1 Kişilik", variable=selected_option, value="option1")
option1.grid(row=0, column=0, padx=5)

option2 = ttk.Radiobutton(option_frame, text="2 kişilik", variable=selected_option, value="option2")
option2.grid(row=0, column=1, padx=5)


image_label = tk.Label(root)
image_label.pack(pady=10)

load_image("resim.png")  # Resmi yüklemek için fonksiyonu çağırıyoruz

# Ana döngüyü başlatmak
root.mainloop()