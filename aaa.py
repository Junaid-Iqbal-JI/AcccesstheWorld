import cv2
from pytesseract import pytesseract
import numpy as np

def get(image2):
    image = cv2.imread(image2)
    image = cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC) # rezize
    # preprocesing
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # grayscale
    image=cv2.medianBlur(image,5)
    image=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    kernel=np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)
    cv2.threshold(cv2.bilateralFilter(image, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    t = 'tesseract'
    pytesseract.tesseract_cmd=t
    custom_config = r'--oem 3 --psm 6'
    text=pytesseract.image_to_string(image,config=custom_config, lang='eng')
    test_str = ''.join(letter for letter in text if letter.isalnum())
    return test_str
