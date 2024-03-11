#the needed extensions and libraries are easyocr/ matplotlib.pyplot/ opencv-python-headless
#this project is a simple approach to analyse an image containing text and displaying the text


import cv2
import easyocr
import matplotlib.pyplot as plt


# read image
img_path = "C:/Users/cccs/Downloads/test3.png" # image path
img = cv2.imread(img_path)
#cv2.imshow(img)

# instance text detector
reader = easyocr.Reader(['en'], gpu=True) #the reading language of the text

#detect text on image
imgtext = reader.readtext(img) #reading the text


#draw bbox and text
# going through the imgtext value, which is containing a 2 dimensional array which will contain
# the position of the bonding box surrounding the text, the text itself and the clarity or threshold of confidence
for i in imgtext:

    print(i)
    bbox, text, score = i[0], i[1], i[2]

    cv2.rectangle(img, bbox[0], bbox[2],(0,200,0), 4)

    cv2.putText(img, text, bbox[1], cv2.FONT_HERSHEY_COMPLEX, 1, (0,200,0), 4)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
