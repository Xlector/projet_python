import cv2 as cv
import mediapipe as m
from hand_analysing.hand import hand_track
from reconissance_facial.face import  face_track
def main():
  cap=cv.VideoCapture(0)
  hand_detector = hand_track()
  face_detector = face_track()
  while  True:
   success,img=cap.read()
   img= hand_detector.findshands(img)
   img= face_detector.find_face(img)
   #pour afficher les images    
   cv.imshow("Image",img)
   # pour quitter le program
   if cv.waitKey(20) & 0xFF == ord('q'):
     break

if __name__ == '__main__':
  main()