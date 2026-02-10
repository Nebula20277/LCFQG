# DAY8-NOTE

## pandas

是什么？

pandas 是 Python 里专门用来处理表格数据的库，能快速读取、清洗、分析数据，是数据科学的必备工具。

### Series

```python

import pandas as pd

# 创建一个 Series：数据是 [10, 20, 30]，标签是 ['a', 'b', 'c']

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

print(s)

a    10

b    20

c    30

dtype: int64

```

### DataFrame

```python

# 创建一个 DataFrame：两列，三行

df = pd.DataFrame({

    '姓名': ['张三', '李四', '王五'],

    '年龄': [20, 21, 22]

})

print(df)

输出：

   姓名  年龄

0  张三  20

1  李四  21

2  王五  22

```

看前几行：df.head()

看数据信息：df.info()（列名、类型、非空值数量）

看统计摘要：df.describe()（均值、最大最小等）

### 数据读写

#### 读取数据

-CSV 文件

```python

# 读取 CSV 文件

df = pd.read_csv('data.csv')

```

-Excel 文件

```python

# 读取 Excel 文件

df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

```

#### 写入数据

```python

# 保存，index=False 表示不保存行索引

df.to_csv('output.csv', index=False)

```

### 数据清洗

1.缺失值

即指数据里的空值(NaN)

```python

#统计每列缺失值数量

df.isnull().sum()

#处理方法

（1）删除一整行

df.dropna()

（2）替换

df.fillna(0)

df.fillna(df['年龄'].mean())

...
```

2.重复值

即完全相同的两行

```python

#统计重复行数

df.duplicated().sum()

#处理方法

df.drop_duplicates()

```
3.数据类型转换

举例：（将年龄转为整数型）

df['年龄']=df['年龄'].astype('int')

4.字符串清洗

df[]=df[].str.strip()

df[]=df[].str.replace('被替换的','替换成')

5. 数据筛选

即从表里 “挑” 出想要的行

按列选：

-选一列：df['姓名']             #返回一个 Series

-选多列：df[['姓名', '年龄']]   #返回一个 DataFrame

按行选：

df.iloc[0:2]

df[df['年龄']>20]

6. 数据统计与分组

df[].sum()

df[].mean()

df[].max()

df[].min()

df.groupby()[].mean()

## matplotlib

matplotlib 是 Python 里最基础的绘图库，能画出各种图表（折线、条形、散点等），把数据变成直观的图。

绘图的 “标准流程”：

```python

import matplotlib.pyplot as plt

# 1. 创建画布和子图（相当于准备一张纸）

fig, ax = plt.subplots(figsize=(8, 6))  # 8x6 英寸的图

# 2. 画图形（在纸上画画）

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 25, 30]

ax.plot(x, y)  # 画折线图

# 3. 设置标签和标题（给图加说明）

ax.set_title('示例折线图')

ax.set_xlabel('X轴')

ax.set_ylabel('Y轴')

# 4. 显示图形

plt.show()

```

折线图：ax.plot(x,y,linestyle='--',marker='o',color='red')

散点图：ax.scatter(x,y,c='blue',s=50)

条形图：

catagories=['A class','B class','C class']

scores=[87,85,93]

ax.bar(catagories,scores,color='green')

饼图：

sizes=[30,45,25]

labels=['A','B','C']

ax.pie(sizes,labels=labels,autopct='%1.1f%%')

直方图：

data = [60, 70, 75, 80, 85, 90, 95]

ax.hist(data, bins=5, edgecolor='black') 

图形美化：

-颜色：color='red' 或 color='#FF5733'（十六进制颜色）

-图例：ax.legend(['系列1', '系列2'])（当图里有多个系列时）

-网格：ax.grid(True, linestyle='--', alpha=0.7)（加网格线，更清晰）

-保存图片：plt.savefig('plot.png', dpi=300)（保存为高清图片）
