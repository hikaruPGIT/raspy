#人感センサ（18ピン）が反応したら、60フレーム分（約3秒）、動画を保存するプログラム

import RPi.GPIO as GPIO
import cv2
import time
import datetime
import numpy as np

GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN,GPIO.IN)

while True:
    if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
        
        print("1")
        
        dt_now = datetime.datetime.now()
        file_name = dt_now.strftime('%Y年%m月%d日%H時%M分%S秒')
        print(file_name)
        
        #カメラ映像を保存する
        cap = cv2.VideoCapture(0)
        fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        fps = 20.0
        size = (640, 360)
        writer = cv2.VideoWriter((file_name + '.m4v'), fmt, fps, size)
        
        i = 0
        #60フレーム撮影する
        while i < 60:
            _, frame = cap.read()
            frame = cv2.resize(frame, size)
            writer.write(frame)
     
            i = i + 1
             
        writer.release()
        cap.release()
        
        time.sleep( 10 )
        
    else:
        print("0")
        time.sleep( 1 )
GPIO.cleanup()