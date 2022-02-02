import cv2 as cv
import mediapipe as m

class hand_track():
    def __init__(self,mode=False,maxbra=1,modelComplexity=1,detectioncon=0.5,trackcon=0.5):
        self.modelComplexity=modelComplexity
        self.mode=mode
        self.trackcon=trackcon
        self.maxbra=maxbra
        self.detectioncon=detectioncon
        self.mesbras= m.solutions.hands
        self.bras = self.mesbras.Hands(self.mode,self.maxbra, self.modelComplexity,self.detectioncon,self.trackcon)
        self.drawer= m.solutions.drawing_utils

    def findshands(self,img,draw=True):
     imageRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
     resultat =self.bras.process(imageRGB)
     if resultat.multi_hand_landmarks :
         for brasLMS in resultat.multi_hand_landmarks :
            if draw :
             self.drawer.draw_landmarks(img,brasLMS,self.mesbras.HAND_CONNECTIONS)
     return img