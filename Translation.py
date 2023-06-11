import cv2 as cv#untuk mengimpor modul cv2 .
import numpy as np#untuk mengimpor numpy dan memberikan as np ke modul tersebut.
import matplotlib.pyplot as plt#untuk mengimpor modul matplotlib.pyplot dan memberikan alias plt ke modul tersebut.

image = cv.imread("flower.jpg")# untuk membaca citra dengan nama file "flower.jpg" menggunakan fungsi cv.imread dari pustaka OpenCV.
h,w = image.shape[:2]# untuk mengambil dimensi baris (h) dan kolom (w) dari citra image menggunakan metode shape pada objek citra.
half_height, half_width = h//4, w//8# untuk menginisialisasi variabel half_height dan half_width dengan nilai setengah dari tinggi (h) dan delapan-pembagian (delapan bagi) dari lebar (w) citra.
transition_matrix = np.float32([[1, 0,half_width],[0, 1,half_height]])#untuk membuat matriks transisi transition_matrix menggunakan modul numpy (np.float32).
img_transition =cv.warpAffine(image,transition_matrix, (w, h))# untuk melakukan transformasi translasi pada citra image menggunakan matriks transisi transition_matrix yang telah dibuat sebelumnya.
plt.imshow(cv.cvtColor(img_transition,cv.COLOR_BGR2RGB))#untuk menampilkan citra img_transition dengan menggunakan fungsi imshow dari modul matplotlib.pyplot.
plt.title("Translation")#untuk menambahkan judul pada plot yang akan ditampilkan menggunakan modul matplotlib.pyplot
plt.show()#Menampilkan hasil citra