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

