import cv2
import numpy as np
import matplotlib.pyplot as plt
def rotate_image(image, angle):#untuk memutar gambar (image) sebesar sudut (angle) yang ditentukan.
    rows, cols = image.shape[:2]#untuk mendapatkan dimensi (jumlah baris dan kolom) dari gambar image menggunakan metode .shape pada objek gambar tersebut.
    center = (cols / 2, rows / 2)# untuk menghitung pusat (koordinat tengah) dari gambar dengan menggunakan nilai cols (jumlah kolom) dan rows (jumlah baris) yang telah diambil sebelumnya.
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)#untuk mendapatkan matriks transformasi rotasi yang akan digunakan untuk memutar gambar.
    rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))# untuk melakukan transformasi affine pada gambar image dengan menggunakan matriks transformasi rotation_matrix yang dihasilkan sebelumnya.
    return rotated_image#untuk mengembalikan hasil gambar yang telah diputar sebagai hasil dari fungsi rotate_image.

img = cv2.imread('flower.jpg')#Baca gambar sumber
rotated_img = rotate_image(img, angle=-180)#Rotasi foto

cv2.imshow('Rotation Image', rotated_img)#untuk menampilkan gambar yang telah diputar dengan menggunakan jendela tampilan dari pustaka OpenCV.
cv2.waitKey(0)#ntuk menunggu hingga tombol apa pun ditekan pada jendela tampilan yang dibuat dengan cv2.imshow().
cv2.destroyAllWindows()#Menutup Jendela