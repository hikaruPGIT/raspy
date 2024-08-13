# LINEに通知を送るプログラム

import requests
def LINE():
    url = "https://notify-api.line.me/api/notify" 
    token = ""
    headers = {"Authorization" : "Bearer "+ token} 
    message =  "侵入者あり。画像をかくにんしてください！！" 
    payload = {"message" :  message} 
    r = requests.post(url, headers = headers, params=payload)