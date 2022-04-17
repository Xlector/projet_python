############################################# IMPORTING ################################################
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image,ImageTk
import pandas as pd
import datetime
import time
import mysql.connector


############################################# FUNCTIONS ################################################

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

##################################################################################

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200,tick)

###################################################################################

def contact():
    mess._show(title='Contactez-Nous', message="abazinehichame@gmail.com\nalilekhal5@gmail.com")

###################################################################################

def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Absence du fichier', message='contacter-Nous')
        window.destroy()


###################################################################################

def save_pass():
    assure_path_exists("Etiquette_d'image_de_simulation/")
    exists1 = os.path.isfile("Etiquette_d'image_de_simulation/psd.txt")
    if exists1:
        tf = open("Etiquette_d'image_de_simulation/psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Ancien mot de passe non trouvé', 'Veuillez entrer un nouveau mot de passe ci-dessous', show='*')
        if new_pas == None:
            mess._show(title='Aucun mot de passe n\'a été saisi', message='Mot de passe non défini ! Veuillez réessayer')
        else:
            tf = open("Etiquette_d'image_de_simulation/psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Mot de passe enregistré', message='Le nouveau mot de passe a été enregistré avec succès !')
            return
    op = (old.get())
    newp= (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if(newp == nnewp):
            txf = open("Etiquette_d'image_de_simulation/psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Erreur', message='Confirmez à nouveau le nouveau mot de passe !')
            return
    else:
        mess._show(title='Mot de passe erroné', message='Veuillez entrer l\'ancien mot de passe correct.')
        return
    mess._show(title='Mot de passe changé', message='Mot de passe changé avec succès !')
    master.destroy()

###################################################################################

def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False,False)
    master.title("Changer le mot de passe")
    master.configure(background="white")
    lbl4 = tk.Label(master,text='    Entrez l\'ancien mdp ',bg='white',font=('times', 12, ' bold '))
    lbl4.place(x=10,y=10)
    global old
    old=tk.Entry(master,width=25 ,fg="#fff",relief='solid',font=('times', 10, ' bold '),show='*')
    old.place(x=180,y=10)
    lbl5 = tk.Label(master, text='   Entrez le nouveau mdp', bg='white', font=('times', 10, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="#fff",relief='solid', font=('times', 12, ' bold '),show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='Confirmer le nouveau mdp', bg='white', font=('times', 10, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="#fff", relief='solid',font=('times', 12, ' bold '),show='*')
    nnew.place(x=180, y=80)
    cancel=tk.Button(master,text="Annuler", command=master.destroy ,fg="white"  ,bg="#F4556F" ,height=1,width=25 , activebackground = "white" ,font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="Sauvegarder", command=save_pass, fg="white", bg="#58C472", height = 1,width=25, activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()

#####################################################################################

def psw():
    assure_path_exists("Etiquette_d'image_de_simulation/")
    exists1 = os.path.isfile("Etiquette_d'image_de_simulation/psd.txt")
    if exists1:
        tf = open("Etiquette_d'image_de_simulation/psd.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('Ancien mot de passe non trouvé', 'Veuillez entrer un nouveau mot de passe ci-dessous', show='*')
        if new_pas == None:
            mess._show(title='Aucun mot de passe n\'a été saisi', message='Mot de passe non défini ! \n Veuillez réessayer')
        else:
            tf = open("Etiquette_d'image_de_simulation/psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Mot de passe enregistré', message='Le nouveau mot de passe a été enregistré avec succès !')
            return
    password = tsd.askstring('Mots de Passe', 'Entrez le mot de passe', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='Mot de passe incorrect', message='Vous avez saisi un incorrect mdp')

######################################################################################

def clear():
    txt.delete(0, 'end')
    res = "1)Prenez des photos  >>>  2)Enregistrer le profil"
    message1.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = "1)Prenez des photos >>>  2)Enregistrer le profil"
    message1.configure(text=res)


#######################################################################################

def Prenez_des_images():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    assure_path_exists("Details_l'Etudiant/")
    assure_path_exists("Image_d'entrainement/")
    serial = 0
    exists = os.path.isfile("Details_l'Etudiant/Details_l'Etudiant.csv")
    if exists:
        with open("Details_l'Etudiant/Details_l'Etudiant.csv", 'r') as csvFile1:
         serial = len(csvFile1.readlines())
        csvFile1.close()
    else:
        with open("Details_l'Etudiant/Details_l'Etudiant.csv", 'a+') as csvFile1:
            serial = len(csvFile1.readlines())
        csvFile1.close()
    Id = (txt.get())
    name = (txt2.get())
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder Image_d'entrainement
                cv2.imwrite("Image_d'entrainement/ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('Prise d\'images', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = " Images prises CNE :" + Id
        row = [serial, '', Id, '', name]
        with open('Details_l\'Etudiant/Details_l\'Etudiant.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Entrez le nom correct"
            message.configure(text=res)

########################################################################################

def TrainImages():
    check_haarcascadefile()
    assure_path_exists("Etiquette_d'image_de_simulation/")
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("Image_d'entrainement")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='Aucun Enregistrement', message='S\'il vous plaît, enregistrez quelqu\'un d\'abord ')
        return
    recognizer.save("Etiquette_d'image_de_simulation/Trainner.yml")
    res = "Profil sauvegardé avec succès"
    message1.configure(text=res)
    message.configure(text='Nombre total d\'inscriptions : ' + str(ID[0]))

############################################################################################3

def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids

###########################################################################################

def Tracking_des_images():

    check_haarcascadefile()
    assure_path_exists("Details_l'Etudiant/")
    for k in tv.get_children():
        tv.delete(k)
    i = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    exists3 = os.path.isfile("Etiquette_d'image_de_simulation/Trainner.yml")
    if exists3:
        recognizer.read("Etiquette_d'image_de_simulation/Trainner.yml")
    else:
        mess._show(title='Details manquants', message='Veuillez cliquer sur Enregistrer le profil pour réinitialiser les données !')
        return
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    presences= []
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    exists1 = os.path.isfile("Details_l'Etudiant/Details_l'Etudiant.csv")
    if exists1:
        df = pd.read_csv("Details_l'Etudiant/Details_l'Etudiant.csv")
    else:
        mess._show(title='Details manquants', message='Des détails sur les étudiants manquent, veuillez vérifier !')
        cam.release()
        cv2.destroyAllWindows()
        window.destroy()
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%d-%m')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                nom = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                ID = str(ID)
                ID = ID[1:-1]
                bb = str(nom)
                bb = bb[2:-2]
                etudaint_a = [str(ID),bb, str(date),str(timeStamp)]
                if (len(presences)==0) :
                    presences.append(etudaint_a)
                else :
                  i=0
                  for etudiant in presences :
                        if(etudiant[1] != bb) :
                         i+=1
                if(len(presences)==i) :
                    presences.append(etudaint_a)
            else:
                Id = 'Inconnu'
                bb = str(Id)
            cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow("Notant la presence",im)
        if (cv2.waitKey(1) == ord('q')):
            ajouter_presences(presences)
            bring_data()
            break
    cam.release()
    cv2.destroyAllWindows()

######################################## Des variables global ############################################

global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%d-%m')
year,day,month=date.split("-")

mont={'01':'janvier',
      '02':'février',
      '03':'mars',
      '04':'Avril',
      '05':'Mai',
      '06':'Juin',
      '07':'Juillet',
      '08':'Août',
      '09':'September',
      '10':'Octobre',
      '11':'Novembre',
      '12':'Décembre'
      }

######################################## GUI FRONT-END ###########################################

window = tk.Tk()
window.geometry("1280x720")
window.resizable(False,False)
window.title("Système de gestion des Présences ")
window.configure(background='#D9D9D9')

frame1 = tk.Frame(window, bg="#999999")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#999999")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="                     Système de gestion des présences" ,fg="black",bg="#D9D9D9" ,width=55 ,height=1,font=('times', 29, ' bold '))
message3.place(x=10, y=10)


image=ImageTk.PhotoImage(Image.open("ests_logo.png").resize((180,110),Image.ANTIALIAS))
lable0 = tkinter.Label(image=image)
lable0.image=image
lable0.place(x=9,y=9)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.34, rely=0.09, relwidth=0.18, relheight=0.07)

datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"  |  ", fg="orange",bg="#D9D9D9" ,width=55 ,height=1,font=('times', 22, ' bold '))
datef.pack(fill='both',expand=1)

clock = tk.Label(frame3,fg="orange",bg="#D9D9D9" ,width=55 ,height=1,font=('times', 22, ' bold '))
clock.pack(fill='both',expand=1)
tick()

head2 = tk.Label(frame2, text="                           S'inscrire                                          ", fg="#fff",bg="#252525" ,font=('times', 17, ' bold ') )
head2.grid(row=0,column=0)

head1 = tk.Label(frame1, text="                        Marquer la présence                                 ", fg="#fff",bg="#252525" ,font=('times', 17, ' bold ') )
head1.place(x=0,y=0)

lbl = tk.Label(frame2, text="Entrer CNE",width=20  ,height=1  ,fg="#fff"  ,bg="#999999" ,font=('times', 17, ' bold ') )
lbl.place(x=80, y=55)

txt = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold '))
txt.place(x=30, y=88)

lbl2 = tk.Label(frame2, text="Entrez le nom complet",width=20  ,fg="#fff"  ,bg="#999999" ,font=('times', 17, ' bold '))
lbl2.place(x=80, y=140)

txt2 = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=30, y=173)

message1 = tk.Label(frame2, text="1)Prenez des photos >>>  2)Enregistrer le profil" ,bg="#999999" ,fg="#fff"  ,width=43 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
message1.place(x=7, y=230)

message = tk.Label(frame2, text="" ,bg="#999999" ,fg="#fff"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
message.place(x=7, y=450)

lbl3 = tk.Label(frame1, text="Présence",width=20  ,fg="#fff"  ,bg="#999999"  ,height=1 ,font=('times', 17, ' bold '))
lbl3.place(x=100, y=115)

res=0
exists = os.path.isfile("Details_l'Etudiant/Details_l'Etudiant.csv")
if exists:
    with open("Details_l'Etudiant/Details_l'Etudiant.csv", 'r') as csvFile1:
     res = len(csvFile1.readlines()) - 1
    csvFile1.close()
else:
    res = 0
message.configure(text='Nombre total d\'inscriptions  : '+str(res))

#####################  barre de menu  #################################

menubar = tk.Menu(window,relief='ridge')
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='Changer le mots de passe', command = change_pass)
filemenu.add_command(label='Contactez-Nous', command = contact)
filemenu.add_command(label='Quittez',command = window.destroy)
menubar.add_cascade(label='Aide',font=('times', 15, ' bold '),menu=filemenu)

################## TABLE DE PRÉSENCE TREEVIEW ####################

tv= ttk.Treeview(frame1,height =13,columns = ('#0','#1','#2','#3'))
tv.column('#0',width=120)
tv.column('#1',width=130)
tv.column('#2',width=133)
tv.column('#3',width=133)
tv.grid(row=0,column=0,padx=(0,0),pady=(150,0),columnspan=4)
tv.heading('#0',text ='CNE')
tv.heading('#1',text ='NOM')
tv.heading('#2',text ='DATE')
tv.heading('#3',text ='TEMPS')

###################### SCROLLBAR ################################

scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
scroll.grid(row=2,column=4,padx=(0,100),pady=(150,0),sticky='ns')
tv.configure(yscrollcommand=scroll.set)

###################################### Remplir le tableau #################################################
def bring_data():


    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='presence',
                                             user='admin',
                                             password='')
        ts = time.time()
        date= datetime.datetime.fromtimestamp(ts).strftime('%Y-%d-%m')
        temps = datetime.datetime.fromtimestamp(ts).strftime('%H')
        sql_select_query: str = "select * from presences where DATE_FORMAT(presences.Date, '%Y-%d-%m')  = '"+date+"' and SUBSTR(presences.temps, 1, 2) = '"+temps+"';"
        cursor = connection.cursor()
        cursor.execute(sql_select_query)
        # get all records
        records = cursor.fetchall()
        for row in records:
            tv.insert('',tk.END,text=row[0],values=(row[1],row[2],row[3]))

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()

######################################ajouter_presences#################################################
def ajouter_presences(presences):


    try:

        connection = mysql.connector.connect(host='localhost',
                                             database='presence',
                                             user='admin',
                                             password='')



        cursor = connection.cursor()
        for row in presences:
            print(row[2])
            sql_select_Query = "INSERT INTO `presences` (`CNE`, `Nom_complet`, `Date`, `temps`) VALUES ('"+row[0]+"','"+row[1]+"',  STR_TO_DATE( '"+row[2]+"' , '%Y-%d-%m' ) ,  STR_TO_DATE('"+row[3]+"','%H:%i:%s'))"
            cursor.execute(sql_select_Query)
            connection.commit()

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():

            connection.close()
            cursor.close()



###################### Les BUTTONS ##################################

clearButton = tk.Button(frame2, text="Effacer", command=clear  ,fg="white"  ,bg="#F4556F"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
clearButton.place(x=335, y=86)
clearButton2 = tk.Button(frame2, text="Effacer", command=clear2  ,fg="white"  ,bg="#F4556F"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
clearButton2.place(x=335, y=172)
takeImg = tk.Button(frame2, text="Prenez des photos", command=Prenez_des_images  ,fg="white"  ,bg="#F8C03E"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
takeImg.place(x=30, y=300)
trainImg = tk.Button(frame2, text="Enregistrer le profil", command=psw ,fg="white"  ,bg="#F8C03E"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trainImg.place(x=30, y=380)
trackImg = tk.Button(frame1, text="Prendre les présences", command=Tracking_des_images  ,fg="white"  ,bg="#58C472"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trackImg.place(x=30,y=50)
quitWindow = tk.Button(frame1, text="Quittez", command=window.destroy  ,fg="white"  ,bg="#F4556F"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
quitWindow.place(x=30, y=450)

##################### Fin ######################################

window.configure(menu=menubar)
bring_data()
window.mainloop()

####################################################################################################



