import easyocr
import cv2

import numpy as np

IMAGE_PATH = './IMAGES/2.jpg'

reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(IMAGE_PATH)

print(result)