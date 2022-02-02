import os as os 
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
IMG_DIR=os.path.join(BASE_DIR,"../src/tmp/images")
noms=[]
ids=[]
paths=[]

for root,dirs,files in os.walk(IMG_DIR):
 noms.append(dirs)
 for file in files:
     if file.endswith('.jpg') or file.endswith('.png'):
         print(os.path.join(root,file)[63::].replace("/"," ").replace("-"," ",1))

print(noms)