import cv2 as cv
import mediapipe as m

class hand_track():
    def __init__(self,mode=False,maxbra=2,detectioncon=0.5,trackcon=0.5):
        self.mode=mode
        self.trackcon=trackcon
        self.maxbra=maxbra
        self.detectioncon=detectioncon
        self.mesbras= m.solutions.hands
        self.bras = self.mesbras.Hands(self.mode,self.maxbra,self.detectioncon,self.trackcon)
        self.drawer= m.solutions.drawing_utils
       

    def findshands(self,img,draw=True):
     imageRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
     resultat =self.bras.process(imageRGB)
     if resultat.multi_hand_landmarks :
         for brasLMS in resultat.multi_hand_landmarks :
            if draw==True :
             self.drawer.draw_landmarks(img,brasLMS,self.mesbras.HAND_CONNECTIONS)
         
while True :
    success,img=cap.read()

   
    if face_resultat.detections :
      for id,detection in enumerate(face_resultat.detections) :
          drawer.draw_detection(img,detection)




 
    cv.imshow("Image",img)
    cv.waitKey(1)

  