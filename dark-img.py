import numpy as np from imageio 
import imread,imwrite
import cv2
img = imread('a.jpg')
arr = img*np.array([0.1,0.2,0.5])
arr2 = (255*arr/arr.max()).astype(np.unit8)
imgwrite('night.png',arr2)
img2 = cv2.imread('night.png')
gamma = 2
gamma_img = np.array(255*(img2/255)**gamma,dtype = uint8)
cv2.iwrite('night_final.png',gamma_img)
print("Coversion Done!")