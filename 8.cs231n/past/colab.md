### attention

#### knn

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


#### liner

这部分的内容主要是svm，softmax和sgd

线性分类器需要注意的地方有很多。首先必须得理解其全部的过程。

首先SVM 需要计算每个样本的分类分数。假设数据集包含 N 个样本，每个样本有 D 个特征，一共有 C 个类别，那么数据矩阵 X 的形状是 (N, D)，权重矩阵 W 的形状是 (D, C)。为了计算每个样本在每个类别上的得分，需要进行矩阵乘法 `scores = X.dot(W)`，这样得到的 `scores` 矩阵形状是 (N, C)，其中 `scores[i, j]` 表示第 i 个样本在类别 j 上的得分。

接下来计算 SVM 的损失函数，SVM 采用的是 hinge loss，即希望正确类别的得分比其他类别的得分高至少 1，否则就会有损失。首先需要取出每个样本的正确类别得分 `correct_class_scores = scores[np.arange(N), y]`，这里利用 NumPy 的高级索引，`np.arange(N)` 生成从 0 到 N-1 的索引，而 `y` 记录了每个样本对应的正确类别，因此 `correct_class_scores` 是一个形状为 (N,) 的向量，包含了所有样本的正确类别得分。接下来计算每个类别相对于正确类别的间隔 `margins = np.maximum(0, scores - correct_class_scores[:, np.newaxis] + 1)`，这里 `correct_class_scores[:, np.newaxis]` 通过 `np.newaxis` 变成了 (N, 1) 形状，使其可以与 `scores` 进行广播运算，每个样本的正确类别得分都会被扩展到所有类别上，与 `scores` 进行逐元素相减，得到一个形状为 (N, C) 的矩阵，再加上 1 作为 SVM 的边界要求，最后 `np.maximum(0, ...)` 确保间隔小于 0 的部分不会贡献损失。

正确类别的间隔是不应该计入损失的，因此需要手动将正确类别的间隔置零，`margins[np.arange(N), y] = 0`，这样正确类别的那一列损失就不会被计算在内。然后计算总损失 `loss = np.sum(margins) / N + reg * np.sum(W * W)`，其中 `np.sum(margins) / N` 计算的是平均损失，`reg * np.sum(W * W)` 是 L2 正则化项，防止过拟合。

接下来计算梯度，对于错误分类的类别，即 `margins > 0` 的部分，它的权重应该增加，因此首先构造一个与 `margins` 形状相同的二值矩阵 `binary = (margins > 0).astype(float)`，这个矩阵的作用是标记哪些类别产生了损失，`binary[i, j] = 1` 表示第 i 个样本的类别 j 产生了损失，需要增加该类别的权重。同时，对于每个样本的正确类别，它的梯度应该减少，因此需要统计该样本总共有多少个错误分类 `row_sum = np.sum(binary, axis=1)`，然后更新正确类别的梯度 `binary[np.arange(N), y] = -row_sum`，这样保证正确类别的梯度是所有错误类别梯度的负和。最终，计算梯度 `dW = X.T.dot(binary) / N + 2 * reg * W`，这里 `X.T.dot(binary)` 计算的是所有样本贡献的梯度，`/ N` 取均值，`2 * reg * W` 是正则化项的梯度。

对于 Softmax，计算方式稍有不同。首先也是计算 `scores = X.dot(W)`，但 Softmax 需要对得分进行指数化并归一化，直接计算 `exp_scores = np.exp(scores)` 可能会导致数值溢出，因此需要进行数值稳定性处理，先减去每个样本的最大得分 `scores -= np.max(scores, axis=1, keepdims=True)`，这样保证最大值变为 0，指数化后不会过大。然后计算 `exp_scores = np.exp(scores)`，并归一化 `probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)`，得到的 `probs` 形状为 (N, C)，其中 `probs[i, j]` 代表第 i 个样本属于类别 j 的概率。

计算 Softmax 的损失时，需要关注正确类别的概率，首先取出 `correct_class_probs = probs[np.arange(N), y]`，然后计算交叉熵损失 `loss = -np.sum(np.log(correct_class_probs)) / N + reg * np.sum(W * W)`，这里 `-np.log(correct_class_probs)` 计算的是正确类别的负对数概率，取均值后加上正则化项。梯度计算时，Softmax 采用的是概率分布方式，因此先计算 `dscores = probs`，然后 `dscores[np.arange(N), y] -= 1`，这一操作相当于计算 `probs - y_one_hot`，即正确类别的梯度减少，错误类别的梯度增加。最后计算 `dW = X.T.dot(dscores) / N + 2 * reg * W`，同样是取均值并加上正则化项。

无论是 SVM 还是 Softmax，最终都需要使用 SGD 来优化权重。在每一次迭代中，从数据集中随机抽取一批样本，计算损失和梯度，然后更新权重 `W -= learning_rate * dW`，使得损失逐步减少。SGD 的核心在于每次只使用一小部分数据，而不是整个数据集，从而加快计算速度。
### notes：

https://colab.research.google.com/drive/1fQLJ2RaYJqtu_8QsLgixJNvFULbL6LZK?usp=sharing

notes后面基本没写，这里理解起来并非是用notes就能理解的，而是得把那些专业的术语转换为自己可以理解的语言
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


#### svm(complete)

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

```python
from __future__ import print_function

from builtins import range
from builtins import object
import numpy as np
from ..classifiers.linear_svm import *
from ..classifiers.softmax import *
from past.builtins import xrange


class LinearClassifier(object):
    def __init__(self):
        self.W = None

    def train(
        self,
        X,
        y,
        learning_rate=1e-3,
        reg=1e-5,
        num_iters=100,
        batch_size=200,
        verbose=False,
    ):
        """
        Train this linear classifier using stochastic gradient descent.

        Inputs:
        - X: A numpy array of shape (N, D) containing training data; there are N
          training samples each of dimension D.
        - y: A numpy array of shape (N,) containing training labels; y[i] = c
          means that X[i] has label 0 <= c < C for C classes.
        - learning_rate: (float) learning rate for optimization.
        - reg: (float) regularization strength.
        - num_iters: (integer) number of steps to take when optimizing
        - batch_size: (integer) number of training examples to use at each step.
        - verbose: (boolean) If true, print progress during optimization.

        Outputs:
        A list containing the value of the loss function at each training iteration.
        """
        num_train, dim = X.shape
        num_classes = (
            np.max(y) + 1
        )  # assume y takes values 0...K-1 where K is number of classes
        if self.W is None:
            # lazily initialize W
            self.W = 0.001 * np.random.randn(dim, num_classes)

        # Run stochastic gradient descent to optimize W
        loss_history = []
        for it in range(num_iters):
            X_batch = None
            y_batch = None

            #########################################################################
            # TODO:                                                                 #
            # Sample batch_size elements from the training data and their           #
            # corresponding labels to use in this round of gradient descent.        #
            # Store the data in X_batch and their corresponding labels in           #
            # y_batch; after sampling X_batch should have shape (batch_size, dim)   #
            # and y_batch should have shape (batch_size,)                           #
            #                                                                       #
            # Hint: Use np.random.choice to generate indices. Sampling with         #
            # replacement is faster than sampling without replacement.              #
            #########################################################################
            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            #随机采样小批量数据

            batch_indices = np.random.choice(X.shape[0], batch_size, replace=True)
            X_batch = X[batch_indices]
            y_batch = y[batch_indices]

            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            # evaluate loss and gradient
            loss, grad = self.loss(X_batch, y_batch, reg)
            loss_history.append(loss)

            # perform parameter update
            #########################################################################
            # TODO:                                                                 #
            # Update the weights using the gradient and the learning rate.          #
            #########################################################################
            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            self.W -= learning_rate * grad

            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            if verbose and it % 100 == 0:
                print("iteration %d / %d: loss %f" % (it, num_iters, loss))

        return loss_history

    def predict(self, X):
        """
        Use the trained weights of this linear classifier to predict labels for
        data points.

        Inputs:
        - X: A numpy array of shape (N, D) containing training data; there are N
          training samples each of dimension D.

        Returns:
        - y_pred: Predicted labels for the data in X. y_pred is a 1-dimensional
          array of length N, and each element is an integer giving the predicted
          class.
        """
        y_pred = np.zeros(X.shape[0])
        ###########################################################################
        # TODO:                                                                   #
        # Implement this method. Store the predicted labels in y_pred.            #
        ###########################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        # 计算分数
        scores = X.dot(self.W)

        #获取最大
        y_pred = np.argmax(scores, axis=1)

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        return y_pred

    def loss(self, X_batch, y_batch, reg):
        """
        Compute the loss function and its derivative.
        Subclasses will override this.

        Inputs:
        - X_batch: A numpy array of shape (N, D) containing a minibatch of N
          data points; each point has dimension D.
        - y_batch: A numpy array of shape (N,) containing labels for the minibatch.
        - reg: (float) regularization strength.

        Returns: A tuple containing:
        - loss as a single float
        - gradient with respect to self.W; an array of the same shape as W
        """
        pass


class LinearSVM(LinearClassifier):
    """ A subclass that uses the Multiclass SVM loss function """

    def loss(self, X_batch, y_batch, reg):
        return svm_loss_vectorized(self.W, X_batch, y_batch, reg)


class Softmax(LinearClassifier):
    """ A subclass that uses the Softmax + Cross-entropy loss function """

    def loss(self, X_batch, y_batch, reg):
        return softmax_loss_vectorized(self.W, X_batch, y_batch, reg)

```

#### softmax(complete)

https://drive.google.com/file/d/1Q8YgnFQ5D0QSewBGSv2XlgXSKwYDtn2g/view?usp=sharing

```python
from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange


def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    # 计算损失和梯度
    num_classes = W.shape[1]
    num_train = X.shape[0]

    for i in range(num_train):
        scores = X[i].dot(W)
        scores -= np.max(scores)

        exp_scores = np.exp(scores)
        probs = exp_scores / np.sum(exp_scores)

        loss += -np.log(probs[y[i]])

        for j in range(num_classes):
            if j == y[i]:
              dW[:,j] += (probs[j] - 1) * X[i]
            else:
              dW[:,j] += probs[j] * X[i]

    loss /= num_train
    dW /= num_train

    loss += reg * np.sum(W * W)
    dW += 2 * reg * W

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    num_classes=W.shape[1]
    num_train=X.shape[0]

    scores=X.dot(W)
    scores-=np.max(scores,axis=1,keepdims=True)

    exp_scores=np.exp(scores)
    probs=exp_scores/np.sum(exp_scores,axis=1,keepdims=True)

    correct_class_probs = probs[np.arange(num_train), y]  # (N,)
    loss = -np.sum(np.log(correct_class_probs)) / num_train  # 标量

    dscores = probs  # (N, C)
    dscores[np.arange(num_train), y] -= 1  # 只对正确类别做调整
    dscores /= num_train  # 取均值

    dW = X.T.dot(dscores)  # (D, C)

    loss += reg * np.sum(W * W)
    dW += 2 * reg * W

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW

```

