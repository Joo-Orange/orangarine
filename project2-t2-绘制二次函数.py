#matplotlib绘制函数f(x)=x^2+2x+1在区间x∈[-5,5]的函数图像
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5,100)
y = (x+1)**2
plt.plot(x,y)
plt.show()