import matplotlib.pyplot as plt
import numpy as np


ax = plt.axes(projection = '3d') #建立一個3D圖檔
plt.rcParams['font.sans-serif'] = [u'MingLiu'] #細明體
plt.rcParams['axes.unicode_minus'] = False #設定中文
ax.set_title('等高線圖')
x = np.linspace(-6,6,30)
y = np.linspace(-5,5,30)
X,Y = np.meshgrid(x,y) #網格生成
def f(x,y):
    return x**2+y**2
Z = f(X,Y)
# print(x)
# print(x.shape,y.shape,Z.shape) #資料形狀(資料量) 只有Array的資料類型才能用這個
# ax.contour(X,Y,Z,50,cmap='binary') #3D等高線圖
# ax.plot_wireframe(X,Y,Z,color = 'blue') #3D網格圖
ax.plot_surface(X,Y,Z,cmap = 'rainbow') #3D曲面圖
ax.set_xlabel("X",color='red')
ax.set_ylabel("Y",color='red')
ax.set_zlabel("Z",color='blue')
ax.view_init(elev = 45 , azim = 0) #起始角度：elev=伏角 , azim = 方向角
ax.dist=5 #起始距離(與座標系統)
plt.show()