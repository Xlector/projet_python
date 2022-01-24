import cv2 as cv
import mediapipe as m
from hand_analysing.hand import hand_track

def main():
  cap=cv.VideoCapture(0)
  while 1 :
   success,img=cap.read()




if __name__ == '__main__':
  main()