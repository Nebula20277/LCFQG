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
```python
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

### 不同类型乘法

```python

# 1. 逐元素乘法（Element-wise，Hadamard积）

A = np.array([[1, 2], [3, 4]])

B = np.array([[2, 3], [4, 5]])

C_elementwise = A * B  # 或 np.multiply(A, B)

# [[1*2, 2*3],

#  [3*4, 4*5]] = [[2, 6], [12, 20]]

# 2. 矩阵乘法

C_matrix = A @ B

# [[1*2+2*4, 1*3+2*5],

#  [3*2+4*4, 3*3+4*5]] = [[10, 13], [22, 29]]

# 3. 向量内积（点积）

v1 = np.array([1, 2, 3])

v2 = np.array([4, 5, 6])

dot_product = np.dot(v1, v2)  # 1*4 + 2*5 + 3*6 = 32

# 4. 向量外积

outer_product = np.outer(v1, v2)

在三维空间里，向量外积（叉乘）最核心、最常用的作用，就是求一个同时垂直于两个向量的新向量

# 3×3矩阵，第i行第j列 = v1[i] × v2[j]

# 5. 克罗内克积（Kronecker Product）

kron_product = np.kron(A, B)

# 将A的每个元素a_ij替换为a_ij×B

```

### 高维数组乘法

```python

# 三维数组的矩阵乘法（批量矩阵乘法）

A = np.random.rand(10, 3, 4)  # 10个3×4矩阵

B = np.random.rand(10, 4, 5)  # 10个4×5矩阵

C = np.matmul(A, B)           # 结果：10个3×5矩阵

# C[i] = A[i] @ B[i] 对每个i

# 不同维度的广播乘法（见广播机制部分）

```

### 矩阵广播机制（Broadcasting）

1. 广播概念

广播是 NumPy 对不同形状数组进行算术运算的机制。当运算涉及两个不同形状的数组时，较小的数组会"广播"以匹配较大数组的形状，而不需要实际复制数据。

2. 广播规则

规则1：如果两个数组维度数不同，小维度数组的形状会在左边补1

规则2：如果两个数组在某个维度上大小不同，但其中一个为1，则该维度扩展到与另一个相同

规则3：如果两个数组在某个维度上大小不同且都不为1，则报错


### Numpy转置

方法1：A.T

方法2：A.transpose()

方法2：np.transpose(A)

#### 共轭矩阵转置

.conj().T 或 .H

### Numpy逆矩阵

```python

# 创建可逆矩阵

A = np.array([[4, 7],
              [2, 6]])           # 方阵

# 检查是否可逆

det = np.linalg.det(A)           # 行列式 = 4*6 - 7*2 = 10 ≠ 0

# 方法1：np.linalg.inv（标准方法）

A_inv = np.linalg.inv(A)

# [[ 0.6, -0.7],

#  [-0.2,  0.4]]

# 验证：A × A⁻¹ ≈ I（可能有浮点误差）

I = A @ A_inv                    # 应接近单位矩阵

print(np.allclose(I, np.eye(2))) # True

# 方法2：np.linalg.pinv（伪逆，适用于非方阵或奇异矩阵）

A_rect = np.array([[1, 2, 3],

                   [4, 5, 6]])   # 2×3，不是方阵

A_pinv = np.linalg.pinv(A_rect)  # 伪逆，3×2

```

### 矩阵存取

1.单个元素获取

matrix[x,x]

2.行，列获取

整行：arr[row_idx, :]（: 表示 “所有列”）

整列：arr[:, col_idx]（: 表示 “所有行”）

3.切片

```python

# 重新创建原始矩阵

mat = np.array([[1, 2, 3],

                [4, 5, 6],

                [7, 8, 9]])

# 取第 0-1 行，第 1-2 列（左闭右开，实际取行 0/1，列 1/2）

slice1 = mat[0:2, 1:3]  # → array([[2,3], [5,6]])

# 取所有行，第 0-1 列（步长默认 1）

slice2 = mat[:, 0:2]    # → array([[1,2], [4,5], [7,8]])

# 取偶数行（步长 2），所有列

slice3 = mat[::2, :]    # → array([[1,2,3], [7,8,9]])

# 取最后两行，最后两列

slice4 = mat[-2:, -2:]  # → array([[5,6], [8,9]])

# 修改切片（注意：切片是视图，修改会影响原矩阵！）

slice1[0, 0] = 20       # → 原矩阵变为：[[1,20,3], [4,5,6], [7,8,9]]

关键易错点：切片是 “视图” 而非 “副本”

视图：切片返回的是原数组的引用，修改切片会直接改原矩阵；

如需独立副本：用 copy() 方法。

```
#### 高级索引

```python

mat = np.array([[1, 2, 3],

                [4, 5, 6],

                [7, 8, 9]])

# 取第 0 行和第 2 行，所有列

rows = mat[[0, 2], :]  # → array([[1,2,3], [7,8,9]])

# 取所有行，第 1 列和第 0 列（注意顺序）

cols = mat[:, [1, 0]]  # → array([[2,1], [5,4], [8,7]])

# 取指定行列的交叉元素（如 (0,2)、(2,1)）

elems = mat[[0, 2], [2, 1]]  # → array([3, 8])

```

##### 布尔索引

```python

# 取矩阵中大于 5 的元素

mask = mat > 5  # 布尔矩阵：[[False,False,False], [False,False,True], [True,True,True]]

vals = mat[mask]  # → array([6,7,8,9])

# 修改大于 5 的元素为 0

mat[mask] = 0  # 矩阵变为：[[1,2,3], [4,5,0], [0,0,0]]

# 按行条件筛选：取第二列大于 2 的行

row_mask = mat[:, 1] > 2  # → array([False, True, False])

filter_rows = mat[row_mask, :]  # → array([[4,5,0]])

```

```python

# 整体替换为标量

mat[:] = 10  # 所有元素变为 10 → [[10,10,10], [10,10,10], [10,10,10]]

# 用同形状矩阵替换

new_mat = np.array([[1,2,3], [4,5,6], [7,8,9]])

mat[:] = new_mat  # 恢复原始矩阵

```

### 矩阵相关文件操作

（1）保存为 NPY 格式

```python

# 保存矩阵到文件

np.save("matrix_data.npy", mat)

# 从文件读取矩阵

mat_loaded = np.load("matrix_data.npy")

```

（2）保存为 CSV 格式（通用，可被 Excel / 文本编辑器打开）

```python

# 保存为 CSV

np.savetxt("matrix_data.csv", mat, delimiter=",", fmt="%d")  # fmt=%d 表示整数格式

# 读取 CSV

mat_loaded = np.loadtxt("matrix_data.csv", delimiter=",")

```
