import numpy as np
import cv2

img = cv2.imread('image.png', cv2.IMREAD_COLOR)
#cv2 color modes
#IMREAD_UNCHANGED : -1
#IMREAD_GRAYSCALE : 0
#IMREAD_COLOR : 1

cv2.line(img, (0,0), (150,150), (255,255,255), 15)
#cv2.line(imgVar, (X1,Y1), (X2,Y2), (B,G,R), lineWidth)
cv2.rectangle(img, (15,25), (200,150), (0,255,0), 5)
#cv2.rectangle(imgVar, (X1,Y1), (X2,Y2), (B,G,R), lineWidth)
cv2.circle(img, (100,63), 55, (0,0,255), -1)
#cv2.circle(imgVar, (cntrX,cntrY), radius, (B,G,R), linewidth)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#arrayVar = np.array([X1,Y1],[X2,Y2]..., np.int32)

##pts = pts.reshape ((-1,1,2)
#reshape array tp 1x2, already to shape?

cv2.polylines(img, [pts], True, (0,255,255), 3)
#cv2.polylines(imgVar, [arrayVar], connectLast, (B,G,R), lineWidth)

font = cv2.FONT_HERSHEY_SIMPLEX
#fontVar = cv2.Your_Font_Here

cv2.putText(img, 'OpenCV Tuts!', (0,130), font, 1, (200,255,255), 2, cv2.LINE_AA)
#cv2.putText(imgvar, 'Your Text', (X,Y), fontVar, (B,G,R), lineWidth, cv2.antiAlias)

cv2.imshow('image', img)
#cv2.imshow('windowName', imgVar)
cv2.waitKey(0)
#Wait for any key

cv2.imwrite('TwitchDraw.png', img)
#cv2.imwrite('fileName', imgVar)

cv2.destroyAllWindows
#Closes all associated windows