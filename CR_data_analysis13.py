import urllib.request as req
import json
url="https://docs.royaleapi.com/json/player_battles_8L9L9GL.json"
request=req.Request(url, headers={
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
})
with req.urlopen(request) as response:
    data=json.load(response)
#print(data)
with open("WHAM! eSports player_mungo.txt", mode="w", encoding="utf-8") as file:
    file.write("mungo近25場之對戰牌組:"+"\n"*2),
    used_cards_list=[]
    for x in range(25):
        decks=data[x]["team"]
        items=[]
        for item in decks:
            items.append(item["deck"])
        for y in range(8):
            #print(items[0][y]["name"])
            card=items[0][y]["name"]
            used_cards_list+=[card]
            file.write(card+"\n")        
        file.write("------------------------"+"\n"*2)

#print(used_cards_list)

def remove_duplicates(original):
    list_new=[]
    for i in original:
        if i not in list_new:
            list_new.append(i)
    return list_new
num=len(remove_duplicates(used_cards_list))
print("mungo近25戰所用過的卡牌數: ",num)

from collections import Counter
new_list=Counter(used_cards_list)
arranged_list=new_list.most_common()
#print(arranged_list)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
resultforplot=pd.value_counts(used_cards_list)
#print(resultforplot)

resultforplot.plot.barh(align="center",yerr=0.000001,figsize=(10,8),facecolor="#9999ff",edgecolor="white")
plt.xticks([3,10,20],["少用卡牌","常用卡牌","高熟練卡牌"],fontproperties="SimSun")
plt.xlabel("卡牌使用次數",fontproperties="SimSun")
plt.title("mungo近25戰所用卡牌",fontproperties="SimHei",fontsize=24)
plt.show()
