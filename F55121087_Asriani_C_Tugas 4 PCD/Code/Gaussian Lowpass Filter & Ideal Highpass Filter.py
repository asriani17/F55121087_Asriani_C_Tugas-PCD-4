import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gambar asli/Gaussian Lowpass Filter & Ideal Highpass Filter.jpg', 0)

ksize = 11
sigma = 5
kernel = cv2.getGaussianKernel(ksize, sigma)
gaussian_kernel = np.outer(kernel, kernel.transpose())

gaussian = cv2.filter2D(img, -1, gaussian_kernel)

ksize = 21
cx = cy = ksize // 2
radius = 30
ideal_kernel = np.zeros((ksize, ksize), np.float32)
for i in range(ksize):
    for j in range(ksize):
        distance = np.sqrt((i-cx)**2 + (j-cy)**2)
        if distance <= radius:
            ideal_kernel[i, j] = 0
        else:
            ideal_kernel[i, j] = 1

ideal = cv2.filter2D(img, -1, ideal_kernel)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Gambar Asli'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(gaussian, cmap='gray')
plt.title('Hasil Gaussian Lowpass Filter'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(ideal, cmap='gray')
plt.title('Hasil Ideal Highpass Filter'), plt.xticks([]), plt.yticks([])

cv2.imwrite('hasil_gaussian_lowpass.png', gaussian)
cv2.imwrite('hasil_ideal_highpass.png', ideal)

plt.show()
