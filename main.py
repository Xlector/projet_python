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
   cv.imshow("Image",img)
   cv.waitKey(1)

if __name__ == '__main__':
  main()