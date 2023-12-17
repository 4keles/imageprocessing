#code reference : https://datahacker.rs/004-how-to-smooth-and-sharpen-an-image-in-opencv/
#filters reference : http://fy.chalmers.se/~romeo/RRY025/notes/lec3.pdf
import cv2
import numpy as np
import matplotlib.pyplot as plt

def sharpening(image_path): #-1,9,-1
    # Load the image
    img = cv2.imread(image_path,1)

    # Apply Laplacian sharpening
    filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened_img = cv2.filter2D(img, -1, filter)
    # Display the original and sharpened images
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(img.astype('uint8'))
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(sharpened_img.astype('uint8'))
    plt.title('Laplacian Sharpened Image')

    plt.show()

def apply_median_blur(image_path, kernel_size):
    # Load the image
    img = cv2.imread(image_path)

    # Apply median blur
    blurred_img = cv2.medianBlur(img, kernel_size)

    # Display the original and blurred images
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(blurred_img, cv2.COLOR_BGR2RGB))
    plt.title(f'Median Blurred Image (Kernel Size = {kernel_size})')

    plt.show()


def apply_gaussian_blur(image_path, kernel_size):
    # Load the image
    img = cv2.imread(image_path)

    # Apply Gaussian blur
    blurred_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

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
    apply_median_blur(img_path, kernel_size)
    apply_gaussian_blur(img_path, kernel_size)
    sharpening(img_path)