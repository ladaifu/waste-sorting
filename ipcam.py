import urllib.request
import cv2
import numpy as np

url='http://172.16.190.219:8080/shot.jpg'
# key = cv2. waitKey(1)
while True:
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)

    # all the opencv processing is done here
    cv2.imshow('test',cv2.resize(img,(600,400)))

    key = cv2.waitKey(1)
    if key == ord('s'): 
        cv2.imwrite(filename='saved.jpg', img=cv2.resize(img,(600,400)))
        cv2.destroyAllWindows()  
    elif key == ord('q'):
        cv2.destroyAllWindows()
        break