import fitbit
from ast import literal_eval
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import seaborn as sns

CLIENT_ID     = "23QPZV" 
CLIENT_SECRET = "ef47477d9cd2bc1b852e02b815828102"
TOKEN_FILE    = "token.txt"

tokens = open(TOKEN_FILE).read()
token_dict = literal_eval(tokens)
access_token = token_dict['access_token']
refresh_token = token_dict['refresh_token']

def updateToken(token):
    f = open(TOKEN_FILE, 'w')
    f.write(str(token))
    f.close()
    return
client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET,
    access_token = access_token, refresh_token = refresh_token, refresh_cb = updateToken)

DATE = "2025-08-02"
weight_data = client.time_series('body/weight', base_date=DATE, period='1d')
kgs=round(float(weight_data['body-weight'][0]['value'])*0.45359237)
weight_data['body-weight'][0]['value']=str(kgs)
weight_df = pd.DataFrame(weight_data['body-weight'])
weight_df

DATE = "2025-08-01"
nutrition_data = client.foods_log(date=DATE)
nutrition_df = pd.DataFrame(nutrition_data['foods'])
nutrition_df