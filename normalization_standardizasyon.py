import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.preprocessing import StandardScaler

image_path = "images/ottocat.PNG"
def normalization():
    image = Image.open(image_path)
    image_np = np.array(image)

    plt.imshow(image_np)
    plt.title('Original Image')
    plt.show()

    min_value = np.min(image_np)
    max_value = np.max(image_np)
    normalized_image = (image_np - min_value) / (max_value - min_value)


    plt.imshow(normalized_image)
    plt.title('Normalized Image')
    plt.show()
    print("Normalized Image")

def standardization():
    image_path = "images/ottocat.PNG"
    image = cv2.imread(image_path)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    flatten_image = image_rgb.reshape(-1, 3)
    standard_scaler = StandardScaler() #https://www.digitalocean.com/community/tutorials/standardscaler-function-in-python
    standardized_image = standard_scaler.fit_transform(flatten_image).reshape(image_rgb.shape) #https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html

    plt.imshow(standardized_image.astype('uint8'))
    plt.title('Standardized Image')
    plt.show()
    print("Standardized Image")

if __name__ == '__main__':
    print("Normalization and Standardization")
    normalization()
    standardization()
