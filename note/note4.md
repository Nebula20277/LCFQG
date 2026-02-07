# DAY5-NOTE

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

