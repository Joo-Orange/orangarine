#从co2-mm-mlo.csv中读取数据，以Date作为横坐标，在一张图上绘制Interpolated和Trend的折线图
import matplotlib.pyplot as plt 
import numpy as np 
import csv
from matplotlib.pyplot import MultipleLocator
from datetime import datetime
import matplotlib.ticker as ticker
x=[]
y1=[]
y2=[]
filename='C:\\Users\\admin\\Desktop\\程序设计实验报告-2\\co2-mm-mlo.csv'
with open(filename) as f:
    reader=csv.reader(f)
    for row in reader:
        x.append(row[0])
        y1.append(row[3])
        y2.append(row[4])
del x[0]
del y1[0]
del y2[0]
for i in range(len(y1)):
    y1[i]=float(y1[i])
for i in range(len(y2)):
    y2[i]=float(y2[i])
y1_major_locator=MultipleLocator(10.00)
y2_major_locator=MultipleLocator(10.00)
for a in x : 
    a= datetime.strptime(a, "%Y-%m-%d")
tick_spacing=100
tick_spacing=100
fig, ax = plt.subplots(1,1)
ax.plot(x,y1,color = 'red')
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax.plot(x,y2,color = 'blue' )
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
plt.show()