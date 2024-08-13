#カメラ映像を表示する＋動画ファイルに保存するプログラム

import cv2
import numpy as np
import LINE
import datetime

token=input("トークン入力：")
cap = cv2.VideoCapture(0)#カメラチャンネルを指定する
 
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')#動画保存の際の、コーデックを指定する
fps = 20.0#リフレッシュレート
size = (640, 360)#解像度
writer = cv2.VideoWriter('test.m4v', fmt, fps, size)
 
while True:
    _, frame = cap.read()#戻り値の片方は使用しない
    frame = cv2.resize(frame, size)
    writer.write(frame)#writerに１フレーム分追加
     
    cv2.imshow('題名', frame)
    #escキーで終了
    if cv2.waitKey(1) == 27:
        cv2.imwrite("sinnyuusya.jpg", frame)
        dt_now=datetime.datetime.now()
        Discovery_time = dt_now.strftime('%Y年%m月%d日%H時%M分%S秒')
        break
 
writer.release()
cap.release()
cv2.destroyAllWindows()
LINE.LINE(token,Discovery_time)