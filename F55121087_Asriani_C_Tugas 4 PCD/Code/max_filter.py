import cv2
import numpy as np

img = cv2.imread('Gambar asli/Median_min_max.jpg')

max_filter = cv2.dilate(img, np.ones((3,3), np.uint8))

cv2.imshow('Gambar Asli', img)
cv2.imshow('Hasil Max Filter', max_filter)

cv2.imwrite('hasil_Max_filter.png', max_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()
