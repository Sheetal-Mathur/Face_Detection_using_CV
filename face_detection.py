import cv2
import os
from random import randrange
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#to read the image
"img=cv2.imread('ccb55d43-5101-4d60-ab53-17dc9a2c71a7.jpg ')"

#for real time detection from webcam
webcam=cv2.VideoCapture(0)

while True:
    successful_frame_read,frame = webcam.read()

    #to read the video frame


   #cinvert img color to gray
    grayscaledimg=cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)


   #for rectangle coodinates
    face_coordinates=trained_face_data.detectMultiScale(grayscaledimg,1.1,4)


   #print(face_coordinates)
    for(x,y,w,h) in face_coordinates:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(255),randrange(256),randrange(256)),2)  # coordinates number , color,




# To show the image
    cv2.imshow("mine",frame)
    cv2.waitKey(1)


print("code")