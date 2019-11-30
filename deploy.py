from fastai.vision import*
import sys
import numpy as np
import cv2
import ipcam

# load model
learn = vision.load_learner('./models', 'export_new.pkl')

# load ảnh đầu vào trong thư mục image
img = open_image('./image/shot.jpg')
pred_class,pred_idx,outputs = learn.predict(img)

# return accuracy
accuracy = 0
for i in outputs:
    if tensor(i)>accuracy:
        accuracy = tensor(i)
accuracy = accuracy.numpy()*100

# ghi dự đoán lên ảnh
window_name = 'Image'
text = str(pred_class)+" "+str(round(accuracy, 2))+"%"
img = cv2.imread('./image/shot.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX 
org = (50, 50) 
fontScale = 1
color = (255, 0, 0) 
thickness = 2
img = cv2.putText(img, text, org, font, fontScale, color, thickness, cv2.LINE_AA) 

# hiển thị ảnh
cv2.imshow(window_name,cv2.resize(img,(512,384)))

# save image
cv2.imwrite("./image/result.jpg", img)

cv2.waitKey(0)