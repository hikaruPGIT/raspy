import cv2 as cv
import time
import picamera

fn="my_pic.jpg"


#カメラの初期化
with picamera.PiCamera() as camera:
    camera.resolution=(512,384)#解像度の設定
    camera.start_preview()
    time.sleep(2)
    camera.capture(fn)
    img=cv.imread(fn)
    grayimg=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_cascade=cv.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
    eye_cascade=cv.CascadeClassifier("haarcascades/haarcascade_eye.xml")
    facerect=face_cascade.detectMultiScale(grayimg,scaleFactor=1.2,minNeighbors=2,minSize=(1,1))
    eyerect=eye_cascade.detectMultiScale(grayimg)
    
    print(facerect)
    print(eyerect)
    
    if len(facerect)>0:
        for rect in facerect:
            cv.rectangle(img,tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]),(0,255,0),thickness=3)
    if len(eyerect)>0:
        for rect in eyerect:
            cv.rectangle(img,tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]),(0,255,0),thickness=3)
    cv.imshow("camera",img)
    cv.imwrite(fn,img)
   
   
    cv.waitKey(0)
    cv.destroyAllWindows()
