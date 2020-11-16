#从co2-mm-gl.json中读取数据，以Date作为横坐标，在一张图上绘制Average和Trend的折线图
import matplotlib.pyplot as plt 
import numpy as np 
import json
from matplotlib.pyplot import MultipleLocator
from datetime import datetime
import matplotlib.ticker as ticker
x=[]
y1=[]
y2=[]
filename='C:\\Users\\admin\\Desktop\\程序设计实验报告-2\\co2-mm-gl.json'
with open(filename) as f:
    dict=json.load(f)
for item in range(463):
    d=dict[item]['Date']
    x.append(d)
    a=dict[item]['Average']
    y1.append(a)
    t=dict[item]['Trend']
    y2.append(t)
y1_major_locator=MultipleLocator(10.00)
y2_major_locator=MultipleLocator(10.00)
for a in x : 
    a= datetime.strptime(a, "%Y-%m-%d")
tick_spacing=100
tick_spacing=100
fig, ax = plt.subplots(1,1)
ax.plot(x,y1,color = 'grey',label='average')
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax.plot(x,y2,color = 'orange', label='trend')
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

plt.show()
