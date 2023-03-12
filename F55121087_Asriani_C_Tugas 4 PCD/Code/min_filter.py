import cv2
import numpy as np

# membaca gambar
img = cv2.imread('Gambar asli/Median_min_max.jpg')

# menerapkan Min Filter dengan ukuran kernel 3x3
min_filter = cv2.erode(img, np.ones((3,3), np.uint8))

# menampilkan gambar asli dan hasil Min Filter
cv2.imshow('Gambar Asli', img)
cv2.imshow('Hasil Min Filter', min_filter)

# menyimpan hasil Min Filter ke dalam file baru
cv2.imwrite('hasil_min_filter.png', min_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()
