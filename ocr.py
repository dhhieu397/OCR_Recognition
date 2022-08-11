import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np 

#Read an image/ video
IMAGE_PATH ='out_of_service.jpg'
reader = easyocr.Reader(['en'], gpu=False)
result =reader.readtext(IMAGE_PATH)
# print(result)
# print(result[0])

#handing multiple lines:
img =cv2.imread(IMAGE_PATH)
for detection in result:
    top_left = tuple([int(val) for val in detection[0][0]])
    bottom_right = tuple([int(val) for val in detection[0][2]])
    text = detection[1]
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
    img = cv2.putText(img, text, top_left, font, 2, (255, 255, 255), 2,  cv2.LINE_AA)

plt.figure(figsize=(10, 10))
plt.imshow(img)
plt.show()
#Draw result:
# top_left = tuple(result[0][0][0])
# bottom_right = tuple(result[0][0][2])
# text = result[0][1]
# font = cv2.FONT_HERSHEY_SIMPLEX

# img = cv2.imread(IMAGE_PATH)
# img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
# # img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 255), 5)
# img = cv2.putText(img, text, top_left, font, .5, (255, 255, 255), 2,  cv2.LINE_AA)

# plt.imshow(img)
# plt.show()
