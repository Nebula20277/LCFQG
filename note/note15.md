# DAY16-NOTE

## 梯度下降法

梯度下降是一种「找函数最小值」的迭代优化算法。

在机器学习里：

- 我们有一个损失函数（Loss Function），衡量模型预测有多差。

- 目标：让损失函数尽可能小。

- 手段：沿着函数下降最快的方向，一步步往前走，直到走到谷底。

前置数学知识：

导数/偏导数/方向导数/梯度

梯度：把所有偏导数排成向量

∇f 的方向 = 函数上升最快的方向

### 关于梯度下降的详细解析

由于我们使用最小二乘法衡量误差，即真实值和预测值之间的差距，为了使二者之间更加拟合，我们需要减少误差，如何减少误差？求导，答案就是求导，对应这里的多元函数就是求偏导，即针对各个参数进行求导，并且，找到其梯度。对MSE求偏导有：

$$
\begin{align*}
\frac{\partial J}{\partial \theta_j} 
&= \frac{\partial}{\partial \theta_j} \left[ \frac{1}{2m} \sum_{i=1}^m \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2 \right] \\
&= \frac{1}{2m} \sum_{i=1}^m \frac{\partial}{\partial \theta_j} \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2 
\quad \text{（求和的导数等于导数的求和）} \\
&= \frac{1}{2m} \sum_{i=1}^m 2 \cdot \left( h_\theta(x^{(i)}) - y^{(i)} \right) \cdot \frac{\partial}{\partial \theta_j} \left( h_\theta(x^{(i)}) - y^{(i)} \right)
\quad \text{（链式法则）} \\
&= \frac{1}{m} \sum_{i=1}^m \left( h_\theta(x^{(i)}) - y^{(i)} \right) \cdot \frac{\partial h_\theta(x^{(i)})}{\partial \theta_j}
\quad \text{（2和1/2抵消，y是常数，导数为0）}
\end{align*}
$$

接下来，我们需要算
$\frac{\partial h_\theta\left(x^{(i)}\right)}{\partial \theta_j}$

已知
$h_\theta(x^{(i)}) = \theta_0 + \theta_1 x_1^{(i)} + \cdots + \theta_j x_j^{(i)} + \cdots$

对
$\theta_j$
求导后可得出：
$\frac{\partial h_\theta(x^{(i)})}{\partial \theta_j} = x_j^{(i)}$

最后我们可以得出
$\frac{\partial J}{\partial \theta_j} = \frac{1}{m} \sum_{i=1}^m \left( h_\theta(x^{(i)}) - y^{(i)} \right) x_j^{(i)}$

据此，我们可以进行所有参数的更新：

$$
\begin{align*}
\theta_0 &:= \theta_0 - \eta \cdot \frac{\partial J}{\partial \theta_0} \\
\theta_1 &:= \theta_1 - \eta \cdot \frac{\partial J}{\partial \theta_1} \\
&\vdots \\
\theta_n &:= \theta_n - \eta \cdot \frac{\partial J}{\partial \theta_n}
\end{align*}
$$

而η即我们所说的学习率，学习率 η 告诉我们 “每一步走多远”。

补充：

收敛的核心定义（一句话讲透）

在梯度下降中，收敛就是指：随着迭代次数增加，模型参数 θ 不再发生明显变化，损失函数 J(θ) 的值也稳定在一个极小值（谷底）附近，不再大幅波动或持续增大。简单说：模型找到了最优解（或接近最优解），不再 “乱动” 了。


## 多元线性回归模型

行向量与列向量相乘，本质上是点积（Dot Product）

## 损失函数（均方误差）（MSE）

乘以1/2是为了求导时消去系数，便于计算
