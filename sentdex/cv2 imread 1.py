import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
#cv2 color modes
#IMREAD_UNCHANGED : -1
#IMREAD_GRAYSCALE : 0
#IMREAD_COLOR : 1
 
cv2.imshow('image', img)
#cv2.imshow('windowName', imgVar)
 
cv2.waitKey(0)
#Wait for any key
cv2.destroyAllWindows
#Closes all associated windows

##imshow alternative in matplotlib
#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.imshow(imgVar, cmap='colorMap', interpolation='interpolationSetting')
#plt.show()

cv2.imwrite('TwitchGrey.png', img)
#cv2.imwrite('fileName', imgVar)