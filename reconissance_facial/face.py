from contextlib import nullcontext
import cv2 as cv
import mediapipe as m
import os 
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
IMG_DIR=os.path.join(BASE_DIR,"/src/tmp/images")
class face_track():
  def __init__(self, minDetectionCon=0.5) :
    self.minDetectionCon=minDetectionCon
    self.mface_detection= m.solutions.face_detection
    self.face_detection =self.mface_detection.FaceDetection(self.minDetectionCon,0)
    self.drawer= m.solutions.drawing_utils
  
 # def
    
  
  def find_face(self,img,draw=True,text=None,x=None,y=None):
     imageRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
     face_resultat =self.face_detection.process(imageRGB)
     if face_resultat.detections :
       for id,detection in enumerate(face_resultat.detections) :
         if draw:
          self.drawer.draw_detection(img,detection)
          cv.putText(img,text,(x,y),cv.FONT_HERSHEY_DUPLEX,3,(255,0,0),6)
     return img 
