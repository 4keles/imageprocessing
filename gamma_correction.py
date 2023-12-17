#source formula : https://lindevs.com/apply-gamma-correction-to-an-image-using-opencv

import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'images/ottocat.PNG'

def gamma_correction(gamma):
    img = cv2.imread(image_path)

    invGamma = 1 / gamma
    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)
    gammaImg = cv2.LUT(img, table)
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Original image')

    plt.subplot(1,2, 2)
    plt.imshow(gammaImg)
    plt.title('Gamma corrected image')
    plt.show()

if __name__ == '__main__':
    gamma_correction(2.2)

