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
    print("q4")
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
    
def q5(agents):
    print("q5")
    print("q5是基于时间与下载次数关系之间的分析，最终的出来是一张图")

    df=pd.DataFrame(agents)

    df['date']=pd.to_datetime(df['date'])
    df_grouped=df.groupby('date').agg({'attachment_times': 'sum'}).reset_index()

    plt.figure(figsize=(10, 6))
    plt.scatter(df_grouped['date'], df_grouped['attachment_times'], color='blue', label='下载次数')

    plt.title('附件下载次数与日期的关系', fontsize=16)
    plt.xlabel('日期', fontsize=12)
    plt.ylabel('下载次数', fontsize=12)

    plt.xticks(rotation=45)

    plt.grid(True)

    plt.tight_layout()
    plt.show()

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

    a=int(input("请输入一个数字（从2到5中选择一个）："))

    if a==2:
        q2(fzu_edu["agent"],fzu_department)
    elif a==3:
        q3(fzu_edu[["agent","attachment_times"]],fzu_department)
    elif a==4:
        q4(fzu_edu["date"])
    elif a==5:
        q5(fzu_edu[["date","attachment_times"]])
    else:
        print("输入无效，程序结束")

    print()
    input("输入任意结束")