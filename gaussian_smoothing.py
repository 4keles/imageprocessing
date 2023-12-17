#reference source code https://www.geeksforgeeks.org/apply-a-gauss-filter-to-an-image-with-python/
import cv2
import numpy as np
import matplotlib.pyplot as plt


def apply_gaussian_blur(image_path, kernel_size, sigmaX):

    img = cv2.imread(image_path)

    # Apply Gaussian blur
    blurred_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), sigmaX)

    # Display the original and blurred images
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(blurred_img, cv2.COLOR_BGR2RGB))
    plt.title(f'Gaussian Blurred Image (Kernel Size = {kernel_size})')

    plt.show()

if __name__ == "__main__":
    img_path = "images/ottocat.PNG"
    kernel_size = 5
    sigmaX = 10 # blur effect
    apply_gaussian_blur(img_path, kernel_size, sigmaX)