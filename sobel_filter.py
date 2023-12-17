# cpp reference code : https://github.com/callyberz/Sobel-Filter/blob/master/opencvpjt_img/main.cpp
# python reference code : https://www.adeveloperdiary.com/data-science/computer-vision/how-to-implement-sobel-edge-detection-using-python-from-scratch/
# python reference code2: https://wisdomml.in/implementing-sobel-filter-edge-detection-in-python-using-opencv/


import cv2
import numpy as np
import matplotlib.pyplot as plt
img_path = "images/ottocat.PNG"

def sobel_filter():
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Error: Could not read the image from the path: {img_path}")
    else:
        filtered_img = np.zeros_like(img)
        sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

        for j in range(img.shape[0] - 2):
            for i in range(img.shape[1] - 2):
                pixval_x = np.sum(sobel_x * img[j:j + 3, i:i + 3])
                pixval_y = np.sum(sobel_y * filtered_img[j:j + 3, i:i + 3])

                sum_val = abs(pixval_x) + abs(pixval_y)
                sum_val = min(sum_val, 255)

                filtered_img[j, i] = sum_val

        plt.subplot(1, 2, 1)
        plt.imshow(img, cmap='gray')
        plt.title('Original image')

        plt.subplot(1, 2, 2)
        plt.imshow(filtered_img, cmap='gray')
        plt.title('Sobel filtered')

        plt.show()

#def sobel_filter_2():

if __name__ == "__main__":
    print("Starting Sobel Filter")
    sobel_filter()
