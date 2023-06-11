import mahotas as mh#Import library mahotas
import numpy as np#untuk mengimpor numpy dan memberikan as np ke modul tersebut.
from pylab import imshow, show#mengimpor fungsi imshow dan show dari modul pylab.
regions = np.zeros((8,8), bool)#membuat matriks regions berukuran 8x8 yang diisi dengan nilai boolean False (0).
regions[:3, :3] = 1#mengatur nilai elemen-elemen matriks regions pada baris 0 hingga 2 (indeks 0, 1, 2) dan kolom 0 hingga 2 (indeks 0, 1, 2) menjadi 1 (True).
regions[6:, 6:] = 1#mengatur nilai elemen-elemen matriks regions pada baris 0 hingga 2 (indeks 0, 1, 2) dan kolom 0 hingga 2 (indeks 0, 1, 2) menjadi 1 (True).
labeled, nr_objects = mh.label(regions)#pemrosesan label pada matriks regions menggunakan modul mahotas
imshow(labeled, interpolation='nearest')#untuk menampilkan matriks labeled sebagai citra dengan menggunakan fungsi imshow dari modul pylab
show()#Menampilkan citra
labeled,nr_objects = mh.label(regions,np.ones((3,3), bool))#melakukan pemrosesan label pada matriks regions menggunakan modul mahotas
sizes = mh.labeled.labeled_size(labeled)#untuk menghitung ukuran (luas) dari setiap objek yang telah diberi label dalam matriks labeled menggunakan modul mahotas (diasumsikan sebagai mh.labeled).
print('Background size', sizes[0])#untuk mencetak ukuran (luas) latar belakang (background) dalam matriks sizes.
print('Size of first region:{}'.format(sizes[1]))# untuk mencetak ukuran (luas) dari wilayah pertama dalam matriks sizes.

array = np.random.random_sample(regions.shape)#membuat matriks array dengan ukuran yang sama seperti matriks regions dan mengisi elemen-elemennya dengan bilangan acak antara 0 dan 1.
sums = mh.labeled_sum(array, labeled)#ntuk menghitung jumlah (total) dari nilai-nilai dalam matriks array yang terkait dengan setiap objek yang telah diberi label dalam matriks labeled menggunakan modul mahotas
print('Sum of first region:{}'.format(sums[1]))#untuk mencetak nilai dari variabel sums[1] dalam format string.