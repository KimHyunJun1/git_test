'''try:
    import Image
except ImportError:
    from PIL import Image'''

import PIL.Image
import pytesseract


# 영어 인식
#print(pytesseract.image_to_string(Image.open('english.png')))

# 한글 



print(pytesseract.image_to_string(Image.open('Image/hangul.png'), lang='Hangul'))
