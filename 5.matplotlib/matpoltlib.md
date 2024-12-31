from pandas
### 4. 如何绘图？

借助matplotlib.pyplot来绘图

首先需要使用`.plot`预备，随后使用`plt.show()`直接呈现，代码如下：

```
import pandas as pd  
import matplotlib.pyplot as plt  
  
test=pd.read_excel("2.1grade.xlsx",index_col=0,parse_dates=True)  
test[["Chinese","Math","English"]].plot()  
plt.show()
```

输出（在这里调整了不合理的数据，超过100的）：

![[pandas_3.png]]

~~丑陋的折线图~~

使用dataframe，pandas会默认为包含数值的每一列创建一个折线图，先进行plot，随后plt.show()

plot时默认采用的是折线图。

如果想采用散点图来队医语文和英语的成绩，那么可以表示如下：

```
import pandas as pd  
import matplotlib.pyplot as plt  
  
test=pd.read_excel("2.1grade.xlsx",index_col=0,parse_dates=True)  
test.plot.scatter(x="Chinese",y="English",alpha=0.5)  
plt.show()
```

alpha是表示颜色深浅的，越接近1越深，反之，靠近0则变浅。

![[pandas_4.png]]

上述是分析相关性的图，因为我的数据是乱输的，很显然，学生的英语成绩和语文成绩在我的数据里没有必然联系。

---

### 1.1

