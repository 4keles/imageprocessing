# main source : https://stackoverflow.com/questions/51869513/cv2-morph-close-joining-letters-together
import cv2
import numpy as np
import matplotlib.pyplot as plt

def opening_closing_demo(image_path, operation_type, kernel_size):

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    if operation_type == 'opening':
        result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    elif operation_type == 'closing':
        result = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    else:
        print("Invalid operation type. Please use 'opening' or 'closing'.")
        return

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(result, cmap='gray')
    plt.title(f'{operation_type.capitalize()} Result (Kernel Size: {kernel_size})')

    plt.show()

if __name__ == "__main__":
    image_path = 'images/ottocat.PNG'

    operation_type = 'opening'
    kernel_size = 5

    opening_closing_demo(image_path, operation_type, kernel_size)
