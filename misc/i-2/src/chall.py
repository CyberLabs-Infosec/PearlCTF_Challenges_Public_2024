import cv2
import numpy as np

im = cv2.imread("./original.png", cv2.IMREAD_COLOR)

im_fft = np.fft.fft(im)
real = im_fft.real.astype(np.uint16)
imag = im_fft.imag.astype(np.uint16)

cv2.imwrite('car1.png', real)
cv2.imwrite('car2.png', imag)
