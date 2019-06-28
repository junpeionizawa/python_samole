import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.01) #0から6まで0.2刻みで生成
y = np.sin(x)
plt.plot(x,y)
plt.show()




import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.01) #0から6まで0.2刻みで生成
y1 = np.sin(x)
y2 = np.cos(x)
#グラフの描画
plt.plot(x,y1,label = "sin")
plt.plot(x,y2, linestyle = "--",label = "cos")
plt.xlabel("x") #x軸のラベル
plt.ylabel("y") #y軸のラベル
plt.title('sin  & cos') #タイトル
plt.legend()
plt.show()

#ステップ関数
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
	return np.array(x > 0,dtype = np.int)
#-5.0から5.0までの範囲を,0.1刻みで配列を生成　
x = np.arange(-5.0,5.0,0.1)
#配列を引数にとり、ステップ関数を実行して配列に返す
y = step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)#y軸の範囲を指定
plt.show()