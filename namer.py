import urllib.request
import urllib.parse
from pages.views import Register_form
 
import os
import cv2
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image
import pickle


m=tk.Tk()
wid=20
hit=10
widscr=m.winfo_screenwidth()
hitscr=m.winfo_screenheight()
x=(widscr/2)-(wid/2)
y=(hitscr/2)-(hit/2)
m.geometry("%dx%d+%d+%d" % (wid,hit,x,y))
m.after(25,lambda:m.destroy())
    
def get_image(path):
    image_path=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    ids=[]
    for img_path in image_path:
        faceImg=Image.open(img_path).convert("L")
        size=(350,350)
        final_img=faceImg.resize(size,Image.ANTIALIAS)
        facenp=np.array(final_img,"uint8")
        ID=int(os.path.split(img_path) [-1].split(".") [1])
        faces.append(facenp)
        ids.append(ID)
        cv2.waitKey(5)
    return np.array(ids),faces

def dataset_generator(id):
    cam=cv2.VideoCapture(0)
    detector=cv2.CascadeClassifier(r"C:\Users\Shantanu Shukla\djangoProject\pages\haarcascade_frontalface_default.xml")
    sample_Num=0
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
        for(x,y,w,h) in faces:
            if w*h>=33120:
                sample_Num=sample_Num+1
                cv2.imwrite(r"media/user."+str(id)+"."+str(sample_Num)+".jpg",gray[y:y+h,x:x+w])
                cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        cv2.imshow("img",im)
        cv2.waitKey(5)
        if sample_Num>500:
            cam.release()
            cv2.destroyAllWindows()
            break
    recog= cv2.face.LBPHFaceRecognizer_create()
    ids,faces= get_image(r"media")
    recog.train(faces,ids)
    recog.save("pages/trainingdata.yml")
    cv2.destroyAllWindows()
    messagebox.showinfo("SUCCESS!","Successfully Registered!!!")


def face_detector():
    recogniser= cv2.face.LBPHFaceRecognizer_create()
    recogniser.read("trainingdata.yml")
    facesCascade= cv2.CascadeClassifier(r"C:\Users\Shantanu Shukla\djangoProject\pages\haarcascade_frontalface_default.xml")
    cam= cv2.VideoCapture(0)
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    while True:
        ret,im =cam.read()
        if ret!=0:
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=facesCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(int(minW),int(minH)), flags = cv2.CASCADE_SCALE_IMAGE)
        co1=0
        co2=0
        i=0
        abc=[]
        for(x,y,w,h) in faces:
            i+=1
            if i<=100:
                 id, conf= recogniser.predict(gray[y:y+h,x:x+w])
                 cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                 if conf<50: #and conf<=85:
                     co1+=1
                     abc[i-1]=id
                 else:
                     co2+=1
            else:
                 break
        cv2.imshow("img",im)
        cv2.waitKey(5)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cam.release()
            cv2.destroyAllWindows()
            break
    res = max(set(abc), key = abc.count) 
    if(co1>co2):
        return res
    else:
        messagebox.showinfo("WARNING!","Face not matched!!!. Try again...")
        return "0"
            



def send_SMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

def otp(apikey, numbers, sender, message):   
	resp =  send_SMS(apikey, numbers, sender, message)

m.mainloop()

	