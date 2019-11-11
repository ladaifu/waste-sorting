import urllib.request
import cv2
import numpy as np

url='http://192.168.43.96:8080/shot.jpg'
while True:

    # sử dụng urllib để lấy hình ảnh từ IPwebcam
    imgResp = urllib.request.urlopen(url)

    # Chuyển đổi các giá trị nhận được từ url lưu thành mảng
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)

    # Giải mã mảng để  dùng cho OpenCV
    img = cv2.imdecode(imgNp,-1)
    img_rs = cv2.resize(img,(512,384))
    # Đưa ảnh lên màn hình với kích sthước 512x384
    cv2.imshow('IPWebcam',img_rs)

    key = cv2.waitKey(1)

    if key == ord('s'): 
        cv2.imwrite('./image/shot.jpg',img_rs)
        print("Image saved!")
        cv2.destroyAllWindows()
        break
    elif key == ord('q'):
        break