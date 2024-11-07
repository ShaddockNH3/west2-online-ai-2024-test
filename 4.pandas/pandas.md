- 数据科学基本工具学习
    
    - Pandas的学习
        - 数据读取与写入
        - 数据清洗
        - 数据筛选与索引
        - 数据的处理与变换
        - (optional) 数据可视化（matplotlib、plotly、pyecharts、···）


https://pandas.pydata.org/docs/getting_started/index.html#getting-started

### 1. pandas处理哪些类型的数据

#### 1.1 最开始

`import pandas as pd`

pandas数据表实际上就相当于excel表，行为`row`，列为`column`每个行和列的上方还有数据对应的性质。

如图：

![[pandas_1.png]]
在手动存储数据时，需要创建一个DataFrame。使用python列表字典，字典的键将作为列标题，每个列表中的值将用作DataFrame的列。

意思就是说，DataFrame本质上就是一个字典，而值则是一个列表。

一个最基本的实现，存储泰坦尼克号的乘客数据，想知道姓名，年龄，和性别，存储代码如下：

```
import pandas as pd  
  
df=pd.DataFrame(  
    {  
        "Name":[  
            "Braund, Mr. Owen Harris",  
            "Allen, Mr. William Henry",  
            "Bonnell, Miss. Elizabeth",  
        ],  
        "Age":[22,35,58],  
        "Sex":["male","male","fmale"],  
    }  
)  
  
print(df)
```

输出：

```
                       Name  Age    Sex
0   Braund, Mr. Owen Harris   22   male
1  Allen, Mr. William Henry   35   male
2  Bonnell, Miss. Elizabeth   58  fmale
```

#### 1.2 `DataFrame` 中的每一列都是一个 `Series`

选择这个列的过程和字典的处理过程类似

```
import pandas as pd  
  
df=pd.DataFrame(  
    {  
        "Name":[  
            "Braund, Mr. Owen Harris",  
            "Allen, Mr. William Henry",  
            "Bonnell, Miss. Elizabeth",  
        ],  
        "Age":[22,35,58],  
        "Sex":["male","male","fmale"],  
    }  
)  
  
print(df["Age"])
```

输出：

```
0    22
1    35
2    58
Name: Age, dtype: int64
```

也可以从零开始建造一个单列，代码如下：

```
import pandas as pd  
  
ages=pd.Series([22,35,58],name="Age")  
  
print(ages)
```

输出：

```
0    22
1    35
2    58
Name: Age, dtype: int64
```

#### 1.3 对 DataFrame 或 Series[](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html#do-something-with-a-dataframe-or-series "Link to this heading") 执行某些操作

求最值，即类比于内置数据结构的操作。

`df["Age"].max()`即可，对于Series同理。

pandas库内置了一些基本的分析，如计数，均值(mean)，标准差(std)，具体实现如下：

`df.describe()`

此后其自动就会输出所有和数字相关的分析，输出如下：

```
             Age
count   3.000000
mean   38.333333
std    18.230012
min    22.000000
25%    28.500000
50%    35.000000
75%    46.500000
max    58.000000
```

而name和sex与数据无关，所以并不考虑。

简单总结一下，pandas库与excel表格很相似，并且支持pandas库支持再电子表格软件中进行数据操作和计算。~~与numpy，matplotlib配合使用，是用来数学建模的好东西~~

最后是文档中提供的注意事项：

1. 导入包
2. 数据表存储为DataFrame
3. 每一个列都是一个Series
4. 可以将方法应用于DataFrame或Series操作

### 2.如何读取和写入表格？

#### 2.1

现场随便编一个表格如下：

|     | Number   | Name     | Chinese | Math | English |
| --- | -------- | -------- | ------- | ---- | ------- |
| 1   | 22302217 | Williams | 64      | 25   | 84      |
| 2   | 114514   | Bob      | 31      | 36   | 47      |
| 3   | 1314520  | Tom      | 52      | 78   | 67      |
| 4   | 10086    | Alice    | 75      | 42   | 241     |
| 5   | 8848     | Pokemon  | 843     | 78   | 24      |
| 6   | 721      | AAA      | 36      | 23   | 13      |
| 7   | 330199   | Charlie  | 62      | 55   | 74      |
| 8   | 4488233  | David    | 90      | 45   | 56      |
| 9   | 5201314  | Eve      | 72      | 88   | 65      |
| 10  | 666666   | Frank    | 48      | 92   | 53      |
| 11  | 99999    | Grace    | 58      | 33   | 29      |
| 12  | 1357924  | Hannah   | 42      | 69   | 81      |
| 13  | 2468135  | Ian      | 34      | 56   | 72      |
| 14  | 789456   | Julia    | 95      | 61   | 49      |
| 15  | 147258   | Kevin    | 80      | 74   | 36      |
| 16  | 987654   | Laura    | 63      | 80   | 70      |
| 17  | 321123   | Mike     | 55      | 68   | 42      |
| 18  | 456789   | Nancy    | 84      | 52   | 91      |
| 19  | 741852   | Oliver   | 39      | 83   | 27      |
| 20  | 369258   | Peter    | 78      | 49   | 88      |
| 21  | 258369   | Quinn    | 91      | 46   | 76      |
| 22  | 753951   | Ruby     | 45      | 72   | 64      |
| 23  | 852741   | Steve    | 59      | 37   | 59      |
| 24  | 159357   | Tina     | 71      | 82   | 85      |
| 25  | 951753   | Uma      | 66      | 29   | 48      |
| 26  | 135531   | Victor   | 40      | 90   | 58      |

代码如下：

```
import pandas as pd  
  
grades=pd.read_excel("2.1grade.xlsx")  
  
print(grades)
```

上述代码文件和excel文件放入了同一个文件夹，并且是直接输出了所有的数据：

```
    List    Number      Name  Chinese  Math  English
0      1  22302217  Williams       64    25       84
1      2    114514       Bob       31    36       47
2      3   1314520       Tom       52    78       67
3      4     10086     Alice       75    42      241
4      5      8848   Pokemon      843    78       24
5      6       721       AAA       36    23       13
6      7    330199   Charlie       62    55       74
7      8   4488233     David       90    45       56
8      9   5201314       Eve       72    88       65
9     10    666666     Frank       48    92       53
10    11     99999     Grace       58    33       29
11    12   1357924    Hannah       42    69       81
12    13   2468135       Ian       34    56       72
13    14    789456     Julia       95    61       49
14    15    147258     Kevin       80    74       36
15    16    987654     Laura       63    80       70
16    17    321123      Mike       55    68       42
17    18    456789     Nancy       84    52       91
18    19    741852    Oliver       39    83       27
19    20    369258     Peter       78    49       88
20    21    258369     Quinn       91    46       76
21    22    753951      Ruby       45    72       64
22    23    852741     Steve       59    37       59
23    24    159357      Tina       71    82       85
24    25    951753       Uma       66    29       48
25    26    135531    Victor       40    90       58
```

而如果应用`print(grades.head())`，默认会输出前五行，如果在head内有数字n，那么就会输出前n行

如果对后面的数据感兴趣，那么使用`print(grades.tail())`即可输出后n行

可以使用dtype来看pandas如何解释每种列数据类型：

`print(grades.tail().dtypes)`

输出最后五行的数据类型（其实和源数据是一样的）

```
List        int64
Number      int64
Name       object
Chinese     int64
Math        int64
English     int64
dtype: object
```

这里需要提及一个概念，属性与方法。dtypes是DataFrame的属性，而max等是DataFrame的方法，属性不需要+()，而方法需要加

#### 2.2 现在可以通过pandas库导出数据，变成一个表格。

如将tatantic的数据导出到一个excel里，并且给他命名，代码如下：

```
import pandas as pd  
  
df = pd.DataFrame(  
    {  
        "Name": [  
            "Braund, Mr. Owen Harris",  
            "Allen, Mr. William Henry",  
            "Bonnell, Miss. Elizabeth",  
        ],  
        "Age": [22, 35, 58],  
        "Sex": ["male", "male", "fmale"],  
    }  
)  
  
df.to_excel("2.2tatanic.xlsx",sheet_name="Hello World",index=False)
```

现在文件夹里多了一个名为`2.2tatanic.xlsx`的文件，打开看看。

![[pandas_2.png]]

此时可以通过read来访问这个文件。

#### 2.3 摘要

通过info实现

```
import pandas as pd  
  
grades=pd.read_excel("2.1grade.xlsx")  
  
print(grades.info())
```

输出：

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 26 entries, 0 to 25
Data columns (total 6 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   List     26 non-null     int64 
 1   Number   26 non-null     int64 
 2   Name     26 non-null     object
 3   Chinese  26 non-null     int64 
 4   Math     26 non-null     int64 
 5   English  26 non-null     int64 
dtypes: int64(5), object(1)
memory usage: 1.3+ KB
None
```

### 3.如何选择DataFrame的子集

#### 3.1 选择特定列

这一块主要是对选择和形状的选择，shape是DataFrame里的一个属性，所以在调用的时候不需要使用括号。

这里只需要注意，选择单列数据的时候代码如下：

`test=df["Age"]`

而选择多列的时候则是：

`test=df[["Age","Sex","..."]]`

单列则是使用一对方括号，多列则是使用方括号还得框住列表名称列表。

而shape则是表示df的形状，为df的属性。df是二维的，包含行和列。

对于选择的单列，其数据类型本质是列；而对于选择了多列的而言，其数据类型本质上是一个df

#### 3.2 过滤特定行

比如说现在我只关心大于35岁的乘客，那么只需要：

`test=df[df["Age"]>35]`

此时就会返回一个大于35岁的DataFrame，并赋予给test。也就是说，如果对于行来进行操作的话，即在[]内使用条件即可筛选。

如果直接输出`df["Age"]>35`，那么则会输出一个bool列

其他的表达式同样适用。

--

如果想要筛选特定数据的话，比如说筛选年龄等于35或等于34的乘客，则可以采用`isin()`代码，具体如下：

`test=df[df["Age".isin(34,35)]]`

事实上代码等效为：

`test=df[(df["Age"]==34) | (df["Age"]==35)]`

贴一个Note：

组合多个条件语句时，每个条件必须用括号 `（）` 括起来。此外，您不能使用 `or`/`and`，但需要使用 `or` 运算符 `|`和 `and` 运算符 `&`。

--

如果想使用非空的数据，则使用`notna()`

notna()为条件函数，对非Null值得每一行返回True

#### 3.3 如何一次性选择特定的行和列？

比如说，现在我们对2.1中的成绩做一个分析，我现在想筛选出语文大于60分（行），同时将数学和英语两栏去掉（列），那么应该如何实现？

只需要结合上述的东西，并使用一个新的函数`loc/iloc`

```
import pandas as pd  
  
grade=pd.read_excel("2.1grade.xlsx")  
  
test=grade.loc[grade["Chinese"]>60,["List","Number","Name","Chinese"]]  
  
print(test)
```

一次性产生子集如下：

``` 
    List    Number      Name  Chinese
0      1  22302217  Williams       64
3      4     10086     Alice       75
4      5      8848   Pokemon      843
6      7    330199   Charlie       62
7      8   4488233     David       90
8      9   5201314       Eve       72
13    14    789456     Julia       95
14    15    147258     Kevin       80
15    16    987654     Laura       63
17    18    456789     Nancy       84
19    20    369258     Peter       78
20    21    258369     Quinn       91
23    24    159357      Tina       71
24    25    951753       Uma       66
```

亦可使用类似列表的切片：

```
import pandas as pd  
  
grade=pd.read_excel("2.1grade.xlsx")  
  
test=grade.iloc[1:3,2:4]  
  
print(test)
```

前者使用loc，后者使用iloc

同时，可对所选择的数据分配新值，这就是直接在原DataFrame上进行操作：

```
import pandas as pd  
  
grade=pd.read_excel("2.1grade.xlsx")  
  
grade.loc[grade["Chinese"]>60,["List","Number","Name","Chinese"]]=0  
  
print(grade)
```

输出：

```
    List   Number    Name  Chinese  Math  English
0      0        0       0        0    25       84
1      2   114514     Bob       31    36       47
2      3  1314520     Tom       52    78       67
3      0        0       0        0    42      241
4      0        0       0        0    78       24
5      6      721     AAA       36    23       13
6      0        0       0        0    55       74
7      0        0       0        0    45       56
8      0        0       0        0    88       65
9     10   666666   Frank       48    92       53
10    11    99999   Grace       58    33       29
11    12  1357924  Hannah       42    69       81
12    13  2468135     Ian       34    56       72
13     0        0       0        0    61       49
14     0        0       0        0    74       36
15     0        0       0        0    80       70
16    17   321123    Mike       55    68       42
17     0        0       0        0    52       91
18    19   741852  Oliver       39    83       27
19     0        0       0        0    49       88
20     0        0       0        0    46       76
21    22   753951    Ruby       45    72       64
22    23   852741   Steve       59    37       59
23     0        0       0        0    82       85
24     0        0       0        0    29       48
25    26   135531  Victor       40    90       58
```

贴一个note：

- When selecting subsets of data, square brackets `[]` are used.  
    选择数据子集时，使用方括号 `[]。`
    
- Inside these brackets, you can use a single column/row label, a list of column/row labels, a slice of labels, a conditional expression or a colon.  
    在这些括号内，您可以使用单个列/行标签、列/行标签列表、标签切片、条件表达式或冒号。
    
- Select specific rows and/or columns using `loc` when using the row and column names.  
    使用行和列名称时，使用 `loc` 选择特定行和/或列。
    
- Select specific rows and/or columns using `iloc` when using the positions in the table.  
    使用表中的位置时，使用 `iloc` 选择特定的行和/或列。
    
- You can assign new values to a selection based on `loc`/`iloc`.  
    您可以根据 `loc`/`iloc` 为选择指定新值。

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

### 5. 如何从现有列派生新的列？

