import cv2 as cv
import mediapipe as m
class face_track():
  def __init__(self, minDetectionCon=0.5) :
    self.minDetectionCon=minDetectionCon
    self.mface_detection= m.solutions.face_detection
    self.face_detection =self.mface_detection.FaceDetection(self.minDetectionCon,0)
    self.drawer= m.solutions.drawing_utils

  
  def find_face(self,img,draw=True):
     imageRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
     face_resultat =self.face_detection.process(imageRGB)
     if face_resultat.detections :
       for id,detection in enumerate(face_resultat.detections) :
         if draw:
          self.drawer.draw_detection(img,detection)
     return img 