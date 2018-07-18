import numpy as np
import cv2
#haarcascade_eye.xml  haarcascade_smile.xml
#cargamos la plantilla e inicializamos la webcam:
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap = cv2.VideoCapture(1)
while(True):
    #leemos un frame y lo guardamos
    ret, img = cap.read()
    #convertimos la imagen a blanco y negro
    #img= cv2.imread('amigos.jpg',1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    con=0  
    #buscamos las coordenadas de los rostros (si los hay) y
    #guardamos su posicion
    faces = face_cascade.detectMultiScale(gray, 1.3, 1)
    smiles = smile_cascade.detectMultiScale(gray, 1.3, 10)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 3)
    #if not faces:
     #   print("no cara")
    #print(len(faces))
    #print("caras ",faces)
    #Dibujamos un rectangulo en las coordenadas de cada rostro
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),2)
        #Dibujamos un rectangulo en las coordenadas de cada rostro
        for (a,b,c,d) in smiles:            
            if a>x and b>y and a+c<x+w and b+d<y+h:                
                cv2.rectangle(img,(a,b),(a+c,b+d),(0,255,255),2)
        for (a,b,c,d) in eyes:
            if a>x and b>y and a+c<x+w and b+d<y+h:
                cv2.rectangle(img,(a,b),(a+c,b+d),(255,255,255),2)
        #  Mostramos la imagen
     
    cv2.imshow('img',img)
         
        #con la tecla 'q' salimos del programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
    
cap.release()

cv2-destroyAllWindows()
      
