# DAY5-NOTE

## 面向对象

### 类

#### 继承

继承的核心机制：

语法：class 子类名(父类名):

单继承：一个子类只有一个父类

多继承：一个子类有多个父类，如class C(A, B):

方法继承：子类自动获得父类所有非私有方法

属性继承：子类获得父类所有非私有属性

方法重写：子类可重新定义父类方法，覆盖原有实现


##### super()

Function:在子类中调用父类方法，保持继承链

```python

class 子类（父类）:

    def __init__(self):

        super().__init__()

example1:

class 动物:

    def __init__(self, 名字):

        self.名字 = 名字

        print(f"动物 {self.名字} 被创建")

class 狗(动物):

    def __init__(self, 名字, 品种):

        super().__init__(名字)  # 必须先调用父类初始化！

        self.品种 = 品种

        print(f"狗 {self.名字} 是 {self.品种}")

我的狗 = 狗("小白", "哈士奇")

# 输出：

# 动物 小白 被创建

# 狗 小白 是 哈士奇

Format of using:

最常用的格式（Python 3）

super().方法名(参数)

在类方法中

@classmethod

def 类方法(cls):

    super().类方法()  # 同样适用

```

