import os as os
import cv2 as cv
import numpy as np
from PIL import Image
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
IMG_DIR=os.path.join(BASE_DIR,"../src/tmp/images")
noms=[]
ids=[]
paths=[]

for users in os.listdir(IMG_DIR):
 noms.append(users)
for nom in noms:
    for image in os.listdir(IMG_DIR+"/{}".format(nom)):
        path_string=os.path.join("../src/tmp/images/{}".format(nom),image)
        paths.append(path_string)

print(paths)