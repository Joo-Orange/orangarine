#实验四-基于协同过滤算法的电影推荐
'''
实验要求：
1. 读取MoviesLens1M数据，存储为Pandas的DataFrame；
2. 将DataFrame数据改为自己代码所需要的结构；
3. 学习协同过滤算法，写出协同过滤算法相应的函数；
4. 输入两个用户，输出两个用户公共电影的评分；
5. 输入两个用户，计算出用户偏好的相似度；
6. 输入一位用户，输出与指定用户相似度最高的5位用户；
7. 输入一位用户，输出输出推荐电影；
8. 程序界面请自行设计，命令行、GUI、网页、手机App均可。
'''

import pandas as pd

# 数据读取和处理，合并在一个大的dataframe
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv('C:\\Users\\admin\\Desktop\\程序设计实验报告-4\\ml_1m\\ml_1m\\ratings.dat', \
                      sep='::', header=None, names=rnames,
                        usecols = [0,1,2],engine= 'python')
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_csv('C:\\Users\\admin\Desktop\\程序设计实验报告-4\\ml_1m\\ml_1m\\movies.dat', \
                     sep='::', header=None, names=mnames,
                        usecols = [0,1],engine= 'python')
data = pd.merge(ratings, movies)
global df
# 转换成User-Item矩阵
df = ratings.pivot(index='user_id', columns='movie_id', values='rating')


# 以下是公用函数
# 构建共同的评分向量
def build_xy(user_id1, user_id2):
        bool_array = df.loc[user_id1].notnull() & df.loc[user_id2].notnull()
        return df.loc[user_id1, bool_array], df.loc[user_id2, bool_array]

# 余弦相似度
def cosine(user_id1, user_id2):
        x, y = build_xy(user_id1, user_id2)
        # 分母
        denominator = (sum(x*x)*sum(y*y))**0.5
        try:
            value = sum(x*y)/denominator
        except ZeroDivisionError:
            value = 0
        return value

# 计算最近的邻居
def computeNearestNeighbor(user_id, metric='cosine', k=5):
        """
        metric: 度量函数
        k:      返回k个邻居
        返回：pd.Series，其中index是邻居名称，values是距离
        """
        return df.drop(user_id).index.to_series().apply(cosine, args=(user_id,)).nlargest(k)

# 向给定用户推荐（返回：pd.Series）
def recommend(user_id):
    # 找到距离最近的用户id
    nearest_user_id = computeNearestNeighbor(user_id, metric='cosine').index[0]
    print('最近邻用户id：' + str(nearest_user_id))
    # 找出邻居评价过、但自己未曾评价的乐队（或商品）
    # 结果：index是商品名称，values是评分
    recommendList = df.loc[nearest_user_id, df.loc[user_id].isnull() & \
                           df.loc[nearest_user_id].notnull()].sort_values()
    print(recommendList)
    return recommendList


# 下面进行实验要求功能的实现
# 1.输入两个用户，输出两个用户公共电影的评分；
def t1():
    print('please input 2 users id:')
    x=int(input())
    y=int(input())
    print(build_xy(x,y))

# 2.输入两个用户，计算出用户偏好的相似度；
def t2():
    print('please input 2 users`id and get the degree of similarity')
    x=int(input())
    y=int(input())
    print(cosine(x,y))
    
# 3.输入一位用户，输出与指定用户相似度最高的5位用户； 
def t3():
    print('please input a usee`s id and get 5 other most similar users` id')
    x=int(input())
    print(computeNearestNeighbor(x))

# 4.输入一位用户，输出输出推荐电影；
def t4():
    print('please input id and get the recommended movies~ ')
    x=int(input())
    print(recommend(x))
    

#封装调用    
print('''
基于协同过滤算法的电影推荐有以下功能：
1. 输入两个用户，输出两个用户公共电影的评分；
2. 输入两个用户，计算出用户偏好的相似度；
3. 输入一位用户，输出与指定用户相似度最高的5位用户；
4. 输入一位用户，输出输出推荐电影；
输入‘i’表示调用第i个功能。
''')
def t():
    i=int(input())
    if i==1:
        t1()
    if i==2:
        t2()
    if i==3:
        t3()
    if i==4:
        t4()
    else:
        print('重新输入i可再次调用')
        t()
t()