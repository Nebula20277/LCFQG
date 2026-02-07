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

### 关键参数

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
