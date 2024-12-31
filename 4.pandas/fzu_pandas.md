首先讲一下思路。

在第二轮的作业1，已经把需要用到的东西给爬下来了，那么我们现在对着作业一项项地往下看：

2. 统计通知人都有哪些，各占比例多少？

在进行爬取地时候，我并没有保存具体的名称，而是只保存了编号，如综合科是1035等。

因此在运行程序前，我写了一个字典来进行对应。

而统计这些很简单，如果不哟个pandas库，那么最简单的办法就是读取csv文件，然后提取agent列并且遍历，使用if语句。

然而这样太麻烦了，因此直接使用pandas库自带的value_counts函数，这个函数可以对当前列的数据进行统计，并且返回一个dataframe，格式大概是：

data1 counts1
data2 counts2

并且是按照counts进行排序的。

最后打印即可。

q2部分的代码运行如下：

```
q2
总通知数：4115
教学运行，代号1036，通知数：1616，占比39.27%
实践科，代号1039，通知数：937，占比22.77%
教研教改，代号1037，通知数：490，占比11.91%
综合科，代号1035，通知数：408，占比9.91%
质量办，代号1040，通知数：355，占比8.63%
计划科，代号1038，通知数：196，占比4.76%
教材中心，代号1152，通知数：69，占比1.68%
铜盘校区管理科，代号1042，通知数：44，占比1.07%

```

3. 分析附件下载次数与通知人是否有关系？若有，有什么联系？

这一问就不只是提取一个列了，而需要提取一个含有agent和附件下载次数的df。

提取这个df后，因为很多通知实际上并没有附件，所以我需要通过`agents["attachment_times"].notna()`将没有附件的行标记，然后再套一层agents将这些行给删除。

接下来我的思路是按照`agents_with_attachment_times` 进行分组，按照 `agent` 列进行分组。然后计算每个agent的 `attachment_times` 总和，即每个agent的附件下载总次数。`.sum()` 用于计算每个组的总和。`reset_index()` 则将结果的索引重新设置为默认的整数索引，并返回一个新的 DataFrame。

打印即可

q3运行结果：

```
q3
Total attachment downloads: 680564.0
综合科,code 1035, total downloads: 14934, percentage: 2.19%
教学运行,code 1036, total downloads: 140480, percentage: 20.64%
教研教改,code 1037, total downloads: 83994, percentage: 12.34%
计划科,code 1038, total downloads: 35089, percentage: 5.16%
实践科,code 1039, total downloads: 321573, percentage: 47.25%
质量办,code 1040, total downloads: 56600, percentage: 8.32%
铜盘校区管理科,code 1042, total downloads: 27894, percentage: 4.10%
```

- q4

也就是说，福州大学在每年的6月和9月发消息发的最多，也就是快开学和放函数假的时候

而在第52周，也就是每年接近年末的时候消息最多（单周）。每年在刚开学以及期末的时候通知最多，在学期中通知数正常且平缓，寒暑假则基本没有

在周二通知最多，实际上周一至周五差不多，周末的通知数远远不及周一至周五

![[5ae7078bdc97b5c79bfe67ccb5024673.png]]


```
按照月份统计：
date
1     262
2     195
3     385
4     449
5     425
6     510
7     144
8     202
9     510
10    286
11    318
12    429
Name: count, dtype: int64
按照周数统计：
week
1      93
2      74
3      59
4      37
5      14
6      14
7      55
8      77
9      81
10     73
11     92
12     90
13    103
14    100
15     87
16    115
17    106
18     76
19     89
20     92
21    116
22    121
23    124
24    111
25    108
26    125
27    102
28     37
29      4
30      4
31      5
32      1
33     10
34     96
35    122
36    127
37    127
38    103
39    107
40     36
41     68
42     74
43     71
44     80
45     84
46     66
47     73
48     72
49     92
50     69
51     97
52    136
53     20
Name: count, dtype: Int64
按照星期统计：
date
0    762
1    765
2    819
3    681
4    783
5    155
6    150
Name: count, dtype: int64
```

最后的代码如下：

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

def q2(agents,fzu_department):
    print("q2")

    long=len(agents)

    print(f"总通知数：{long}")

    counts=agents.value_counts()

    for code,count in counts.items():
        name=fzu_department[code]
        percentage=count/long*100
        print(f"{name}，代号{code}，通知数：{count}，占比{percentage:.2f}%")

    print()


def q3(agents, fzu_department):
    print("q3")

    agents_with_attachment_times = agents[agents["attachment_times"].notna()]

    result = agents_with_attachment_times.groupby('agent')['attachment_times'].sum().reset_index()

    total_attachments = result['attachment_times'].sum()

    print(f"Total attachment downloads: {total_attachments}")

    names = []
    times = []
    percentages = []

    for index, row in result.iterrows():
        code = row['agent']
        time = row['attachment_times']

        name = fzu_department[code]

        percentage = time/total_attachments * 100
        print(f"{name},code {int(code)}, total downloads: {int(time)}, percentage: {percentage:.2f}%")

        names.append(f"{name} ({int(code)})")
        times.append(int(time))
        percentages.append(percentage)

    print()

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.barh(names, times, color='skyblue')

    for bar, percentage in zip(bars, percentages):
        ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{percentage:.2f}%', va='center', ha='left', fontsize=10)

    ax.set_title("Attachment Downloads and Percentages by Agent", fontsize=16)
    ax.set_xlabel("Total Attachment Downloads", fontsize=12)
    ax.set_ylabel("Agents", fontsize=12)

    plt.tight_layout()
    plt.show()


def q4(agents):
    # 转换为日期并移除非法值
    dates=pd.to_datetime(agents, errors='coerce')
    df_cleaned = dates.dropna()

    # 按月份统计
    months=df_cleaned.dt.month
    month_counts=months.value_counts().sort_index()
    print("按照月份统计：")
    print(month_counts)

    # 按周数统计
    weeks=df_cleaned.dt.isocalendar().week
    week_counts=weeks.value_counts().sort_index()
    print("按照周数统计：")
    print(week_counts)

    # 按星期统计
    weekdays=df_cleaned.dt.dayofweek
    weekday_counts=weekdays.value_counts().sort_index()
    print("按照星期统计：")
    print(weekday_counts)

    # 可视化
    fig,axs=plt.subplots(3, 1, figsize=(12, 18))

    # 按月份统计
    axs[0].bar(month_counts.index, month_counts.values, color='skyblue')
    axs[0].set_title("Count by Month")
    axs[0].set_xlabel("Month")
    axs[0].set_ylabel("Count")
    axs[0].grid()

    # 按周数统计
    axs[1].bar(week_counts.index, week_counts.values, color='lightgreen')
    axs[1].set_title("Count by Week")
    axs[1].set_xlabel("Week")
    axs[1].set_ylabel("Count")
    axs[1].grid()

    # 按星期统计
    axs[2].bar(weekday_counts.index, weekday_counts.values, color='lightcoral')
    axs[2].set_title("Count by Weekday")
    axs[2].set_xlabel("Weekday (0=Monday, 6=Sunday)")
    axs[2].set_ylabel("Count")
    axs[2].grid()

    plt.tight_layout()
    plt.show()

    print()

if __name__=="__main__":
    fzu_department = {
        1035: '综合科',
        1036: '教学运行',
        1037: '教研教改',
        1038: '计划科',
        1039: '实践科',
        1040: '质量办',
        1152: '教材中心',
        1042: '铜盘校区管理科'
    }

    fzu_edu=pd.read_csv("fzu_edu.csv")

    q2(fzu_edu["agent"],fzu_department)
    q3(fzu_edu[["agent","attachment_times"]],fzu_department)
    q4(fzu_edu["date"])
```




运行结果：

```
q2
总通知数：4115
教学运行，代号1036，通知数：1616，占比39.27%
实践科，代号1039，通知数：937，占比22.77%
教研教改，代号1037，通知数：490，占比11.91%
综合科，代号1035，通知数：408，占比9.91%
质量办，代号1040，通知数：355，占比8.63%
计划科，代号1038，通知数：196，占比4.76%
教材中心，代号1152，通知数：69，占比1.68%
铜盘校区管理科，代号1042，通知数：44，占比1.07%

q3
Total attachment downloads: 680564.0
综合科,code 1035, total downloads: 14934, percentage: 2.19%
教学运行,code 1036, total downloads: 140480, percentage: 20.64%
教研教改,code 1037, total downloads: 83994, percentage: 12.34%
计划科,code 1038, total downloads: 35089, percentage: 5.16%
实践科,code 1039, total downloads: 321573, percentage: 47.25%
质量办,code 1040, total downloads: 56600, percentage: 8.32%
铜盘校区管理科,code 1042, total downloads: 27894, percentage: 4.10%

q4
按照月份统计：
date
1     262
2     195
3     385
4     449
5     425
6     510
7     144
8     202
9     510
10    286
11    318
12    429
Name: count, dtype: int64
按照周数统计：
week
1      93
2      74
3      59
4      37
5      14
6      14
7      55
8      77
9      81
10     73
11     92
12     90
13    103
14    100
15     87
16    115
17    106
18     76
19     89
20     92
21    116
22    121
23    124
24    111
25    108
26    125
27    102
28     37
29      4
30      4
31      5
32      1
33     10
34     96
35    122
36    127
37    127
38    103
39    107
40     36
41     68
42     74
43     71
44     80
45     84
46     66
47     73
48     72
49     92
50     69
51     97
52    136
53     20
Name: count, dtype: Int64
按照星期统计：
date
0    762
1    765
2    819
3    681
4    783
5    155
6    150
Name: count, dtype: int64

```
![[4390af87133ec19dce543a72d0167ac0.png]]
![[5ae7078bdc97b5c79bfe67ccb5024673.png]]