#description: https://dl.ebooksworld.ir/motoman/Digital.Image.Processing.3rd.Edition.www.EBooksWorld.ir.pdf  pdf sayfa:140 kitap sayfa:117
#main code: https://www.imageeprocessing.com/2012/11/bit-plane-slicing.html
#matlab kodlarının chatgpt ile pythondaki karşılığı bulundu
#code: https://dsp.stackexchange.com/questions/41635/bit-plane-slicing-in-python

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'images/ottocat.PNG'
def bit_plane_slice(bit):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    bit_plane = (img >> bit) & 1

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Source Image')

    plt.subplot(1, 2, 2)
    plt.imshow(bit_plane, cmap='gray')
    plt.title(f'Bit-Plane {bit}')

    plt.show()

if __name__ == '__main__':

    print("Bit-Plane Image: Choose the bit-plane (0 to 7) you want to visualize (To see al bit-planes, type:8)")
    bit_slice_number =input(">> ")

    if not bit_slice_number.isdigit():
        print("invalid input \nvisualize all bit-slice positions as default")
        bit_slice_number = 8
    bit_slice_number = int(bit_slice_number) % 9


    if bit_slice_number == 8:
        for i in range(8):
            bit_plane_slice(i)
            print("bit-plane position: ", i)
    else:
        bit_plane_slice(bit_slice_number)
        print("bit-plane position: ", bit_slice_number)

