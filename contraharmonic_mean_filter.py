# source code : https://python.hotexamples.com/examples/filter/-/contraharmonic_mean/python-contraharmonic_mean-function-examples.html
# github : https://github.com/joyeecheung/SE-343-Digital-Image-Processing/blob/master/hw4/src/filter.py
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


image_path = "images/ottocat.PNG"

def filter2d(input_img, filter):
    M, N = input_img.shape
    n, m = len(filter), len(filter[0])
    a, b = m // 2, n // 2

    if isinstance(filter, np.ndarray):
        wt = filter.ravel()
    else:
        wt = np.array(filter).ravel()

    def correlate(x, y):
        z = np.full(n * m, input_img[x, y])
        for i in range(x - a, x + a + 1):
            for j in range(y - b, y + b + 1):
                if 0 <= i < M and 0 <= j < N:
                    z[(i - x + a) * n + j - y + b] = input_img[i, j]
        return np.dot(wt, z)

    xx, yy = np.meshgrid(range(M), range(N), indexing='ij')
    vf = np.vectorize(correlate)
    return vf(xx, yy)

def contraharmonic_mean(img, size, Q):
    data = np.array(img, dtype=np.float64)
    epsilon = 1e-5  # Küçük bir epsilon değeri eklenerek sıfırdan farklı olması sağlanır
    numerator = np.power(data + epsilon, Q + 1)
    denominator = np.power(data + epsilon, Q)
    kernel = np.full(size, 1.0)
    result = filter2d(numerator, kernel) / filter2d(denominator, kernel)
    return Image.fromarray(result)
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

def contrast_mean_filter(noisy_image):

    q_neg, q_pos = 1.5, -1.5
    q_neg_name, q_pos_name = [str(q).replace('.', '-')
                              for q in (q_neg, q_pos)]

    # Q < 0
    result = contraharmonic_mean(noisy_image, (3, 3), q_neg)

    # Q > 0
    result1 = contraharmonic_mean(noisy_image, (3, 3), q_pos)

    plt.subplot(1, 2, 2)
    plt.imshow(noisy_image, cmap='gray')
    plt.title('Noisy Image')

    plt.subplot(1, 2, 1)
    plt.imshow(result1, cmap='gray')
    plt.title('after filter Image')
    plt.show()

if __name__ == '__main__':

    salt_prob = 0.02  # Probability of adding salt noise
    pepper_prob = 0.02
    noisy_image = add_salt_and_pepper_noise(salt_prob, pepper_prob)
    contrast_mean_filter(noisy_image)