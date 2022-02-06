import cv2 as cv
from hand_analysing.hand import hand_track
from reconissance_facial.face import  face_track
from trainer.trainer import recognizer
def main():
  cap=cv.VideoCapture(0)
  Trainer= recognizer()
  Trainer.train()
  hand_detector = hand_track()
  face_detector = face_track()
  while  True:
   success,img=cap.read()
   img= hand_detector.findshands(img)
   img= face_detector.find_face(img,1)
   #pour afficher les images    
   cv.imshow("Image",img)
   # pour quitter le program
   if cv.waitKey(20) & 0xFF == ord('q'):
     break

if __name__ == '__main__':
  main()