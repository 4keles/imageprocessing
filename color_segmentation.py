# source code : https://medium.com/@flippygarcia/color-image-segmentation-using-python-part-1-11319b4dccad
# additional resource : https://www.youtube.com/watch?v=4hPl7GMnz5I
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.io import imread, imshow
from skimage.color import rgb2gray, rgb2hsv
from skimage.filters import threshold_otsu

image_path = "images/ottocat.PNG"

def color_segmentation():
    img = imread(image_path)[:, :, :3]
    img_gs_1c = rgb2gray(img)

    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.set_title("Original Image")
    ax.imshow(img)
    ax.set_axis_off()
    plt.show()

    # Grayscale image with 3 channels (the value is triplicated)
    img_gs = ((np.stack([img_gs_1c] * 3, axis=-1) * 255)
              .astype('int').clip(0, 255))

    # Red mask
    red_mask = ((img[:, :, 0] > 150) &
                (img[:, :, 1] < 100) &
                (img[:, :, 2] < 200))
    img_red = img_gs.copy()
    img_red[red_mask] = img[red_mask]

    # Green mask
    green_mask = ((img[:, :, 0] < 190) &
                  (img[:, :, 1] > 190) &
                  (img[:, :, 2] < 190))
    img_green = img_gs.copy()
    img_green[green_mask] = img[green_mask]

    # Blue mask
    blue_mask = ((img[:, :, 0] < 80) &
                 (img[:, :, 1] < 85) &
                 (img[:, :, 2] > 50))
    img_blue = img_gs.copy()
    img_blue[blue_mask] = img[blue_mask]

    # Plot
    fig, ax = plt.subplots(1, 3, figsize=(21, 7))
    ax[0].set_title("Red Segment")
    ax[0].imshow(img_red)
    ax[0].set_axis_off()
    ax[1].set_title("Green Segment")
    ax[1].imshow(img_green)
    ax[1].set_axis_off()
    ax[2].set_title("Blue Segment")
    ax[2].imshow(img_blue)
    ax[2].set_axis_off()
    plt.show()

    img_hsv = rgb2hsv(img)

    # Plot
    fig, ax = plt.subplots(1, 3, figsize=(21, 7))
    ax[0].set_title("Hue Channel")
    ax[0].imshow(img_hsv[:, :, 0], cmap='gray')
    ax[0].set_axis_off()
    ax[1].set_title("Saturation Channel")
    ax[1].imshow(img_hsv[:, :, 1], cmap='gray')
    ax[1].set_axis_off()
    ax[2].set_title("Value Channel")
    ax[2].imshow(img_hsv[:, :, 2], cmap='gray')
    ax[2].set_axis_off()
    plt.show()

    # Plot Hue Channel with Colorbar
    plt.imshow(img_hsv[:, :, 0], cmap='hsv')
    plt.title('Hue Channel with Colorbar')
    plt.colorbar()
    plt.show()

    # Saturation mask
    sat_mask = img_hsv[:, :, 1] > 0.35
    img_hsv_mask = img_gs.copy()
    img_hsv_mask[sat_mask] = img[sat_mask]

    # Green mask (in Hue Channel)
    lower_mask = img_hsv[:, :, 0] > 0.25
    upper_mask = img_hsv[:, :, 0] < 0.59
    green_mask = lower_mask * upper_mask
    img_hsv_mask[green_mask] = img[green_mask]

    # Plot
    fig, ax = plt.subplots(1, 2, figsize=(15, 15))
    ax[0].set_title("Original Image")
    ax[0].imshow(img)
    ax[0].set_axis_off()
    ax[1].set_title("Image Segmented on Outfit")
    ax[1].imshow(img_hsv_mask)
    ax[1].set_axis_off()
    plt.show()

if __name__ == "__main__":
    color_segmentation()
