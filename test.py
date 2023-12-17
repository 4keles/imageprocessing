import sys

from normalization_standardizasyon import normalization, standardization
from bit_plane_slicing import bit_plane_slice
from histogram_equalization import histogram_equalization_gray,histogram_equalization_colorful
from contrast_stretching import contrast_stretching
from gamma_correction import gamma_correction
from mean_filter import mean_filter
from gaussian_filter import gaussian_filter
from sobel_filter import sobel_filter
from laplacian_blur import laplacian_blur_detection,color_average_blur
from smoothing_sharpening import apply_median_blur,sharpening
from gaussian_smoothing import apply_gaussian_blur
from salt_and_pepper import add_salt_and_pepper_noise,remove_salt_and_pepper_noise
from contraharmonic_mean_filter import contrast_mean_filter
from color_segmentation import color_segmentation
from opening_closing import opening_closing_demo
image_path = 'images/ottocat.PNG'

def test_all():

    print("Testing All Functions")
    input("Press any key to continue...")
    print("Normalization and Standardization")
    normalization()
    standardization()
    input("Press any key to pass next function ")
    print("Bit Plane Slicing")
    for i in range(8):
        bit_plane_slice(i)
        print("bit-plane position: ", i)
    input("Press any key to pass next function ")
    print("Histogram Equalization")
    histogram_equalization_gray()
    histogram_equalization_colorful()
    input("Press any key to pass next function ")
    print("Contrast Stretching")
    contrast_stretching()
    input("Press any key to pass next function ")
    print("Gamma Correction")
    gamma_correction(2.2)
    input("Press any key to pass next function ")
    print("Mean Filter")
    mean_filter()
    input("Press any key to pass next function ")
    print("Gaussian Filter")
    gaussian_filter()
    input("Press any key to pass next function ")
    print("Sobel Filter")
    sobel_filter()
    input("Press any key to pass next function ")
    print("Laplacian Filter Detection")
    kernel_size = 3
    test_img = color_average_blur(kernel_size)
    laplacian_blur_detection(test_img)
    input("Press any key to pass next function ")
    print("Smoothing And Sharping")
    kernel_size = 5
    apply_median_blur(image_path, kernel_size)
    apply_gaussian_blur(image_path, kernel_size,sigmaX=10)
    sharpening(image_path)
    input("Press any key to pass next function ")
    print("Gaussian Smoothing")
    kernel_size = 5
    sigmaX = 10 # blur effect
    apply_gaussian_blur(image_path, kernel_size, sigmaX)
    input("Press any key to pass next function ")
    print("Salt and Pepper filter")
    salt_prob = 0.02  # Probability of adding salt noise
    pepper_prob = 0.02
    noisy_image = add_salt_and_pepper_noise(salt_prob, pepper_prob)
    kernel_size = 3
    cleaned_image = remove_salt_and_pepper_noise(noisy_image, kernel_size)
    input("Press any key to pass next function ")
    print("Contraharmonic mean filter")
    salt_prob = 0.02  # Probability of adding salt noise
    pepper_prob = 0.02
    noisy_image = add_salt_and_pepper_noise(salt_prob, pepper_prob)
    contrast_mean_filter(noisy_image)
    input("Press any key to pass next function ")
    print("Color Segmentation")
    color_segmentation()
    input("Press any key to pass next function ")
    print("Opening and Closing (morphology)")
    operation_type = 'opening'
    kernel_size = 5
    opening_closing_demo(image_path, operation_type, kernel_size)
    input("Tüm Fonksiyonlar Çalıştırıldı ")
    sys.exit()










