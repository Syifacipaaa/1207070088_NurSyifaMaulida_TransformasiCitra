import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("flower.jpg")# untuk membaca citra dengan nama file "flower.jpg" menggunakan fungsi cv.imread dari pustaka OpenCV.
fig, ax = plt.subplots(1, 3, figsize=(16, 8))# untuk membuat sebuah figure (gambar) dengan tiga sumbu (axes) secara sejajar dalam satu baris.
# image size being 0.15 times of  original size
image_scaled = cv.resize(image, None, fx=0.15,fy=0.15)# untuk mengubah ukuran citra image dengan faktor skala tertentu.
ax[0].imshow(cv.cvtColor(image_scaled,cv.COLOR_BGR2RGB))#untuk menampilkan citra image_scaled pada sumbu pertama (ax[0]) menggunakan fungsi imshow dari modul matplotlib.pyplot.
ax[0].set_title("Linear Interpolation Scale")#untuk memberikan judul
# image size being 2 times of original size
image_scaled_2 = cv.resize(image, None, fx=2,fy=2, interpolation=cv.INTER_CUBIC)# untuk mengubah ukuran citra image dengan faktor skala 2 menggunakan metode interpolasi BICUBIC.
ax[1].imshow(cv.cvtColor(image_scaled_2,cv.COLOR_BGR2RGB))##untuk menampilkan citra image_scaled pada sumbu pertama (ax[1]) menggunakan fungsi imshow dari modul matplotlib.pyplot.
ax[1].set_title("Cubic Interpolation Scale")#untuk memberikan judul
# image size being 0.15 times of original size

image_scaled_3 = cv.resize(image, (200, 400),interpolation=cv.INTER_AREA)
ax[2].imshow(cv.cvtColor(image_scaled_3,cv.COLOR_BGR2RGB))#untuk menampilkan citra image_scaled pada sumbu pertama (ax[2]) menggunakan fungsi imshow dari modul matplotlib.pyplot.
ax[2].set_title("Skewed Interpolation Scale")#untuk memberikan judul
plt.show()#Menampilkan hasil citra