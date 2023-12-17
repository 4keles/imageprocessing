#description: https://dl.ebooksworld.ir/motoman/Digital.Image.Processing.3rd.Edition.www.EBooksWorld.ir.pdf  pdf page:138 book page:115
#formula reference: https://samirkhanal35.medium.com/contrast-stretching-f25e7c4e8e33
import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'images/ottocat.PNG'
#source code : https://stackoverflow.com/questions/42257173/contrast-stretching-in-python-opencv
def contrast_stretching():

    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    # normalize float versions
    norm_img1 = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    norm_img2 = cv2.normalize(img, None, alpha=0, beta=1.2, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    # scale to uint8
    norm_img1 = (255 * norm_img1).astype(np.uint8)
    norm_img2 = np.clip(norm_img2, 0, 1)
    norm_img2 = (255 * norm_img2).astype(np.uint8)

    plt.imshow(img)
    plt.title('Orjinal Görüntü')
    plt.show()

    plt.imshow(norm_img1)
    plt.title('Kontrast Gerilmiş Görüntü')
    plt.show()

    plt.imshow(norm_img2)
    plt.title('Kontrast Gerilmiş Görüntü 2')
    plt.show()

if __name__ == '__main__':

    contrast_stretching()
