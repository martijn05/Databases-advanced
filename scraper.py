from bs4 import BeautifulSoup
import time
import numpy as np
import pandas as pd
import re
import requests
import pymongo as mongo


client = mongo.MongoClient("mongodb://127.0.0.1:8080")



while(True):
    
    

    blockchain_db = client["blockchain"]

    url = "https://www.blockchain.com/btc/unconfirmed-transactions"
    r = requests.get(url)

    bit = []
    USD = []
    Time = []
    Hash = []

    c = r.content
    soup = BeautifulSoup(c)

    for link in soup.find_all("div",class_= "sc-1au2w4e-0 emaUuf" ):
        tijd = re.sub("Time","",link.getText())
        Time.append(tijd)

        
        
        
    count = 0
    for link in soup.find_all("div",class_= "sc-1au2w4e-0 fTyXWG" ):
        BTC = re.sub(r"\(BTC\)||\(USD\)||(Amount)","",link.getText())
        BTC = BTC.split("BTC")


        if(int(count) >= 2):

            if(count % 2 == 0):
                bit.append(BTC[0])
                count = count+1
            else:
                USD.append(BTC[0])
                count = count+1
        else:
            count = count+1



    for link in soup.find_all("div",class_= "sc-1au2w4e-0 bTgHwk" ):
        has = re.sub("Hash","",link.getText())
        Hash.append(has)


    results = []

    for i in range(0,30):
        
        if(i >= 1):
            results.append(Time[i])
            results.append(Hash[i])
            results.append(bit[i -1])
            results.append(USD[i-1])


    listall = []
    listdf = []
    timer = 0

    for i in range(len(results)):
        listall.append(results[i])
        timer = timer + 1
        if(timer==4):
            listdf.append(listall)
            listall = []
            timer = 0



    BTC_DF = pd.DataFrame(listdf, columns = ['Time', 'Hash', 'BTC', 'USD'])
    BTC_DF = BTC_DF.astype({ 'Time': str,'Hash': str, 'BTC': float, 'USD': str})

    BTC_DF= BTC_DF.sort_values(by=["BTC"], ascending=False, ignore_index=True)

    json = BTC_DF[0:5].to_dict("lines")

    print(BTC_DF[0:5])



    col_Time = blockchain_db["blockchain"]
    

    y = col_Time.insert_one(json)

    time.sleep(60)
