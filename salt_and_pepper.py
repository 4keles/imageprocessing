#adding function source code : https://mackph.hashnode.dev/salt-and-pepper-in-python
#removing function refence solition : https://medium.com/analytics-vidhya/remove-salt-and-pepper-noise-with-median-filtering-b739614fe9db
#removing function source code : https://www.youtube.com/watch?v=yQUwmLx6NGk


import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "images/ottocat.PNG"
def add_salt_and_pepper_noise(salt_prob, pepper_prob):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    noisy_image = np.copy(image)
    row= image.shape[0]
    col= image.shape[1]

    salt_mask = np.random.rand(row, col) < salt_prob
    pepper_mask = np.random.rand(row, col) < pepper_prob

    noisy_image[salt_mask] = 255
    noisy_image[pepper_mask] = 0

    plt.subplot(1, 2, 2)
    plt.imshow(noisy_image, cmap='gray')
    plt.title('Noisy Image')

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.show()

    plt.show()

    return noisy_image

def remove_salt_and_pepper_noise(image, kernel_size):
    cleaned_image = cv2.medianBlur(image, kernel_size)

    plt.subplot(1, 2, 1)
    plt.imshow(cleaned_image, cmap='gray')
    plt.title('Cleaned Image (Median Filter)')
    plt.show()
    return cleaned_image

if __name__ == "__main__":

    salt_prob = 0.02  # Probability of adding salt noise
    pepper_prob = 0.02
    noisy_image = add_salt_and_pepper_noise(salt_prob, pepper_prob)
    kernel_size = 3
    cleaned_image = remove_salt_and_pepper_noise(noisy_image, kernel_size)

