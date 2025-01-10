### attention

首先要注意的是分数矩阵，分数矩阵的行数是样本数，列数是样本特征。

knn的具体过程：

训练矩阵(num_train, D)
测试矩阵(num_test, D)
距离矩阵(num_test, num_train)

现在需要通过训练矩阵和测试矩阵求得距离矩阵，最朴素的想法就是使用两层循环，外层循环遍历num_test, 内存循环遍历num_train，随后是计算当前测试矩阵的这个位置对于训练矩阵的位置，最后填充数据

`dists[i,j]=np.sqrt(np.sum((X[i]-self.X_train[j])**2))`

这里的意思是说，对于dists的每一个元素，都有如上计算。

其次是使用一层循环。使用一层循环则避开使用院选的内存循环num_train，也就是每次计算返回一个长度为num_train的numpy数组。所以只需要把`self.X_train[j]`的j去掉就可以了，这里利用了numpy的广播机制，由于self.X_train本身是一个二维numpy数组，`X[i]`是一维的(num_test, )，所以这里会自动将`X[i]`生维，变成(num_test, num_train)，二者相减平方并对每行进行求和，最后每个数据都开方，最后返回一个numpy一维数组，符合要求

`dists[i:]=np.sqrt(np.sum((X[i]-self.X_train)**2),axis=1)``

最后是不用循环。不用循环的话这里就用到了平方差公式。注意到测试矩阵和训练矩阵的逆相乘的话，即内积。在自己相乘的时候，需要注意最终是对行进行求和，因为需要将所有东西

```
lie=np.sum(X**2,axis=1).reshape(1,-1)
hang=np.sum(self.X_train**2,axis=1)
product=X.dot(self.X_train.T)

dists=np.sqrt(hang+lie-2*product)
```

### notes：

https://colab.research.google.com/drive/1fQLJ2RaYJqtu_8QsLgixJNvFULbL6LZK?usp=sharing
### ass1(35%)

作业

https://cs231n.github.io/assignments2024/assignment1/
#### knn(complete)：

https://drive.google.com/file/d/18_Bi46S7J2-BXo-r2o08-YRb2nmJHPfI/view?usp=sharing

```python
from builtins import range
from builtins import object
import numpy as np
from past.builtins import xrange


class KNearestNeighbor(object):
    """ 使用 L2 距离的 kNN 分类器 """

    def __init__(self):
        pass

    def train(self, X, y):
        """
        训练分类器。对于 k 最近邻分类器，训练只是记住训练数据。

        输入:
        - X: 一个形状为 (num_train, D) 的 numpy 数组，包含训练数据，
             其中 num_train 是样本数量，每个样本的维度为 D。
        - y: 一个形状为 (num_train,) 的 numpy 数组，包含训练标签，
             其中 y[i] 是样本 X[i] 的标签。
        """
        self.X_train = X
        self.y_train = y

    def predict(self, X, k=1, num_loops=0):
        """
        使用此分类器预测测试数据的标签。

        输入:
        - X: 一个形状为 (num_test, D) 的 numpy 数组，包含测试数据，
             其中 num_test 是样本数量，每个样本的维度为 D。
        - k: 投票的最近邻数量。
        - num_loops: 决定使用哪个实现来计算训练点和测试点之间的距离。

        返回:
        - y: 一个形状为 (num_test,) 的 numpy 数组，包含测试数据的预测标签，
             其中 y[i] 是测试点 X[i] 的预测标签。
        """
        if num_loops == 0:
            dists = self.compute_distances_no_loops(X)
        elif num_loops == 1:
            dists = self.compute_distances_one_loop(X)
        elif num_loops == 2:
            dists = self.compute_distances_two_loops(X)
        else:
            raise ValueError("Invalid value %d for num_loops" % num_loops)

        return self.predict_labels(dists, k=k)

    def compute_distances_two_loops(self, X):
        """
        使用两个嵌套循环计算测试点 X 和训练点 self.X_train 之间的距离。

        输入:
        - X: 一个形状为 (num_test, D) 的 numpy 数组，包含测试数据。

        返回:
        - dists: 一个形状为 (num_test, num_train) 的 numpy 数组，
          其中 dists[i, j] 是第 i 个测试点和第 j 个训练点之间的欧几里得距离。
        """
        num_test = X.shape[0]
        num_train = self.X_train.shape[0]
        dists = np.zeros((num_test, num_train))
        for i in range(num_test):
            for j in range(num_train):
                #####################################################################
                # TODO:                                                             #
                # 计算第 i 个测试点和第 j 个训练点之间的 L2 距离，并将结果存储在         #
                # dists[i, j] 中。不应使用维度上的循环，也不使用 np.linalg.norm()。     #
                #####################################################################
                # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

                dists[i, j] = np.sqrt(np.sum((X[i] - self.X_train[j]) ** 2))

                # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        return dists

    def compute_distances_one_loop(self, X):
        """
        使用单个循环计算测试点 X 和训练点 self.X_train 之间的距离。

        输入 / 输出: 与 compute_distances_two_loops 相同。
        """
        num_test = X.shape[0]
        num_train = self.X_train.shape[0]
        dists = np.zeros((num_test, num_train))
        for i in range(num_test):
            #######################################################################
            # TODO:                                                               #
            # 计算第 i 个测试点与所有训练点之间的 L2 距离，并将结果存储在             #
            # dists[i, :] 中。不要使用 np.linalg.norm()。                           #
            #######################################################################
            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            dists[i, :] = np.sqrt(np.sum((self.X_train - X[i]) ** 2, axis=1))

            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        return dists

    def compute_distances_no_loops(self, X):
        """
        不使用显式循环，计算测试点 X 和训练点 self.X_train 之间的距离。

        输入 / 输出: 与 compute_distances_two_loops 相同。
        """
        num_test = X.shape[0]
        num_train = self.X_train.shape[0]
        dists = np.zeros((num_test, num_train))
        #########################################################################
        # TODO:                                                                 #
        # 不使用显式循环，计算所有测试点与所有训练点之间的 L2 距离，并将结果存储在     #
        # dists 中。                                                             #
        #                                                                       #
        # 你应该只使用基本的数组操作；特别是不要使用 scipy 中的函数，也不要使用       #
        # np.linalg.norm()。                                                     #
        #                                                                       #
        # 提示: 尝试使用矩阵乘法和两个广播和来公式化 L2 距离。                      #
        #########################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        test_sq = np.sum(X**2, axis=1).reshape(-1, 1)  # 测试点平方和列向量
        train_sq = np.sum(self.X_train**2, axis=1)  # 训练点平方和行向量
        dot_product = X @ self.X_train.T  # 测试点和训练点的矩阵内积

        dists = np.sqrt(test_sq + train_sq - 2 * dot_product)

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        return dists

    def predict_labels(self, dists, k=1):
        """
        给定测试点和训练点之间的距离矩阵，为每个测试点预测标签。

        输入:
        - dists: 一个形状为 (num_test, num_train) 的 numpy 数组，
                 其中 dists[i, j] 给出了第 i 个测试点和第 j 个训练点之间的距离。

        返回:
        - y: 一个形状为 (num_test,) 的 numpy 数组，包含测试数据的预测标签，
             其中 y[i] 是测试点 X[i] 的预测标签。
        """
        num_test = dists.shape[0]
        y_pred = np.zeros(num_test)
        for i in range(num_test):
            # 一个长度为 k 的列表，存储第 i 个测试点最近的 k 个邻居的标签。
            closest_y = []
            #########################################################################
            # TODO:                                                                 #
            # 使用距离矩阵找到第 i 个测试点最近的 k 个邻居，并使用 self.y_train 找到    #
            # 这些邻居的标签。将这些标签存储在 closest_y 中。                          #
            # 提示: 查阅 numpy.argsort 函数。                                        #
            #########################################################################
            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            sorted_i = np.argsort(dists[i, :])
            closest_y = self.y_train[sorted_i[:k]]

            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
            #########################################################################
            # TODO:                                                                 #
            # 现在你已经找到了最近邻的标签，需要找到这些标签中最常见的标签，并将其存储 #
            # 在 y_pred[i] 中。如果有平局，选择较小的标签。                            #
            #########################################################################
            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            unique_labels, counts = np.unique(closest_y, return_counts=True)
            y_pred[i] = unique_labels[np.argmax(counts)]

            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        return y_pred

```


#### svm

https://drive.google.com/file/d/10wPKQl63mzOKKUvKlebWMDzzne4BlAgG/view?usp=sharing

```python
from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange


def svm_loss_naive(W, X, y, reg):
    """
    结构化 SVM 损失函数的朴素实现（带有循环）。

    输入的维度为 D，类别数为 C，我们针对一个包含 N 个样本的小批量数据进行操作。

    输入参数：
    - W: 一个形状为 (D, C) 的 numpy 数组，包含权重。
    - X: 一个形状为 (N, D) 的 numpy 数组，包含小批量数据。
    - y: 一个形状为 (N,) 的 numpy 数组，包含训练标签；
         y[i] = c 表示 X[i] 的标签是 c，且 0 <= c < C。
    - reg: 一个浮点数，表示正则化强度。

    返回值：
    - loss: 损失值，单个浮点数。
    - dW: 关于权重 W 的梯度，与 W 的形状相同。
    """
    dW = np.zeros(W.shape)  # 初始化梯度为 0

    # 计算损失和梯度
    num_classes = W.shape[1]
    num_train = X.shape[0]
    loss = 0.0
    for i in range(num_train):
        scores = X[i].dot(W)
        correct_class_score = scores[y[i]]
        for j in range(num_classes):
            if j == y[i]:
                continue
            margin = scores[j] - correct_class_score + 1  # 注意 delta = 1
            if margin > 0:
                loss += margin

                dW[:, j] += X[i]    # 错误类别的权重增加
                dW[:, y[i]] -= X[i] # 正确类别的权重减少

    # 目前损失是所有训练样本的总和，但我们希望取平均值，因此除以样本数量
    loss /= num_train

    # 为损失添加正则化
    loss += reg * np.sum(W * W)

    #############################################################################
    # TODO:                                                                     #
    # 计算损失函数的梯度，并将结果存储到 dW 中。                                  #
    # 相较于先计算损失再计算导数，边计算损失边计算导数可能更简单。                  #
    # 因此，你可能需要修改上方的某些代码，以便在计算损失时同时计算导数。             #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    dW = dW / num_train + 2 * reg * W

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def svm_loss_vectorized(W, X, y, reg):
    """
    结构化 SVM 损失函数的向量化实现。

    输入参数和返回值与 svm_loss_naive 相同。
    """
    loss = 0.0
    dW = np.zeros(W.shape)  # 初始化梯度为 0

    #############################################################################
    # TODO:                                                                     #
    # 实现结构化 SVM 损失函数的向量化版本，将结果存储到 loss 中。                   #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    num_classes = W.shape[1]
    num_train = X.shape[0]

    scores = X.dot(W)
    correct_class_scores = scores[np.arange(num_train), y].reshape(-1, 1)

    margins = np.maximum(0, scores - correct_class_scores + 1)
    margins[np.arange(num_train), y] = 0

    loss = np.sum(margins) / num_train
    loss += reg * np.sum(W * W)

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    #############################################################################
    # TODO:                                                                     #
    # 实现结构化 SVM 损失函数梯度的向量化版本，并将结果存储到 dW 中。                #
    #                                                                           #
    # 提示：可以重复使用计算损失时的中间值，而不是重新计算梯度。                     #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    binary = (margins > 0).astype(float)
    row_sum = np.sum(binary, axis=1)  # 每个样本中正间隔的数量
    binary[np.arange(num_train), y] = -row_sum  # 正确类别的权重修正

    dW = X.T.dot(binary) / num_train
    dW += 2 * reg * W

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
```
```
