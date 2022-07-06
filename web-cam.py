import requests
import cv2
import numpy as np 
import imutils

url=""

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.constant), dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    img = imutils.resize(img,width=1000,height=1800)
    cv2.imshow("Android_cam",img)
    
    if cv2.waitKay(1)==27:
        break
cv2.destroyAllWindow()     