from PIL import Image
from pytesseract import image_to_string
import matplotlib.pyplot as plt
import pytesseract

im=Image.open('hangul.png')

plt.imshow(im)

char=pytesseract.image_to_string(im,lang='kor',config='--psm 7 --oem 0')