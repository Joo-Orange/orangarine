#第三次程设实验-美国婴儿名字の分析
#实验要求如下：
'''
1. 读取姓名数据，存储为Pandas的DataFrame；
2. 输入姓名、年份，输出该姓名在该年份的出生人数；
3. 输入姓名、开始年份和结束年份，绘制该姓名在各年份出生人数折线图；
4. 输入若干姓名、开始年份和结束年份，绘制这些姓名在对应年份区间的出生总人数的条状图；
5. 输入姓名、开始年份、结束年份、人口预期寿命，绘制该姓名在各年份生存人数折线图；
6. 输入姓名A、姓名B、开始年份和结束年份，计算姓名A与姓名B出生人数的相关系数；
7. 输入年份，计算哪些名字是男性和女性都取的，若没有输出None，若有请按照取名总人数进行排序；
8. 计算输出每个年份的男性5大常用名和女性5大常用名；
9. 程序界面请自行设计，命令行、GUI、网页、手机App均可。
'''

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.pyplot import MultipleLocator

years=range(1880,2011)
pieces=[]                #空列表，许多frame的集合，之后要合并成一张表
columns=['name','gender','num']   #列的项目是：名字、性别、数量
for year in years:
    path='C:\\Users\\admin\\Desktop\\程序设计实验报告-3\\babynames\\babynames\\yob%d.txt' %year
    frame=pd.read_csv(path,names=columns)
    frame['year']=year
    pieces.append(frame)
df=pd.concat(pieces,ignore_index=True)  #许多frame的集合合并成一个
#print(df)      #in order to check if it is right

#2.输入姓名、年份，输出该姓名在该年份的出生人数-封装成函数 t2()
def t2():
    print('please input the name and the year you want to search\
    and you will get the number.')
    goalname=input()  #目标（goalname）---要查找的名字
    goalyear=input()  #要查找的年份
    df2=df[['gender','num']][(df['name']==str(goalname))&\
        (df['year']==int(goalyear))]         #表示在一个新建的dataframe（叫做df2）中，取出满足名字和年份与目标一样的
    print(df2)                               #而且在这个df2中，只保留'gender','num'两列

#3.输入姓名、开始年份和结束年份，绘制该姓名在各年份出生人数折线图 t3()
def t3():
    print('please input the name, start year, and the end year \
    you want, and you will get a chart concernong year and num')
    goalname=input()                        #目标名字和开始结束年份
    startyear=input() 
    endyear=input()
    start=int(startyear)                    #注意input（）进入的是str，要转化为int
    end=int(endyear)
    df3F=df[['gender','num','year']][(df['name']==goalname)&\
        (df['year']>=start)&(df['year']<=end)&(df['gender']=='F')]#df3F是女的（female），名字和年份和goal一样，性别女
    df3M=df[['gender','num','year']][(df['name']==goalname)&\
        (df['year']>=start)&(df['year']<=end)&(df['gender']=='M')]#同理，男的（male）
    #print(df3F)  #in order to check if it is right
    #print(df3M)
    #df3F.plot(df['year'],df['num'])
    fig, ax = plt.subplots(1,1)                              #创立一个画布
    ax.plot(df3F['year'],df3F['num'],color = 'red',label='Female') #画线
    ax.plot(df3M['year'],df3M['num'],color = 'blue',label='Male')
    ax.legend(loc='best')                                    #做图例
    ax.set_title('name Mary(example) analysis chart (1880-2010) ')
    plt.show()


#4.输入若干姓名、开始年份和结束年份，绘制这些姓名在对应年份区间的出生总人数的条状图 t4()
def t4():

    goalnames=input('please input names you want check and split with(also end with it) \',\': \n').split(',')
    start=int(input('please input the start year:\n'))
    end=int(input('please input the end year:\n'))
    sumlist=[]
    for name in goalnames:
        df_gn=df.loc[df['name']==name]   #新建的小df,放符合的name
        goalyear=[]
        total=[]            #里面是男女num之和的数据
        for i in range(start,end+1):
            df_gy=df_gn.loc[df_gn['year']==i]  #新建的小df,放符合的year
            numlist=[i for i in df_gy['num']]  #新建的list,用来存放同姓名同年份不同性别的num，以便之后求和，合并
            if len(numlist)==0:
                m=0
            else:
                m=sum(numlist)     #m就是同年份同姓名的男女num之和
            goalyear.append(i)
            total.append(m)
        totalsum=sum(total)
        sumlist.append(totalsum)
    plt.figure()
    x=range(len(goalnames))
    y=sumlist
    plt.bar(x,y,width=0.5,color=['blue','red','green','yellow'])
    plt.xticks(x,goalnames)
    plt.show()

#5. 输入姓名、开始年份、结束年份、人口预期寿命，绘制该姓名在各年份生存人数折线图；
def t5():
    print('please input name you want to search')
    goalname=input()
    print('please input start year and end year')
    startyear = input()
    endyear = input()
    start = int(startyear)
    end = int(endyear)
    print('please input Life expectancy of population:')
    expectancy_of_population=input()
    ex=int(expectancy_of_population)
    #合并同年份同姓名的男孩女孩出生人数人数
    df_gn=df.loc[df['name']==goalname]
    goalyear=[]
    total=[]            #里面是男女num之和的数据
    for i in range(start,end+1):
        df_gn=df.loc[df['year']==i]  #新建的小df
        numlist=[i for i in df_gn['num']]  #新建的list,用来存放同姓名同年份不同性别的num，以便之后求和，合并
        if len(numlist)==0:
            m=0
        else:
            m=sum(numlist)     #m就是同年份同姓名的男女num之和
        goalyear.append(i)
        total.append(m)
    total2=total[:]
    #接下来开始绘制曲线
    for i in range(len(goalyear)):
        for n in range(i+1,len(goalyear)):
            if goalyear[i]+ex > goalyear[n]:
                total[n]=total[n]+total2[i]
            else:
                total[n]=total[n]-total2[i]           
    plt.figure
    plt.plot(goalyear,total)
    plt.show()
    
#6. 输入姓名A、姓名B、开始年份和结束年份，计算姓名A与姓名B出生人数的相关系数；
def t6():
    print('以1880-1885的Mary和Anna为例')
    #print('please input 2 names you want:')
    namea="Mary"
    nameb="Anna"
    #print('please input the start year and the end year')
    startyear = 1880
    endyear = 1885
    start = int(startyear)
    end = int(endyear)
    df6a=df[['name','gender','num','year']][(df['name']==namea)&\
        (df['year']>=start)&(df['year']<=end)]
    df6b=df[['name','gender','num','year']][(df['name']==nameb)&\
        (df['year']>=start)&(df['year']<=end)]
    df6a= df6a.reset_index()
    df6b= df6b.reset_index()
    df6a['numb']=df6b['num']
    df6=df6a.drop(['name','gender','year','index'],axis=1)
    #print(df6)
    print(df6.corr('spearman'))

#7. 输入年份，计算哪些名字是男性和女性都取的，若没有输出None，若有请按照取名总人数进行排序；
def t7():
    print('please input the year you want')
    y=int(input())
    years=range(1880,2011)
    pieces=[]     
    #复制了开头的操作，但这次只需要特定一年的数据
    columns=['name','gender','num']   
    for year in range(y,y+1):
        path='C:\\Users\\admin\\Desktop\\程序设计实验报告-3\\babynames\\babynames\\yob%d.txt' %year
        frame=pd.read_csv(path,names=columns)
        frame['year']=year
        pieces.append(frame)
    df=pd.concat(pieces,ignore_index=True) 
    #print(df)      #in order to check if it is right
    df7 = pd.DataFrame(columns = ["name", "num", "year"])
    for i in range(len(df)):
        for j in range(i+1,len(df)):
            if df.loc[i]['name']==df.loc[j]['name']:
                df7 = df7.append(df.loc[i], ignore_index=True)
    print(df7)

#8. 计算输出每个年份的男性5大常用名和女性5大常用名
def t8():
    print('please input the year you want, and you will get 5 most famous f or m names')
    goalyear=input()
    gy=int(goalyear)
    df8F=df[['name','gender','num','year']][(df['year']==gy)&(df['gender']=='F')]
    df8M=df[['name','gender','num','year']][(df['year']==gy)&(df['gender']=='M')]
    print(df8F.head(5))  
    print(df8M.head(5))

#9.封装调用
print('''
对1880-2010年美国婴儿名字的分析有以下功能可以调用：
2. 输入姓名、年份，输出该姓名在该年份的出生人数；
3. 输入姓名、开始年份和结束年份，绘制该姓名在各年份出生人数折线图；
4. 输入若干姓名、开始年份和结束年份，绘制这些姓名在对应年份区间的出生总人数的条状图；
5. 输入姓名、开始年份、结束年份、人口预期寿命，绘制该姓名在各年份生存人数折线图；
6. 输入姓名A、姓名B、开始年份和结束年份，计算姓名A与姓名B出生人数的相关系数；
7. 输入年份，计算哪些名字是男性和女性都取的，若没有输出None，若有请按照取名总人数进行排序；
8. 计算输出每个年份的男性5大常用名和女性5大常用名；
''')
print('输入ti表示要调用第i个功能')
def t():
    x=input()
    if x=='t2':
        t2()
    if x=='t3':
        t3()
    if x=='t4':
        t4()
    if x=='t5':
        t5()
    if x=='t6':
        t6() 
    if x=='t7':
        t7()
    if x=='t8':
        t8()
    else:
        t()
#t()
print(df)