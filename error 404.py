import cv2
import numpy as np
cv2.Cascadeclassifier('haar_cascade_files/haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haar_cascade_files/haarcascade_eye.xml')

if case_cascade.empty():
    print(" unable to load the face cascade classifier xml file ")
if eye_cascade.empty():
    print("unable to load the eye cascade classifier xml file ")
cap=cv2.videocapture(0)
ds_factor = 0.5
while true :
    frame = cap.read()
    frame = cv2.resize (frame,None,fx=ds_factor, fy=ds_factor,interpolation=cv2.INTER_AREA)
    gray = cv2.cvtcolor (frame , cv2.colour_BGR2GRAY)
    faces = face_cascade.detectMultiscale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, X:X+w]
roi_colour = frame[y:y+h,x:x+w]
eyes = eye_cascade.detectmultiscale(roi_gray)
for (x_eye,y_eye,w_eye,h_eye) in eyes:
    centre = (int(x_eye = 0.5*w_eye))
    color = (0,255,0)
    thickness = 3
    cv2.circle(roi_color,centre,radius,colour,thickness)
cv2.imshow('eye detector', frame)
c = cv2.waitkey(1)


#if c == 27:
   # break

cap.release()
cv2.destroyAllWindows()
           
