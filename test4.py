# LINEに通知を送るプログラム

import requests

url = "https://notify-api.line.me/api/notify" 
token = "PDVs5KsUBhhXZlCnXY0enoRA7QGCgkawD1kdiwUX1YQ"
headers = {"Authorization" : "Bearer "+ token} 
message =  "侵入者あり。画像をかくにんしてください！！" 
payload = {"message" :  message} 
r = requests.post(url, headers = headers, params=payload)