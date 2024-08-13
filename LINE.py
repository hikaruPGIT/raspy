# LINEに通知を送るプログラム

import requests
def LINE(inputtoken,Discov_time):
    url = "https://notify-api.line.me/api/notify" 
    token = inputtoken
    print("とーくんは"+token)
    headers = {"Authorization" : "Bearer "+ token} 
    files = {'imageFile': open("sinnyuusya.jpg", "rb")}
    message =  Discov_time+"侵入者あり。画像をかくにんしてください！！" 
    payload = {"message" :  message} 
    r = requests.post(url, headers = headers, params=payload, files=files)