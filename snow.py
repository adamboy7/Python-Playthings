import cv2
import numpy as np
import random

img = cv2.imread('image.png', cv2.IMREAD_COLOR)

height, width, channels = img.shape

while True:
	randB = (random.randint(0,255))
	randG = (random.randint(0,255))
	randR = (random.randint(0,255))
	randX = (random.randint(0,width-1))
	randY = (random.randint(0,height-1)) 
	
	img[randX,randY] = [randB,randG,randR]
	
	cv2.imshow('Snow', img)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.imwrite('Snow.png', img)
print ("B =", randB)
print ("G =", randG)
print ("R =", randR)
print ("X =", randX)
print ("Y =", randY)
cv2.destroyAllWindows