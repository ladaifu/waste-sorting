from fastai.vision import*
import sys
import numpy as np
import cv2
import ipcam

learn = vision.load_learner('.', 'export80.pkl')
img = open_image('saved.jpg')
pred_class,pred_idx,outputs = learn.predict(img)

window_name = 'Image'
text = str(pred_class)
img = cv2.imread('saved.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX 
org = (50, 50) 
fontScale = 1
color = (255, 0, 0) 
thickness = 2

# Using cv2.putText() method 
img = cv2.putText(img, text, org, font, fontScale, color, thickness, cv2.LINE_AA) 

# Displaying the image 
cv2.imshow(window_name,cv2.resize(img,(800,600)))

cv2.waitKey(0)