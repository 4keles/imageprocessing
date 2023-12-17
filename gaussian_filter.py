# reference code : https://www.tutorialkart.com/opencv/python/opencv-python-gaussian-image-smoothing/#gsc.tab=0

import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'images/brain.PNG'
def gaussian_filter():
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    kernel_size = 5
    sigma = 3.0  # Standart sapma

    filtered_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Orijinal Görüntü')

    plt.subplot(1, 2, 2)
    plt.imshow(filtered_img, cmap='gray')
    plt.title(f'Gaussian Filtresi (Kernel Boyutu = {kernel_size}, Sigma = {sigma})')

    plt.show()

if __name__ == "__main__":
    gaussian_filter()
