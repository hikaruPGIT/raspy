{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a5a4d4be-dd45-4b52-97a9-2c1248b14565",
   "metadata": {},
   "outputs": [],
   "source": [
    "import fitbit\n",
    "from ast import literal_eval\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.dates as mdates\n",
    "import numpy as np\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "17a157bd-e898-4c83-81f0-7e6a8eb61358",
   "metadata": {},
   "outputs": [],
   "source": [
    "CLIENT_ID     = \"23QPZV\" \n",
    "CLIENT_SECRET = \"ef47477d9cd2bc1b852e02b815828102\"\n",
    "TOKEN_FILE    = \"token.txt\"\n",
    "\n",
    "tokens = open(TOKEN_FILE).read()\n",
    "token_dict = literal_eval(tokens)\n",
    "access_token = token_dict['access_token']\n",
    "refresh_token = token_dict['refresh_token']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "9d81d78e-df50-45e2-a570-3e2c7ed613ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "def updateToken(token):\n",
    "    f = open(TOKEN_FILE, 'w')\n",
    "    f.write(str(token))\n",
    "    f.close()\n",
    "    return\n",
    "client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET,\n",
    "    access_token = access_token, refresh_token = refresh_token, refresh_cb = updateToken)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8074a549-1e82-4214-8821-09a410a61813",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>dateTime</th>\n",
       "      <th>value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2025-08-02</td>\n",
       "      <td>550</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     dateTime value\n",
       "0  2025-08-02   550"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "DATE = \"2025-08-02\"\n",
    "weight_data = client.time_series('body/weight', base_date=DATE, period='1d')\n",
    "kgs=round(float(weight_data['body-weight'][0]['value'])*0.45359237)\n",
    "weight_data['body-weight'][0]['value']=str(kgs)\n",
    "weight_df = pd.DataFrame(weight_data['body-weight'])\n",
    "weight_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "0ab79544-206f-4fc9-bc63-47db85bd6c50",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>isFavorite</th>\n",
       "      <th>logDate</th>\n",
       "      <th>logId</th>\n",
       "      <th>loggedFood</th>\n",
       "      <th>nutritionalValues</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>False</td>\n",
       "      <td>2025-08-01</td>\n",
       "      <td>36964426224</td>\n",
       "      <td>{'accessLevel': 'PRIVATE', 'amount': 1, 'brand...</td>\n",
       "      <td>{'calories': 100, 'carbs': 0, 'fat': 0, 'fiber...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>False</td>\n",
       "      <td>2025-08-01</td>\n",
       "      <td>36966276659</td>\n",
       "      <td>{'accessLevel': 'PRIVATE', 'amount': 1, 'brand...</td>\n",
       "      <td>{'calories': 124, 'carbs': 0, 'fat': 0, 'fiber...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>False</td>\n",
       "      <td>2025-08-01</td>\n",
       "      <td>36961063572</td>\n",
       "      <td>{'accessLevel': 'PRIVATE', 'amount': 1, 'brand...</td>\n",
       "      <td>{'calories': 100, 'carbs': 0, 'fat': 0, 'fiber...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   isFavorite     logDate        logId  \\\n",
       "0       False  2025-08-01  36964426224   \n",
       "1       False  2025-08-01  36966276659   \n",
       "2       False  2025-08-01  36961063572   \n",
       "\n",
       "                                          loggedFood  \\\n",
       "0  {'accessLevel': 'PRIVATE', 'amount': 1, 'brand...   \n",
       "1  {'accessLevel': 'PRIVATE', 'amount': 1, 'brand...   \n",
       "2  {'accessLevel': 'PRIVATE', 'amount': 1, 'brand...   \n",
       "\n",
       "                                   nutritionalValues  \n",
       "0  {'calories': 100, 'carbs': 0, 'fat': 0, 'fiber...  \n",
       "1  {'calories': 124, 'carbs': 0, 'fat': 0, 'fiber...  \n",
       "2  {'calories': 100, 'carbs': 0, 'fat': 0, 'fiber...  "
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "DATE = \"2025-08-01\"\n",
    "nutrition_data = client.foods_log(date=DATE)\n",
    "nutrition_df = pd.DataFrame(nutrition_data['foods'])\n",
    "nutrition_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "1e6944cc-157b-45ca-9e11-1ef819a245a0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>isFavorite</th>\n",
       "      <th>logDate</th>\n",
       "      <th>logId</th>\n",
       "      <th>loggedFood</th>\n",
       "      <th>nutritionalValues</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>False</td>\n",
       "      <td>2025-08-01</td>\n",
       "      <td>36964426224</td>\n",
       "      <td>{'accessLevel': 'PRIVATE', 'amount': 1, 'brand...</td>\n",
       "      <td>{'calories': 100, 'carbs': 0, 'fat': 0, 'fiber...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>False</td>\n",
       "      <td>2025-08-01</td>\n",
       "      <td>36966276659</td>\n",
       "      <td>{'accessLevel': 'PRIVATE', 'amount': 1, 'brand...</td>\n",
       "      <td>{'calories': 124, 'carbs': 0, 'fat': 0, 'fiber...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>False</td>\n",
       "      <td>2025-08-01</td>\n",
       "      <td>36961063572</td>\n",
       "      <td>{'accessLevel': 'PRIVATE', 'amount': 1, 'brand...</td>\n",
       "      <td>{'calories': 100, 'carbs': 0, 'fat': 0, 'fiber...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   isFavorite     logDate        logId  \\\n",
       "0       False  2025-08-01  36964426224   \n",
       "1       False  2025-08-01  36966276659   \n",
       "2       False  2025-08-01  36961063572   \n",
       "\n",
       "                                          loggedFood  \\\n",
       "0  {'accessLevel': 'PRIVATE', 'amount': 1, 'brand...   \n",
       "1  {'accessLevel': 'PRIVATE', 'amount': 1, 'brand...   \n",
       "2  {'accessLevel': 'PRIVATE', 'amount': 1, 'brand...   \n",
       "\n",
       "                                   nutritionalValues  \n",
       "0  {'calories': 100, 'carbs': 0, 'fat': 0, 'fiber...  \n",
       "1  {'calories': 124, 'carbs': 0, 'fat': 0, 'fiber...  \n",
       "2  {'calories': 100, 'carbs': 0, 'fat': 0, 'fiber...  "
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nutrition_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1e458164-3250-4f73-aa42-1dcdd5a5b693",
   "metadata": {},
   "outputs": [],
   "source": [
    "a=print"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "eb7b84b1-8ee8-46d6-bc4c-1740a0f68ea9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function print(*args, sep=' ', end='\\n', file=None, flush=False)>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "a679b0f9-98ce-4496-b536-944278dfa6a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "torisetu=open(\"tekitou.txt\",encoding=\"utf-8\").read()\n",
    "result=literal_eval(torisetu)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "6ddf4035-9447-43b5-8f09-b11f8da4b032",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(torisetu)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "c49b7468-6a84-4964-ac96-e010ba75ef07",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Google'"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result[\"No1\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "0db96c1d-eecc-41f2-9b80-be74e88b4814",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16d1b36d-bd43-4969-972b-8a8803ae1707",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
