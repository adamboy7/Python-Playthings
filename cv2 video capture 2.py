import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#cameraVar = cv2.VideoCapture(#cameraNumber#)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#codecVar
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
#outVar = cv2.VideoWriter('fileName.avi')



while True:
#loop
	ret, frame = cap.read()
	#return frame from cameraVar
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#Optional filter, convert frameVar to gray
	
	cv2.imshow('frame', frame)
	#cv2.imshow('windowName', frameVar)
	
	cv2.imshow('gray', gray)
	#cv2.imshow('windowName', greyVar)
	
	out.write(frame)
	#Write frame to outVar
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
	#Wait for a specific key, Q
		break
		#Exit loop

cap.release()
#Release camera

out.release()
#Release written file

cv2.destroyAllWindows
#Close all Windows