import cv2
import pytesseract
from pytesseract import Output
from workspace14 import trans_texts
img = cv2.imread('processed-img.png')

h, w, c = img.shape

d = pytesseract.image_to_data(img, output_type=Output.DICT)

n_boxes = len(d['text'])
j=0
coords=[]
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
	if (x!=None and y!=None and w!=None and h!=None):
            coords.append(str(x)+"X"+str(x + w)+","+str(y)+"X"+str(y + h))
	

#cv2.imshow('img', img)
#cv2.waitKey(0)
cv2.imwrite("boxed.png",img)
#print (len(trans_texts))
#print(len(coords))

for c in coords:
	print trans_texts[j],
	j+=1	
	print "\t",c
	
