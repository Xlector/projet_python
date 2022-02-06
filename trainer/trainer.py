import os as os
import cv2 as cv
import numpy as np
from PIL import Image
class recognizer():
    def __init__(self): 
     self.face_cascade = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_frontalface_default.xml')
     self.BASE_DIR=os.path.dirname(os.path.abspath(__file__))
     self.IMG_DIR=os.path.join(self.BASE_DIR,"../src/tmp/images")
     self.noms=[]
     self.ids=[]
     self.paths=[]
     self.faces=[]

    def train(self):
     for users in os.listdir(self.IMG_DIR):
        self.noms.append(users)
     for nom in self.noms:
      for image in os.listdir(self.IMG_DIR+"/{}".format(nom)):
        path_string=os.path.join("src/tmp/images/{}".format(nom),image)
        self.paths.append(path_string)
     for img_path in self.paths :
      img = cv.imread(img_path)
      gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
      img_face = self.face_cascade.detectMultiScale(gray, 1.1, 4)
      for (x, y, w, h) in img_face:
        cv.rectangle(img, (x, y), (x+w, y+h),(0, 0, 255), 2)
        img_face = img[y:y + h, x:x + w]
        cv.imwrite(img_path.split(".")[0]+".png", img_face)
     for img_path in self.paths :
      image=Image.open(img_path).convert("L")
      ImgNp=np.array(image,"uint8")
      self.faces.append(ImgNp)
      id=int(img_path.split("/")[4].split("_")[0])
      self.ids.append(id)
    
     ids=np.array(self.ids)
     trainer=cv.face.LBPHFaceRecognizer_create()
     trainer.train(self.faces,ids)
     trainer.write("src/tmp/training.yml")



