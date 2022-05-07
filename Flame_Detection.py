import cv2
import numpy as np
cap=cv2.VideoCapture(0)
  
while (True) :
    ret, frame = cap.read()
    
    #in order to capture frame continuously
    ret, frame = cap.read ()   #if frame available then ret(T, F) and and frame stored in frame variable
    if(ret == True):
        gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        retval, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
        contours,im = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.imshow('threshold',threshold)
        for contour in contours:
            if len(contours) > 0:
                areas = [cv2.contourArea(c) for c in contours]
                max_index = np.argmax(areas)
                cnt = contours[max_index]
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()

