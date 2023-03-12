import cv2
import numpy as np

img = cv2.imread('Gambar asli/Median_min_max.jpg')

median = cv2.medianBlur(img, 5)

cv2.imshow('Gambar Asli', img)
cv2.imshow('Hasil Median Filter', median)

cv2.imwrite('hasil_median_filter.png', median)

cv2.waitKey(0)

cv2.destroyAllWindows()
