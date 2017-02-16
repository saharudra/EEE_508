import numpy as np
import scipy as sp
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import scipy.ndimage
from scipy import signal

# Some heavy duty lifting over here
image = mpimg.imread('cameraman.jpg')
h = np.array([[1.0/9, 1.0/9, 1.0/9], [1.0/9, 1.0/9, 1.0/9], [1.0/9, 1.0/9, 1.0/9]])   # impulse response matrix
h2 = np.multiply(-9, np.array([[1.0 / 9, 1.0 / 9, 1.0 / 9], [1.0 / 9, -8.0 / 9, 1.0 / 9], [1.0 / 9, 1.0 / 9, 1.0 / 9]]))
h1_row = np.array([1.0/9, 1.0/9, 1.0/9])
h1_col = np.array([[1.0], [1.0], [1.0]])

# Convolution procedure begins
tempy3 = sp.signal.convolve(h1_row, image[0, :])
for i in range(1, np.shape(image)[0]):
    z2 = sp.signal.convolve(h1_row, image[i, :])
    tempy3 = np.vstack((tempy3, z2))
y3 = sp.signal.convolve(h1_col, tempy3)
for i in range(1, np.shape(image)[0]):
    pass
y1 = signal.convolve2d(h, image)    # generation of y1 with convolve2D
y2 = sp.ndimage.filters.convolve(h, image)  # ndimage convolve
type1 = type(y1)
print("y1 is a : " + str(type1))
print(y1)
type2 = type(y2)
print("y2 is a : " + str(type2))
print(y2)
#y3 = sp.signal.convolve(h, image)
img_size = image.size
mean2 = np.sum(image) / img_size
y4 = np.add(signal.convolve2d(h2, image), mean2)
new_img_size = y4.size
new_mean = np.sum(y4) / new_img_size
print(mean2, new_mean)

# Plotting images as part of the subplot.
plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')   # Showing the original image
plt.title("Original Image")
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 2)
plt.imshow(y1, cmap='gray')
plt.title("y1")
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 3)
plt.imshow(y2, cmap='gray')
plt.title("y2")
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 4)
plt.imshow(tempy3, cmap='gray')
plt.title('y3')
plt.xticks([]), plt.yticks([])
plt.imshow(y4, cmap='gray')
plt.title('y4')
plt.xticks([]), plt.yticks([])
plt.show()


