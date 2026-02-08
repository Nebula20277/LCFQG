# DAY6-NOTE

## Numpy

### 是什么？

NumPy（Numerical Python）是 Python 的科学计算基础库，提供了：

-多维数组对象：ndarray

-数学函数库：向量化运算、线性代数、随机数生成

-广播机制：不同形状数组间的运算规则

### 创建

```python

import numpy as np

# example

arr1d = np.array([1, 2, 3, 4, 5]) 

matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

arr3d = np.array([[[1, 2], [3, 4]], 
                  [[5, 6], [7, 8]]])

# 不用np也能创建以上这些数组，但是使用np运行速度更快

```

### 属性

```python

dtype: 指定数据类型（影响精度和内存）

arr_int = np.array([1, 2, 3], dtype=np.int32)     # 32位整数

arr_float = np.array([1, 2, 3], dtype=np.float64) # 64位浮点数

arr_complex = np.array([1, 2, 3], dtype=complex)  # 复数

arr_bool = np.array([1, 0, 1], dtype=bool)        # 布尔值

# 不同位数范围不同，在保证不溢出的情况下越小越好，应考虑兼容性，性能权衡

dtype 对照表：

-np.int8, int16, int32, int64      # 有符号整数

-np.uint8, uint16, uint32, uint64  # 无符号整数

-np.float16, float32, float64      # 浮点数

-np.complex64, complex128          # 复数

-np.bool_                          # 布尔

-np.object_                        # Python对象
 
-np.string_, np.unicode_           # 字符串

ndmin: 最小维度。是np中创建函数中的一个参数，用于指定数组的最小维度，如果输入数据维度小于ndmin，np会自动在左边添加维度，直到达到指定维度。ndmin只升维，不降维。（维度 = 你需要几个索引才能定位到一个具体数字）

arr = np.array([1, 2, 3], ndmin=3)

# 将一维数组强制变为三维：shape (1, 1, 3)

属性详解：

arr = np.array([[1, 2, 3], [4, 5, 6]])

# 形状（shape）：元组，表示各维度大小

print(arr.shape)      # (2, 3) ← 2行3列

# 维度（ndim）：整数，表示数组维度

print(arr.ndim)       # 2 ← 二维数组

# 大小（size）：整数，表示元素总数

print(arr.size)       # 6 ← 2×3=6个元素

# 数据类型（dtype）：数组中元素的数据类型

print(arr.dtype)      # int64

# 步长（strides）：元组，表示每个维度上移动到下一个元素需要跨越的字节数

print(arr.strides)    # (24, 8) ← 行步长24字节，列步长8字节

# 解释：int64占8字节，一行3个元素→3×8=24字节

```

### Special Matrix

#### 全零矩阵

define：所有元素为0

z = np.zeros((2, 3), dtype=int)  # dtype=int 整数型，默认float

#### 全一矩阵

define：所有元素为1

ones_3d = np.ones((2, 3, 4), dtype=float) # 指定浮点类型

#### 单位矩阵

define：对角线上均为1，其余为0

性质：A × I = I × A = A

eye_3 = np.eye(3)       # 3×3单位矩阵

 [[1., 0., 0.],
 
  [0., 1., 0.],
  
  [0., 0., 1.]]

eye_rect = np.eye(3, 4)  # 3×4矩阵，对角线为1

 [[1., 0., 0., 0.],

  [0., 1., 0., 0.],
  
  [0., 0., 1., 0.]]

 k参数：对角线偏移

eye_k = np.eye(3, k=1)   # 主对角线向上偏移1

 [[0., 1., 0.],
 
  [0., 0., 1.],
  
  [0., 0., 0.]]

#### 对角矩阵

define：只有对角线上有非零值

diag_vals = [1, 2, 3, 4]

diag_matrix = np.diag(diag_vals)

[[1, 0, 0, 0],
  
  [0, 2, 0, 0],
  
  [0, 0, 3, 0],
  
  [0, 0, 0, 4]]

从矩阵提取对角线

matrix = np.array([[1, 2, 3],
  
                   [4, 5, 6],
                   
                   [7, 8, 9]])

main_diag = np.diag(matrix)  # [1, 5, 9]

k参数：对角线偏移

diag_k1 = np.diag(matrix, k=1)       # 上方第一条对角线： [2, 6]

diag_k_neg1 = np.diag(matrix, k=-1)  # 下方第一条对角线：[4, 8]

#### 随机矩阵

```python

-均匀分布 [0, 1)

rand_uniform = np.random.rand(3, 4)          # 3×4，均匀分布

[[0.5488135  0.71518937 0.60276338 0.54488318]

 [0.4236548  0.64589411 0.43758721 0.891773  ]
 
 [0.96366276 0.38344152 0.79172504 0.52889492]]



-标准正态分布（均值为0，标准差为1）

rand_normal = np.random.randn(3, 4)          # 3×4，正态分布

[[ 1.76405235  0.40015721  0.97873798  2.2408932 ]

[ 1.86755799 -0.97727788  0.95008842 -0.15135721]

 [-0.10321885  0.4105985   0.14404357  1.45427351]]

 

-随机整数 [low, high)

rand_int = np.random.randint(0, 10, (3, 4))  # 3×4，0-9随机整数

[[3 5 2 4]

[7 6 8 8]

 [1 6 7 7]]

 

-特定分布的随机数

rand_poisson = np.random.poisson(lam=5, size=(3, 4))          # 泊松分布

[[5 4 5 6]

 [4 6 3 4]
 
 [5 7 5 4]]

rand_binomial = np.random.binomial(n=10, p=0.5, size=(3, 4))  # 二项分布

[[5 5 5 6]

 [4 4 5 5]

 [4 6 5 5]]


-快速记忆
 
-  rand(shape)             [0,1) 均匀

-  randn(shape)            标准正态

-  randint(low,high,size)  整数

-  poisson(lam, size)      计数分布,固定平均次数 λ ,数实际发生几次

-  binomial(n,p,size)      n次试验成功次数,数成功几次

```

#### 等差数列矩阵

arange: 类似range，但返回数

arr = np.arange(0, 10, 2)        # [0, 2, 4, 6, 8]

linspace: 线性等分

数学公式：x_i = start + i × (stop-start)/(num-1)

arr_lin = np.linspace(0, 1, 5)   # [0., 0.25, 0.5, 0.75, 1.]

logspace: 对数等分

数学公式：x_i = base^(log_start + i×Δ)

arr_log = np.logspace(0, 2, 5)   # [1., 3.16, 10., 31.62, 100.]


#### 全值填充矩阵

define：所有值都相等的矩阵

full_matrix = np.full((3, 4), 7)     # 3×4矩阵，所有元素为7

full_like = np.full_like(matrix, 5)  # 形状同matrix，元素全为5

### Numpy的矩阵乘法

A = np.array([[1, 2], [3, 4]])  # 2×2

B = np.array([[5, 6], [7, 8]])  # 2×2

方法1：@ 运算符

C = A @ B

[[1*5+2*7, 1*6+2*8],

[3*5+4*7, 3*6+4*8]]

= [[19, 22],

  [43, 50]]

方法2：np.matmul（矩阵乘法）

C = np.matmul(A, B)  # 同上

方法3：np.dot（点积，也可用于矩阵乘法）

C = np.dot(A, B)     # 同上

方法4：A.dot(B)（对象方法）

C = A.dot(B)         # 同上
