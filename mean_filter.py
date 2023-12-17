# reference code : https://medium.com/@sarves021999/noise-filtering-mean-median-mid-point-filter-72ab3be76da2
# reference code2: https://stackoverflow.com/questions/18427031/median-filter-with-python-and-opencv

import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'images/brain.PNG'
def mean_filter():
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    kernel_size = 3
    filtered_img = cv2.blur(img, (kernel_size, kernel_size))

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Orijinal Görüntü')

    plt.subplot(1, 2, 2)
    plt.imshow(filtered_img, cmap='gray')
    plt.title(f'Ortalama Filtresi (Kernel Boyutu = {kernel_size})')

    plt.show()

if __name__ == "__main__":

    mean_filter()
