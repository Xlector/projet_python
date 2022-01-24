import cv2 as cv
import mediapipe as m
import time
cap=cv.VideoCapture(0)
mesbras= m.solutions.hands
bras = mesbras.Hands(0,2)
drawer= m.solutions.drawing_utils
mface_detection= m.solutions.face_detection
face_detection =mface_detection.FaceDetection()
while 1 :
    success,img=cap.read()

    imageRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    face_resultat =face_detection.process(imageRGB)
    resultat =bras.process(imageRGB)
    if resultat.multi_hand_landmarks :
      for brasLMS in resultat.multi_hand_landmarks :
          drawer.draw_landmarks(img,brasLMS,mesbras.HAND_CONNECTIONS)
    if face_resultat.detections :
      for id,detection in enumerate(face_resultat.detections) :
          drawer.draw_detection(img,detection)




 
    cv.imshow("Image",img)
    cv.waitKey(1)