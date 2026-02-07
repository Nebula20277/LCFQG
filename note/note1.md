#**DAY3-NOTE**

##**数据类型**

| **NUMERIC TYPES** |                                             |
| ----------------- | ------------------------------------------- |
| int               | 二进制(0b)/八进制(0o)/十六进制(0x)          |
| float             | 1.23e-4=0.000123;0.1 + 0.2 != 0.3           |
| bool              | 为int子类；and/or/not                       |
| complex           | 3+5j=complex（3,5）;conjugate()返回共轭复数 |



##**运算符**

算术运算符：+ - * /  //  %  **  @ (矩阵乘法)

比较运算符：==  !=  >  <  >=  <=

赋值运算符：=  +=  -=  *=  /=  //=  %=  **=

位运算符：&  |  ^  ~  <<  >>

成员运算符：in  not in

身份运算符：is  is not



##import math（cmath：复数）

abs(): 绝对值；pow(x, y): x 的 y 次幂；round(): 四舍五入



##**字符串**



###**创建**

r“字符串\n字符串”：取消转义（可用于路径表示）

f“字符串{变量}‘’：变量插入(字符串格式化）

u”字符串”：万能显示（任何字符均可如希腊字母）

b”字符串“：转为ASCII（改变其存储方式）



###**索引和切片**

s[index]: 获取单个字符

s[start​：end：​step]: 切片



###**大小写**

upper()  lower()  title()  

capitalize(): 首字母大写，其余均小写

swapcase(): 大小写互换



###**查找及其他**

find(想找的字符串,start,end): 从左往右找

rfind(): 从右往左找，可用于找最后一次出现

index()和rindex()类似于以上二者，但找不到时会报错

count(): 统计出现次数

replace(被替换的,替换的)

startswith(检查对象,start,end): 检查是否为指定开头，可同时检查多个可能的开头

endswith(检查对象,start,end): 检查是否为指定结尾



###**割裂及拼凑**

split(指定分隔符,分割次数): 从左往右

rsplit(指定分隔符,分割次数): 从右往左

splitlines(): 按换行符分割

连接符.join(连接对象): 连接字符串

partition(分隔符): 将字符串分隔成分隔符前，分隔符，分隔符后



###**对齐及判断**

isalpha()  isnumeric()  isalnum()  center(n,填充符)  ljust()  rjust()



##**列表** 



###**创建**

lst1 = []

lst2 = list()

lst3 = [1, 2, 3]

lst4 = list(range(10))

lst5 = [x**2 for x in range(5)]



###**操作**

lst[  ：：]: 切片

lst1+lst2：连接

lst*3：重复

lst.append(单个元素）：末尾添加

lst.extend(可迭代对象）：拓展

lst.insert(索引位置，要插入元素)：插入

lst.remove(要删除元素) ：删除第一个匹配项

lst.pop(索引) ：删除并返回指定位置元素

lst.clear()  ：清空所有元素

lst.index(要查找的元素，start，end)  ：查找索引

lst.count(要统计的元素) ：计数

lst.sort() ：排序（默认升序，reverse=True则为降序）

lst.reverse()  ：反转

lst.copy()   ：浅拷贝



##**字典**



###**创建**

dict1={不可变类型：任何类型，不可变类型：任何类型，...}

```python

#举例1

student = {
    "name": "张三",
    "age": 20,
    "major": "计算机科学",
    "grades": {"数学": 95, "英语": 88, "编程": 92}
}

print(student)


#举例2

flexible_dict = {
    "string": "Hello",           # 字符串
    "number": 42,                # 整数
    "list": [1, 2, 3],           # 列表
    "dict": {"key": "value"},    # 字典
    "function": len,             # 函数
    "none": None                 # None
}

print(flexible_dict)

```



###**操作**

访问：d[key],d.get(key）

赋值：d[key] = value

删除：del d[key], d.pop(key)

​d.popitem（）（返回一对键值对）

清空：d.clear()

更新：d.update(other_dict)

复制：d.copy()

获取：keys()  values()  items()



##**元组**



###**创建**

```python

t1 = ()

t2 = tuple()

t3 = (1,) (单个元素需要逗号)

t4 = (1, 2, 3)

t5 = 1, 2, 3 (括号可选)

t6 = tuple([1, 2, 3])

```



###**操作**

索引   切片   连接   重复   方法   

解包：

```python

# 普通元组解包 - 已知元素数量

person = ("张三", 25, "北京")

name, age, city = person  # 解包到三个变量

print(name)   # 张三

print(age)    # 25

print(city)   # 北京

# 必须数量匹配

# a, b = (1, 2, 3)  # ❌ 报错：太多值需要解包

# x, y, z = (1, 2)  # ❌ 报错：值不足


# 使用星号 * 收集剩余元素

numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers

print(first)   # 1

print(middle)  # [2, 3, 4] ← 注意：总是列表！

print(last)    # 5

# 星号位置灵活

*start, end = numbers

print(start)  # [1, 2, 3, 4]

print(end)    # 5

begin, *rest = numbers

print(begin)  # 1

print(rest)   # [2, 3, 4, 5]
```



##**集合**[元素唯一]



###**创建**

```python

s1 = set()

s2 = {1, 2, 3}

s3 = set([1, 2, 2, 3])  # 去重

s4 = {x for x in range(5)}  # 集合推导式

```



###**操作**

数学运算：

```python

- 并集：union() 或 |

- 交集：intersection() 或 &

- 差集：difference() 或 -

- 对称差集：symmetric_difference() 或 ^

举例：

# 创建集合

set1 = {1, 2, 3, 4, 5}

set2 = {4, 5, 6, 7, 8}

并集：

# 方法1：使用 | 运算符

union_set = set1 | set2

print("并集 | :", union_set)  # {1, 2, 3, 4, 5, 6, 7, 8}

# 方法2：使用 union() 方法

union_set = set1.union(set2)

print("并集 union():", union_set)  # {1, 2, 3, 4, 5, 6, 7, 8}

# 多个集合的并集

set3 = {8, 9, 10}

multi_union = set1 | set2 | set3

print("三个集合的并集:", multi_union)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# union() 也支持多个参数

multi_union = set1.union(set2, set3)

print("union()多参数:", multi_union)

交集：

# 方法1：使用 & 运算符

intersection_set = set1 & set2

print("交集 & :", intersection_set)  # {4, 5}

# 方法2：使用 intersection() 方法

intersection_set = set1.intersection(set2)

print("交集 intersection():", intersection_set)  # {4, 5}

# 多个集合的交集

set3 = {5, 6, 7}

multi_inter = set1 & set2 & set3

print("三个集合的交集:", multi_inter)  # {5}


差集（在A中但不在B中的元素）：

# 方法1：使用 - 运算符

diff_set = set1 - set2

print("差集 set1 - set2:", diff_set)  # {1, 2, 3}

diff_set = set2 - set1

print("差集 set2 - set1:", diff_set)  # {8, 6, 7}

# 方法2：使用 difference() 方法

diff_set = set1.difference(set2)

print("差集 difference():", diff_set)  # {1, 2, 3}


# 多个集合的差集

set3 = {3, 4}

multi_diff = set1 - set2 - set3

print("连续差集:", multi_diff)  # {1, 2}

# 注意：difference() 不支持连续操作，但支持多参数

multi_diff = set1.difference(set2, set3)

print("difference()多参数:", multi_diff)  # {1, 2}

对称差集（在A或B中，但不同时在两者中的元素）：

# 方法1：使用 ^ 运算符

sym_diff = set1 ^ set2

print("对称差集 ^ :", sym_diff)  # {1, 2, 3, 6, 7, 8}

# 方法2：使用 symmetric_difference() 方法

sym_diff = set1.symmetric_difference(set2)

print("对称差集 symmetric_difference():", sym_diff)  # {1, 2, 3, 6, 7, 8}

# 对称差集的理解：并集 - 交集

print("验证(并集-交集):", (set1 | set2) - (set1 & set2))  # {1, 2, 3, 6, 7, 8}

```

 frozenset(): 创建不可变集合


更新运算：

```python

举例：

# 创建两个集合

set1 = {1, 2, 3}

set2 = {3, 4, 5}

print("初始 set1:", set1)  # {1, 2, 3}

print("set2:", set2)       # {3, 4, 5}

# 方法1：使用 |= 运算符

set1 |= set2  # 相当于 set1 = set1 | set2，但更高效

print("set1 |= set2 后:", set1)  # {1, 2, 3, 4, 5}

# 重置

set1 = {1, 2, 3}

# 方法2：使用 update() 方法

set1.update(set2)

print("set1.update(set2) 后:", set1)  # {1, 2, 3, 4, 5}

# update() 支持多种可迭代对象

set1 = {1, 2, 3}

set1.update([4, 5, 6], {7, 8}, (9, 10))

print("update() 多参数后:", set1)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

&=或intersection_update()

-=或difference_update()

^=或symmetric_difference_update()

```



