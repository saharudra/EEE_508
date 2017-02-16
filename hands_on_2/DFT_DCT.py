import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('zebras.jpg', 0)
plt.imshow(img)
imf = np.float32(img)/255.0
dft_img=np.fft.fft2(img)
fshift = np.fft.fftshift(imf)


# Code for taking DFT
for L in range(200,10,-10):
    dft_img = np.fft.fft2(img)
    for i in range(L,255-L+1):
        for j in range(L,255-L+1):
            dft_img[i][j]=0
    fshift = np.fft.fftshift(dft_img)
    f_ishift = np.fft.ifftshift(fshift)
    img_return = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_return)
    plt.imshow(img_return)
    plt.show()



# Code for DCT
for L in range(200,10,-10):
    dst = cv2.dct(imf)
    for i in range(L,256):
        for j in range(L,256):
            dst[i][j]=0
    img_return=cv2.idct(dst)
    plt.imshow(img_return)
    plt.show()

