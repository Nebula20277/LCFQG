# DAY10&11-NOTE10

## 向量

## 内积（点积）

点积计算：dot_product1 = np.dot(a, b)

模长计算：norm_a = np.linalg.norm(a) 

## 矩阵乘法

$c_{ij}=\sum_{k=1}^{n}a_{ik}b_{kj}$

AB 表示：先应用变换B，再应用变换A

重要：矩阵乘法不交换，AB≠BA

计算：C1 = np.matmul(A, B) / C2 = A @ B

