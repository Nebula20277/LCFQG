# DAY4-NOTE

## try-expect异常捕获机制

直接用代码例子更清晰吧：

举例：

try:

    # 尝试执行的代码（危险区域）
    
    file = open("data.txt", "r")
    
    content = file.read()
    
    number = int(content)
    
except FileNotFoundError:

    # 处理文件不存在的异常
    
    print("文件不存在！")
    
except ValueError:

    # 处理值转换错误
    
    print("文件内容不是有效数字！")
    
except Exception as e:

    # 捕获所有其他异常（兜底）
    
    print(f"发生未知错误：{e}")
    
else:

    # 只有当try块没有异常时才执行
    
    print("文件读取成功！")
    
finally:

    # 无论是否发生异常，都会执行（清理工作）
    
    print("程序执行结束")
    
    # 通常用于关闭文件、释放资源等
    
### 常见异常类型

ZeroDivisionError  ValueError  TypeError  IndexError  KeyError  FileNoteFoundError

## for循环

## while循环

## if-elif-else

## 列表推导式

[表达式 for 变量 in 可迭代对象 if 条件]

##匿名函数 lambda

lambda 参数1, 参数2, ...: 表达式

 ↑ 没有函数名    ↑ 自动返回表达式结果

举例1：

对列表按字符串长度排序

words = ["apple", "kiwi", "banana", "pear"]

words.sort(key=lambda word: len(word))

 ['kiwi', 'pear', 'apple', 'banana']
 
## 高阶函数 map filter

高阶函数：接受函数作为参数，==或==返回函数的函数

### map()函数

map(函数, 可迭代对象)  # 返回map对象（可转换为列表）

作用：将函数应用到序列的每个元素

举例1：

创建一个列表

numbers = [1, 2, 3, 4, 5]
 
使用map将每个数字平方

squared = map(lambda x: x**2, numbers)

print("map对象:", squared)         # <map object at 0x...>输出map的内存地址，但每次运行结果都不一样

print("类型:", type(squared))      # <class 'map'>

map对象是迭代器，需要转换为列表查看（惰性求值的特性）

print("平方结果:", list(squared))  # [1, 4, 9, 16, 25]

注意：map对象只能遍历一次！

print("再次遍历:", list(squared)) # [] ← 空了！ 

### filter()函数

filter(函数, 可迭代对象)  # 返回filter对象

作用：筛选出满足条件的元素

举例1：

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

过滤偶数

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print("filter对象:", even_numbers)  # <filter object at 0x...>

print("偶数:", list(even_numbers))   # [2, 4, 6, 8, 10]

过滤大于5的数

greater_than_5 = filter(lambda x: x > 5, numbers)

print("大于5的数:", list(greater_than_5))  # [6, 7, 8, 9, 10]

#和map（）一样具有惰性求值的特性，且只能遍历一次

## 数据清洗核心技能re（regular expression）

### WHAT & HOW

在python无需额外pip，只需：

import re

re,中文叫“正则表达式”，即正则表达式是一组由字母和符号组成的特殊文本，它可以用来从文本中找出满足你想要的格式的句子，其主要有四个函数：

1. re.findall() 找出所有匹配内容

2. re.sub() 替换/清洗脏字符

3. re.match() 从头匹配

4. re.search() 找任意位置的第一个匹配

re模块常用函数返回值为list[]，找不到则返回空列表[]

须记住：

 \d  ： 单个半角数字（0-9），比如匹配  5 ，不匹配  a  或  你 

 \d+  ： 一串连续的半角数字，比如匹配  199 、 888 

 \w  ： 单个字母/数字/下划线，比如匹配  a 、 5 、 _ 

 \w+  ： 一串连续的字母/数字/下划线，比如匹配  user123 、 name_1 

 \s  ： 单个空白（空格、换行、Tab），比如匹配普通空格、换行符

 \s+  ： 一串连续的空白，比如匹配多个连续空格

 .  ： 任意单个字符（除换行），比如匹配  a 、 ! 、 你 

 []  ： 匹配括号内任意一个字符，比如  [a-zA-Z]  匹配单个英文字母

 [^...]  ： 匹配「不在括号内」的任意字符，比如  [^a-zA-Z0-9\u4e00-\u9fa5]  匹配所有非中英数字的字符

{n}  恰好 n 次

{n,}  至少 n 次

{n,m}  最少 n 次，最多 m 次

\u4e00-\u9fa5 ：所有汉字

\uff01-\uff5e ：全角数字，字母，大部分常用符号

控制符等：

 \n  换行

 \r  回车

 \t  制表符（Tab）

 \b  退格

 \0  空字符

 \x00-\x1f  各种底层控制字符

全角空格  \u3000
