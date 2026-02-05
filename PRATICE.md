#**DAY4-PRATICE**

##**Q&A**

###**Q**

*数据清洗*
####**部分概念解释**
1. Unicode空格：
常见Unicode空格：
```python
spaces = {
    "普通空格": " ",                # U+0020
    "不换行空格": "\u00A0",        # &nbsp; (HTML中)
    "全角空格": "\u3000",          # 中文全角空格
    "窄空格": "\u2009",            # 比普通空格窄
    "零宽空格": "\u200B",          # 不可见，但占位
    "不间断空格": "\u202F",        # 数字和单位之间
}
```

2. BOM头（Byte Order Mark）
字节顺序标记，是Unicode文件开头的特殊标记，用于标识编码和字节序
```python
# 这是正常的"hello"文本文件
正常文件 = b'h' + b'e' + b'l' + b'l' + b'o'
# 字节: 68 65 6C 6C 6F

# 这是带BOM头的"hello"（Windows记事本保存的）
BOM文件 = b'\xEF\xBB\xBF' + b'h' + b'e' + b'l' + b'l' + b'o'
# 字节: EF BB BF 68 65 6C 6C 6F
# ↑ 前面多了3个字节
```

4. 控制字符
不可见的设备控制符
```python
# 这些都是控制字符（你看不见！）：
隐身符 = "\x00"  # 空字符（NULL） → 什么都没有
响铃符 = "\x07"  # 让电脑"哔"一声
删除符 = "\x08"  # 删除前一个字符
逃逸符 = "\x1B"  # ESC键

举例：
print("正常文字" + "\x00" + "后面文字")  
# 输出：正常文字后面文字  ← 中间的\x00你看不见！

print("我要" + "\x07")  # 电脑可能会"哔"一声，但屏幕上看不到字符
```

5. 本地化格式
地区特定的数据格式(指不同地区有不同的表达方式)

6.全角数字
```python
# 正常数字（半角）：
正常 = "123"  # 英文输入法打的，瘦子

# 全角数字（胖子）：
全角 = "１２３"  # 中文输入法打的，每个字占2个英文字符宽度

print("正常数字:", 正常, "长度:", len(正常))  # "123" 长度:3
print("全角数字:", 全角, "长度:", len(全角))  # "１２３" 长度:3（但看起来胖！）
```

###**算法**
先清洗再过滤

数据归类：
**保留项**
1.0o，0x，0b，e
2.全角数字
3.\u，..，火
4.不同格式
5.

**剔除项**
1.全英文，全汉字
2.空白，空
3./，-，=，_，*
4.小列表内元素为列表或字典
5.纯字母加数字























###**A**
```python

```




#**DAY3-PRATICE**

##**Q&A**

###**Q**

*情报解密*

-截获一条杂乱情报： " Agent:007_Bond; Coords:(40,74); Items:gun,money,gun; 

Mission:2025-RESCUE-X " 

-请运用所有所学知识清洗数据：利用 **String** 方法去除干扰空格；利用 **Set** 帮特工去除重复装 

备；利用 **Slicing** 截取核心任务代号；利用 **Tuple**锁定坐标；最后将所有信息归档进一个 **Dict** 

档案中 



###**算法**

-使用strip（）和split（）进行干扰处理

-使用切片获取关键信息

-使用集合去重复

-使用元组锁定坐标

-使用字典进行归档



###**A**

```python
#情报整理：

mess_info=" Agent:007_Bond; Coords:(40,74); Items:gun,money,gun;  Mission:2025-RESCUE-X "
info_list=mess_info.split(';') #以；分割所截获情报字符串

print('分割后形成的情报列表为：') 
print(info_list) #打印初次分割后的情报列表

#去空格
cleaned_info=[]
for i in info_list:
    cleaned=i.strip()
    cleaned_info.append(cleaned)

print("去空格后的情报列表为：")
print(cleaned_info) #打印去空格后的情报列表


#用于存放最终处理后的结果
last_info={}

for i in cleaned_info:
    key,value=i.split(":",1)

    if key=='Agent':
        last_info[key]=value

    elif key=='Coords':
        coords_str=value[1:-1] #切片
        coords_list=coords_str.split(',')
        coords_tuple=(int(coords_list[0]),int(coords_list[1])) #将字符串型转为整型
        last_info[key]=coords_tuple 

    elif key=='Items':
        items_list=value.split(',')
        items_set=set(items_list) #集合去重复
        last_info[key]=items_set

    elif key=='Mission':
        index=value.find('-')
        mission_code=value[index+1:] #切片
        last_info[key]=mission_code

print('最终归档字典为：')
print(last_info) #打印最终处理后的归档字典

```



