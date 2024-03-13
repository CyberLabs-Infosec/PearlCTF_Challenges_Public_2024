import cv2
import numpy as np

real = cv2.imread("../publish/car1.png", cv2.IMREAD_UNCHANGED).astype(np.int16)
imag = cv2.imread("../publish/car2.png", cv2.IMREAD_UNCHANGED).astype(np.int16)

# to account for negatives
real = np.where(real > (1<<15), real - 65536, real)
imag = np.where(imag > (1<<15), imag - 65536, imag)

im_fft = real + imag * 1j
im = np.fft.ifft(im_fft).real
cv2.imwrite('car_original.png', im)
