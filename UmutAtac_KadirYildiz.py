import face_recognition
import cv2
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def read_img(path):
    img = cv2.imread(path)
    (h, w) = img.shape[:2]
    width = 500
    ratio = width / float(w)
    height = int(h * ratio)
    return cv2.resize(img, (width, height))

known_encodings = []
known_names = []

#    app = ImageGalleryApp(root)

#print(resimler)
kilit = []
birkez = 1
resimsayisi = 5
kisi = []
j=0
sayac = 0
def okuma(galeri, kilit):
    for file in os.listdir(galeri):
        global sayac
        sayac +=1
        img_path = os.path.join(galeri, file)
        try:
            img = read_img(img_path)
            if img is None:
                print(f"Error reading image: {img_path}")
                continue  # Skip to the next image if reading fails
    
            img_encs = face_recognition.face_encodings(img)
            if not img_encs:
                print(f"No face found in image: {img_path}")
                continue  # Skip to the next image if no face is detected
    
            face_locations = face_recognition.face_locations(img)
            img = read_img(galeri + '/' + file)
            img_encs = face_recognition.face_encodings(img)
            face_locations = face_recognition.face_locations(img)
            print(file)
            for (img_enc, (top, right, bottom, left)) in zip(img_encs, face_locations):
                results = face_recognition.compare_faces(known_encodings, img_enc)
                #print(face_recognition.face_distance(known_encodings, img_enc))
                if True in results:
                    for i in range(len(results)):
                        if results[i]:
                            name = known_names[i]
                            #cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
                            #cv2.putText(img, name, (left+2, bottom+20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
                                #if birkez == 1:
                                    #resimsayisi = sayac - j 
                                    #print(resimsayisi)
                                    #im2 = read_img(unknown_dir + "/" + resimler[kilit[resimsayisi-1][0]-1])
                                    #cv2.imshow("img",im2)
                                    #cv2.waitKey(0)
                                    #birkez = 0
                else:   
                    global j
                    j+=1
                    #print("j = ",j)
                    #crop_img = img[top:bottom+100, left-50:right+100]
                    #cv2.imwrite('bilinen/bilinen{}.jpg'.format(j), crop_img)
                    known_encodings.append(img_enc)
                    kilit.append([sayac,"kisi",file])
                    known_names.append("kisi{}".format(j))
                    #cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
                    #cv2.putText(img,"Bilinmeyen Kisi,{}".format(j), (left+2,bottom+20), cv2.FONT_HERSHEY_PLAIN ,1,(255,255,255),1) 
            
        except Exception as e:
            print(f"An error occurred for image {img_path}: {e}")
            continue 
        
#kisiler = []
def returndizi(galeri,dizi,kilit):
    for h , file in enumerate(os.listdir(galeri)):
        for j in range(len(kilit)):
            if int(kilit[j][0])-1 == h:
                print(h)
                print(kilit[j][0]-1)
                dizi.append(file)
    return dizi
            
def show_images(images,galeri):
    originalPath = os.getcwd() 
    os.chdir(galeri)
    fig = plt.figure(figsize=(10, 10))
    columns = 4
    rows = 5
    for i in range(1, columns*rows +1):
        if i <= len(images):
            img = mpimg.imread(images[i-1])
            fig.add_subplot(rows, columns, i)
            plt.title(f" {i}")
            plt.subplots_adjust(hspace=0.5)
            plt.imshow(img)
    plt.show()
    os.chdir(originalPath)
    
#show_images(kisiler)
#arama = input("tek kişi için 1'e iki kişi aramak için 2 girin")

def ikikisiarama(galeri,a,b):
    d = 0
    e = 0
    arama = 2
    if arama == 2:
     for file in os.listdir(galeri):
        global sayac
        sayac += 1 
        img_path = os.path.join(galeri, file)
        try:
            img = read_img(img_path)
            if img is None:
                print(f"Error reading image: {img_path}")
                continue  # Skip to the next image if reading fails
    
            img_encs = face_recognition.face_encodings(img)
            if not img_encs:
                print(f"No face found in image: {img_path}")
                continue  # Skip to the next image if no face is detected
    
            face_locations = face_recognition.face_locations(img)
            print("resim okundu", file)
            print("---------------------")
            for (img_enc, (top, right, bottom, left)) in zip(img_encs, face_locations):
                results = face_recognition.compare_faces(known_encodings, img_enc)
                #print(face_recognition.face_distance(known_encodings, img_enc))
                if True in results:
                    for i in range(len(results)):
                        if results[i]:
                            name = known_names[i]
                            cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
                            cv2.putText(img, name, (left+2, bottom+20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
                            #cv2.imshow("img",img)
                            #cv2.waitKey(0)
                            if  e == 1:
                                if a == name:
                                    e=0
                                    d=0
                                    print("çalıştı d")
                                    kisi.append(file)
                            if d == 1:
                                if b == name:
                                    d=0
                                    e=0
                                    print("çalıştı e")
                                    kisi.append(file)
                            if a == name: 
                                    d = 1
                                    e = 0
                            if b == name:
                                    e= 1 
                                    d= 0
                            print("d   " ,d)
                            print("e   " , e)
                                #if birkez == 1:
                                    #resimsayisi = sayac - j 
                                    #print(resimsayisi)
                                    #im2 = read_img(unknown_dir + "/" + resimler[kilit[resimsayisi-1][0]-1])
                                    #cv2.imshow("img",im2)
                                    #cv2.waitKey(0)
                                    #birkez = 0
            
        except Exception as e:
            print(f"An error occurred for image {img_path}: {e}")
            continue  # Skip to the next image if any exception occurs
            
        d = 0
        e = 0
    return kisi

#show_images(kisi)
def tekkisiarama(galeri,a):
    for file in os.listdir(galeri):
             global sayac
             sayac += 1 
             img_path = os.path.join(galeri, file)
             try:
               img = read_img(img_path)
               if img is None:
                 print(f"Error reading image: {img_path}")
                 continue  # Skip to the next image if reading fails
    
               img_encs = face_recognition.face_encodings(img)
               if not img_encs:
                print(f"No face found in image: {img_path}")
                continue  # Skip to the next image if no face is detected
    
               face_locations = face_recognition.face_locations(img)
               print("resim okundu", file)
               print("---------------------")
               for (img_enc, (top, right, bottom, left)) in zip(img_encs, face_locations):
                               if not face_locations:
                                   continue  
                               results = face_recognition.compare_faces(known_encodings, img_enc)
                               #print(face_recognition.face_distance(known_encodings, img_enc))
                               if True in results:
                                   for i in range(len(results)):
                                       if results[i]:
                                           name = known_names[i]
                                           cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
                                           cv2.putText(img, name, (left+2, bottom+20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
                                           #cv2.imshow("img",img)
                                           #cv2.waitKey(0)
                                           if a == name:
                                            kisi.append(file)
                                               #if birkez == 1:
                                                   #resimsayisi = sayac - j 
                                                   #print(resimsayisi)
                                                   #im2 = read_img(unknown_dir + "/" + resimler[kilit[resimsayisi-1][0]-1])
                                                   #cv2.imshow("img",im2)
                                                   #cv2.waitKey(0)
                                                   #birkez = 0
                                                   
             except Exception as e:
               print(f"An error occurred for image {img_path}: {e}")
             continue  # Skip to the next image if any exception occurs
    return kisi
#show_images(kisi)
