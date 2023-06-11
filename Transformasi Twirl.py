#Import Liblary
import matplotlib.pyplot as plt#untuk mengimpor modul matplotlib.pyplot dan memberikan alias plt ke modul tersebut.
import cv2#untuk mengimpor modul cv2 .
import numpy as np#untuk mengimpor numpy dan memberikan as np ke modul tersebut.

#membuat efek swirled dengan bantuan numpy
def swirled_effect(image, strength, radius):#image adalah citra input yang akan diberikan efek swirled,strength adalah parameter yang mengontrol kekuatan efek swirled,radius adalah parameter yang menentukan jarak maksimum dari pusat citra yang akan terpengaruh oleh efek swirled.
    rows, cols = image.shape[:2]# untuk mengambil dimensi baris dan kolom dari citra image menggunakan metode shape pada objek citra.
    center_x, center_y = rows / 2, cols / 2#untuk menginisialisasi variabel center_x dan center_y dengan nilai setengah dari rows dan cols secara masing-masing.
    map_x = np.zeros((rows, cols), dtype=np.float32)#untuk membuat matriks map_x yang berukuran rows x cols dengan tipe data np.float32 (floating point).
    map_y = np.zeros((rows, cols), dtype=np.float32)#untuk membuat matriks map_y yang berukuran rows x cols dengan tipe data np.float32 (floating point).

    for i in range(rows):#sebuah perulangan yang berjalan sebanyak rows kali, di mana rows adalah jumlah baris pada citra.
        for j in range(cols):#ebuah perulangan yang berjalan sebanyak cols kali, di mana cols adalah jumlah kolom pada citra.
            x = j - center_x#berarti bahwa variabel x akan diisi dengan nilai selisih antara j (indeks baris) dengan center_x (koordinat x pusat citra).
            y = i - center_y#berarti bahwa variabel y akan diisi dengan nilai selisih antara i (indeks baris) dengan center_y (koordinat y pusat citra).
            theta = np.arctan2(y, x)#untuk menghitung nilai theta yang merupakan arctan (arctangent) dari rasio y dibagi x.
            distance = np.sqrt(x * x + y * y)# menghitung nilai distance yang merupakan jarak piksel terhadap pusat citra.
            if distance < radius:#merupakan sebuah kondisi yang memeriksa apakah distance (jarak piksel terhadap pusat citra) lebih kecil dari radius (jarak maksimum yang ditentukan).
                r = distance / radius#menghitung nilai rasio r yang merupakan perbandingan antara jarak piksel terhadap pusat citra dengan radius yang ditentukan.
                angle = strength * (1 - r)#menghitung nilai sudut angle berdasarkan strength dan r dalam proses transformasi swirled.
                map_x[i, j] = int(x * np.cos(angle) + y * np.sin(angle) + center_x)#berarti bahwa pada matriks map_x, nilai pada baris i dan kolom j akan diisi dengan hasil dari perhitungan
                map_y[i, j] = int(-x * np.sin(angle) + y * np.cos(angle) + center_y)#berarti bahwa pada matriks map_y, nilai pada baris i dan kolom j akan diisi dengan hasil dari perhitungan
            else:
                map_x[i, j] = j#i bahwa pada matriks map_x, nilai pada baris i dan kolom j akan diisi dengan nilai j.
                map_y[i, j] = i#i bahwa pada matriks map_y, nilai pada baris i dan kolom j akan diisi dengan nilai i.

    output = cv2.remap(image, map_x, map_y, interpolation=cv2.INTER_LINEAR)#untuk melakukan transformasi mapping piksel pada citra image menggunakan matriks map_x dan map_y sebagai koordinat baru.
    return output

img = cv2.imread('flower.jpg')#Membaca Gambar

output_img = swirled_effect(img, strength=10, radius=120)#mengaplikasikan efek swirled
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3), sharex=True, sharey=True)#untuk membuat subplot (grafik-gambar yang terdiri dari beberapa subplot) dalam satu figure.
ax0.imshow(img, cmap=plt.cm.gray)#ntuk menampilkan gambar img pada subplot ax0 menggunakan fungsi imshow dari Matplotlib.
ax0.axis('off')# untuk menghilangkan tampilan sumbu (axis) pada subplot ax0.
ax1.imshow(output_img, cmap=plt.cm.gray)#untuk menampilkan gambar output_img pada subplot ax1 menggunakan fungsi imshow dari Matplotlib.
ax1.axis('off')# untuk menghilangkan tampilan sumbu (axis) pada subplot ax1.
plt.show()#menampilkan citra