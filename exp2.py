import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
x=np.linspace(0,10,1000)
y=np.cos(x)
z=np.sin(x)
plt.plot(x, y, 'k', label="$cosx$", color='r', \
         linewidth=3, linestyle="-")
plt.yticks([-1,0,1])
ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
plt.plot(x, z, "b--", label="$sinx$", linewidth=1)
plt.title("正余弦函数图像绘制")
plt.legend()
plt.show()
