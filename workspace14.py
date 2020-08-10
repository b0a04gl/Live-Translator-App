import re
import cv2
import pytesseract
from googletrans import Translator
from tamil import utf8


img = cv2.imread('processed-img.png')
custom_config = r'-l eng --psm 6'
text = pytesseract.image_to_string(img,lang='eng+spa+tam+ben+guj+hin+kan+mal+mni+ori+pan+sat+tel')
#print(text)
lines=text.split('\n')
texts=[]
for line in lines:
	for i in line.split(' '):
		texts.append(i)
#print texts


translator = Translator()
trans_texts=[]
for t in texts:
	if(t.isnumeric()==False):
		trans_text = translator.translate(t, dest='ta').text
		trans_texts.append(trans_text)
		#letters = utf8.get_letters(trans_text)
		
		
 	else:
		trans_texts.append(t)
#for i in trans_texts:
#	print i,

