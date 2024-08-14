#カメラ映像を表示する＋動画ファイルに保存するプログラム
import cv2
import numpy as np
import LINE
import datetime

#標準入力からトークンを取得
token = input("トークン入力：")

#カメラチャンネルを指定する
cap = cv2.VideoCapture(0)

#動画保存の際の、コーデックを指定する
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

#リフレッシュレート
fps = 20.0

#解像度
size = (640, 360)

#インスタンスの作成
writer = cv2.VideoWriter('test.m4v', fmt, fps, size)

#escキーを押すまで動画撮影
while True:
    #戻り値の片方は使用しない
    _, frame = cap.read()
    frame = cv2.resize(frame, size)
    #writerに１フレーム分追加
    writer.write(frame)
     
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
