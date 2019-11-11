from fastai.vision import*
import sys
import numpy as np
import cv2
import ipcam

learn = vision.load_learner('.', 'export80.pkl')

img = open_image('saved.jpg')

# pred = learn.predict(img)
pred_class,pred_idx,outputs = learn.predict(img)
print(pred_class,pred_idx,outputs)