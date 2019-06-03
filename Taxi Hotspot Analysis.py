
# coding: utf-8

# In[29]:


import folium   
from sklearn.cluster import KMeans  
import plotly 
import plotly.plotly as py
import plotly.graph_objs as go
import urllib.request # download data, refer this link "https://docs.python.org/2/library/urllib2.html"
import csv
import numpy as np
import requests
from bs4 import BeautifulSoup
import lxml
import re
plotly.tools.set_credentials_file(username='lane569', api_key='1qQt7yshvb4M05SO7dRm')
import math 


# In[3]:


file_name = "C:\\Users\\Yi Ching\\Desktop\\Cloud_computing\\taxi hotspot inspection\\final\\yellow_tripdata_2012-10.csv"
file_object = open(file_name,"r")
data = np.array([row for row in csv.reader(file_object)])
data = data[1:]
sample_index = np.random.choice(len(data),len(data)//100) #0.01
sample_data = data[sample_index]

f = open("C:\\Users\\Yi Ching\\Desktop\\Cloud_computing\\taxi hotspot inspection\\final\\sample_2.csv","w")
for row in sample_data:
    f.write(",".join(row))
    f.write("\n")
f.close()


# In[21]:


#載入10月的計程車資料
file_name = "C:\\Users\\Yi Ching\\Desktop\\Cloud_computing\\taxi hotspot inspection\\final\\sample_2.csv"  
f = open(file_name,"r")
data = np.array([row for row in csv.reader(f)])
f.close()

#載入8月的計程車資料
file_name = "C:\\Users\\Yi Ching\\Desktop\\Cloud_computing\\taxi hotspot inspection\\final\\sample.csv"  
f = open(file_name,"r")
data_2 = np.array([row for row in csv.reader(f)])
f.close()


# In[43]:


#人數距離關係圖

distance = data[:,4]
distance_2 = data_2[:,4]

people = np.array([0]*10)
people_2 = np.array([0]*10)

for t in distance_2:
    index = int(float(t))
    if(index > 10):
        people_2[9] = people_2[9]+1
    else:
        people_2[index-1] = people_2[index-1]+1
    
for t in distance:
    index = int(float(t))
    if(index > 10):
        people[9] = people[9] + 1
    else:
        people[index-1] = people[index-1] + 1
        
people = np.round(people/float(len(distance)),3)
people_2 = np.round(people_2/float(len(distance_2)),3)
       
x = []
for i in range(1,11,1):
    if(i == 10):
        s = '>' + str(i)   
    else:
        s = str(i) + '-' + str(i+1)
    x.append(s)

trace0 = go.Bar(
    x = x ,
    y = people ,
    text = people,
    textposition = 'auto',
    name='十月資料',
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

trace1 = go.Bar(
    x = x ,
    y = people_2 ,
    text = people_2,
    textposition = 'auto',
    name = '八月資料',
    marker=dict(
        color='rgb(204,204,204)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

source = [trace0,trace1]
layout = dict(title = '距離人數關係圖',
              font = dict(size = 20),
              xaxis = dict(title = 'Distance(km)',titlefont=dict(size=18),tickfont=dict(size=18)),
              yaxis = dict(title = 'Person',titlefont=dict(size=18),tickfont=dict(size=18))
)
fig = go.Figure(data=source, layout=layout)


py.image.save_as(fig, filename="C:\\Users\\Yi Ching\\Desktop\\Cloud_computing\\taxi hotspot inspection\\final\\distance_people.png")


# In[44]:


#費用距離關係圖
payamount = data[:,17]
payamount_2 = data_2[:,17]

person = np.array([0]*17)
person_2 = np.array([0]*17)

for k in payamount:
    index = int(float(k))
    if(index >= 20):
        person[16] = person[16] + 1
    elif(index <= 5):
        person[0] = person[0] + 1
    else:
        person[index-5] = person[index-5] + 1
        
for k in payamount_2:
    index = int(float(k))
    if(index >= 20):
        person_2[16] = person_2[16] + 1
    elif(index <= 5):
        person_2[0] = person_2[0] + 1
    else:
        person_2[index-5] = person_2[index-5] + 1
        
person = np.round(person/float(len(payamount)),3)
person_2 = np.round(person_2/float(len(payamount_2)),3)
    
x = []
for i in range(0,17,1):
    if(i == 0):
        s = '<=5'
    elif(i == 16):
        s = '>20'
    else:
        s = str(i+4) + ' -' + str(i+5)
    x.append(s)


trace0 = go.Bar(
    x = x,
    y = person,
    text = person,
    textposition = 'auto',
    name = '十月資料',
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

trace1 = go.Bar(
    x = x,
    y = person_2,
    text = person_2,
    textposition = 'auto',
    name = '八月資料',
    marker=dict(
        color='rgb(204,204,204)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

source = [trace0,trace1]
layout = dict(title = '總費用與人數關係圖',
              font = dict(size = 20),
              xaxis = dict(title = 'Payamount(USD)',titlefont=dict(size=18),tickfont=dict(size=18)),
              yaxis = dict(title = 'Person',titlefont=dict(size=18),tickfont=dict(size=18))
)
fig = go.Figure(data=source, layout=layout)


py.image.save_as(fig, filename="C:\\Users\\Yi Ching\\Desktop\\Cloud_computing\\taxi hotspot inspection\\final\\payamount_people.png")


# In[45]:


payamount = data[:,12]
payamount_2 = data_2[:,12]

person = np.array([0]*17)
person_2 = np.array([0]*17)

for k in payamount:
    index = int(float(k))
    if(index >= 20):
        person[16] = person[16] + 1
    elif(index <= 5):
        person[0] = person[0] + 1
    else:
        person[index-5] = person[index-5] + 1
        
for k in payamount_2:
    index = int(float(k))
    if(index >= 20):
        person_2[16] = person_2[16] + 1
    elif(index <= 5):
        person_2[0] = person_2[0] + 1
    else:
        person_2[index-5] = person_2[index-5] + 1
        
person = np.round(person/float(len(payamount)),3)
person_2 = np.round(person_2/float(len(payamount_2)),3)
    
x = []
for i in range(0,17,1):
    if(i == 0):
        s = '<=5'
    elif(i == 16):
        s = '>20'
    else:
        s = str(i+4) + ' -' + str(i+5)
    x.append(s)


trace0 = go.Bar(
    x = x,
    y = person,
    text = person,
    textposition = 'auto',
    name = '十月資料',
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

trace1 = go.Bar(
    x = x,
    y = person_2,
    text = person_2,
    textposition = 'auto',
    name = '八月資料',
    marker=dict(
        color='rgb(204,204,204)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

source = [trace0,trace1]
layout = dict(title = '車費與人數關係圖',
              font = dict(size = 20),
              xaxis = dict(title = 'Payamount(USD)',titlefont=dict(size=18),tickfont=dict(size=18)),
              yaxis = dict(title = 'Person',titlefont=dict(size=18),tickfont=dict(size=18))
)
fig = go.Figure(data=source, layout=layout)

py.image.save_as(fig, filename="C:\\Users\\Yi Ching\\Desktop\\Cloud_computing\\taxi hotspot inspection\\final\\taxiamount_people.png")

