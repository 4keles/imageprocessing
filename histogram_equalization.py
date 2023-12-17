#description: https://dl.ebooksworld.ir/motoman/Digital.Image.Processing.3rd.Edition.www.EBooksWorld.ir.pdf  pdf sayfa:145 kitap sayfa:122
#reference code for histogram_equalization : https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'images/ottocat.PNG'
#reference code for histogram_equalization: https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
def histogram_equalization_gray():
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply histogram equalization
    equalized_img = cv2.equalizeHist(img)

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(equalized_img, cmap='gray')
    plt.title('Equalized Image')

    plt.show()

#reference code for histogram_equalization_colorful: https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
def histogram_equalization_colorful():
    img = cv2.imread(image_path)

    lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab_img)

    equ = cv2.equalizeHist(l)

    updated_lab_img = cv2.merge((equ, a, b))
    hist_eq_img = cv2.cvtColor(updated_lab_img, cv2.COLOR_LAB2BGR)

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(hist_eq_img, cv2.COLOR_BGR2RGB))
    plt.title('Histogram Equalized Image')
    plt.show()

if __name__ == '__main__':
    histogram_equalization_gray()
    histogram_equalization_colorful()


