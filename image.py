import numpy as np
from PIL import Image
import os

# path = '/Users/User/project/banana/images/solar.jpg'

def image_to_bw(path_to_image):
    path_to_save = '/Users/User/project/banana/result_banana/'
    image_name = path_to_image.split('/')[-1]
    img = Image.open(path_to_image)
    arr = np.asarray(img, dtype='uint8')
    x, y, _ = arr.shape

    k = np.array([[[0.2989, 0.587, 0.114]]])
    arr2 = np.round(np.sum(arr*k, axis=2)).astype(np.uint8).reshape((x, y))
    
    img2 = Image.fromarray(arr2)
    img2.save(path_to_save+image_name)
    os.remove(path_to_image)
    return path_to_save+image_name