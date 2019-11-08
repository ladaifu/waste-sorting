from fastai.vision import*
import sys
import numpy as np
import cv2

#vision.defaults.device = vision.torch.device('gpu')

# path = vision.Path('exoprt80.pkl')
# learn = vision.load_learner(path)
learn = vision.load_learner('.', 'export80.pkl')

imgpath = sys.argv[1]

img = open_image(imgpath)

# pred = learn.predict(img)
pred_class,pred_idx,outputs = learn.predict(img)
print(pred_class,pred_idx,outputs)