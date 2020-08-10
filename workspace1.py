from PIL import Image
import pytesseract
import argparse
import cv2
import os
from googletrans import Translator
text = pytesseract.image_to_string(Image.open('processed-img.png'),lang='eng')

print(text)



translator = Translator()

trans_text = translator.translate(text, dest='ta').text
print(trans_text)
