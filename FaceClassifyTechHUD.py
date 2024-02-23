import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import shutil
from UmutAtac_KadirYildiz import *
folder_path = ""
kisiler = []
l = 0
class ImageGalleryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Gallery")
        self.folder_path = filedialog.askdirectory()
        self.image_frame = tk.Frame(root)
        self.image_frame.pack(padx=10, pady=10)
        self.l = l
        self.person1 = ""
        self.person2 = ""
        self.loadimages = []

        label = tk.Label(root, text=" resimleri yükle,resmin üstüne tıkla ve sabırla bekle ardından resimleri kaydet.", font=("Hotel De Paris", 16))
        label.pack(pady=20)

        button = tk.Button(root, text="Resimleri Yükle", command=self.load_images)
        button.pack()
        
        self.selected_option = tk.StringVar()
        option_frame = tk.Frame(root)
        option_frame.pack(pady=10)

        
        self.option1 = tk.Radiobutton(option_frame, text="1 Kişilik", variable=self.selected_option, value="option1")
        self.option1.grid(row=0, column=0, padx=5)
        
        self.option2 = tk.Radiobutton(option_frame, text="2 kişilik", variable=self.selected_option, value="option2")
        self.option2.grid(row=0, column=1, padx=5)
        button = tk.Button(root, text="Resimleri Kaydet", command=self.save_images_to_folder)
        button.pack()

    def Yuklemeekrani(self):
        if self.folder_path:
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



    def kontrol(self,dizi,explorer):
            liste= []
            for i, image in enumerate(os.listdir(explorer)):
                for x in range(len(dizi)): 
                    if dizi[x][0] == i + 1:
                        folder = "galeri/" + image
                        liste.append(folder)
            return liste
        
    def open_file(self,image_path):
         new_window = tk.Toplevel(self.root)
         new_window.title("Tıkladığınız kişinin Fotoğrafları")
         img = Image.open(image_path)
         photo = ImageTk.PhotoImage(img)

         label = tk.Label(new_window, image=photo)
         label.image = photo
         label.pack()
         
    def on_image_click(self,image_path,person):
        self.l = self.l+1
        self.secili_secenek = self.selected_option.get()
        if self.secili_secenek == "option1":
            person1 = "kisi" + str(person)
            image_files = tekkisiarama(self.folder_path, person1)
            self.loadimages = image_files 
            new_window = tk.Toplevel(self.root)
            for i, image_file in enumerate(image_files):
                                image_path = os.path.join(self.folder_path, image_file)
                                img = Image.open(image_path)
                                img = img.resize((200, 200))
                                photo = ImageTk.PhotoImage(img)
                    
                                label = tk.Label(new_window,image=photo)
                                label.photo = photo
                                label.grid(row=i // 4, column=i % 4, padx=10, pady=10)
                                
        elif self.secili_secenek == "option2":
            if  self.l <= 1:
                self.person1 = "kisi" + str(person)
            
            if self.l == 2:
                self.person2 = "kisi" + str(person)
                image_files = ikikisiarama(self.folder_path, self.person1, self.person2)
                self.loadimages = image_files
                new_window = tk.Toplevel(self.root)
                print(image_files)
                for i, image_file in enumerate(image_files):
                                    image_path = os.path.join(self.folder_path, image_file)
                                    img = Image.open(image_path)
                                    img = img.resize((200, 200))
                                    photo = ImageTk.PhotoImage(img)
                        
                                    label = tk.Label(new_window,image=photo)
                                    label.photo = photo
                                    label.grid(row=i // 4, column=i % 4, padx=10, pady=10)
        return image_files                           
          
         
    def load_images(self):
            okuma(self.folder_path, kisiler)
            self.kontrol(kisiler,self.folder_path)
            self.show_images_in_folder()
            
    def save_images_to_folder(self):
            destination_folder = filedialog.askdirectory(title="Select a destination folder")
            if destination_folder:
                image_files =  self.loadimages
                for i, image_file in enumerate(image_files):
                    source_path = os.path.join(self.folder_path, image_file)
                    destination_path = os.path.join(destination_folder, image_file)
                    shutil.copy(source_path, destination_path)
                    print("Image saved")


    def show_images_in_folder(self):
        # Get a list of image files in the selected folder
        print(kisiler)
        image_files = kisiler

        for i, image_file in enumerate(image_files):
            for x in range(len(self.folder_path)):
                if kisiler[i][0] == x+1:
                    image_path = os.path.join(self.folder_path, image_file[2])
                    img = Image.open(image_path)
                    img = img.resize((200, 200))
                    photo = ImageTk.PhotoImage(img)
        
                    label = tk.Label(self.image_frame,image=photo,text=f"{i+1}. kişi")
                    label.photo = photo
                    label.grid(row=i // 4, column=i % 4, padx=10, pady=10)                   
                    label.bind("<Button-1>", lambda event, person=i+1, path=image_path: self.on_image_click(path,person))
if __name__ == "__main__":
        root = tk.Tk()
        app = ImageGalleryApp(root)
        root.mainloop()
