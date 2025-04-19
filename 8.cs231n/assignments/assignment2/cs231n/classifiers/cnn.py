from builtins import object
import numpy as np

from ..layers import *
from ..fast_layers import *
from ..layer_utils import *


class ThreeLayerConvNet(object):
    """
    A three-layer convolutional network with the following architecture:

    conv - relu - 2x2 max pool - affine - relu - affine - softmax

    The network operates on minibatches of data that have shape (N, C, H, W)
    consisting of N images, each with height H and width W and with C input
    channels.
    """

    """
    具有以下架构的三层卷积网络：

    卷积 - RELU - 2x2 最大池 - 仿射 - RELU - 仿射 - SoftMax

    该网络对形状为 （N、C、H、W） 的小批量数据进行作，这些数据由 N 张图像组成，每张图像的高度为 H，宽度为 W，输入通道为 C。
    """

    def __init__(
        self,
        input_dim=(3, 32, 32),
        num_filters=32,
        filter_size=7,
        hidden_dim=100,
        num_classes=10,
        weight_scale=1e-3,
        reg=0.0,
        dtype=np.float32,
    ):
        """
        Initialize a new network.

        Inputs:
        - input_dim: Tuple (C, H, W) giving size of input data
        - num_filters: Number of filters to use in the convolutional layer
        - filter_size: Width/height of filters to use in the convolutional layer
        - hidden_dim: Number of units to use in the fully-connected hidden layer
        - num_classes: Number of scores to produce from the final affine layer.
        - weight_scale: Scalar giving standard deviation for random initialization
          of weights.
        - reg: Scalar giving L2 regularization strength
        - dtype: numpy datatype to use for computation.
        """
        self.params = {}
        self.reg = reg
        self.dtype = dtype

        ############################################################################
        # TODO: Initialize weights and biases for the three-layer convolutional    #
        # network. Weights should be initialized from a Gaussian centered at 0.0   #
        # with standard deviation equal to weight_scale; biases should be          #
        # initialized to zero. All weights and biases should be stored in the      #
        #  dictionary self.params. Store weights and biases for the convolutional  #
        # layer using the keys 'W1' and 'b1'; use keys 'W2' and 'b2' for the       #
        # weights and biases of the hidden affine layer, and keys 'W3' and 'b3'    #
        # for the weights and biases of the output affine layer.                   #
        #                                                                          #
        # IMPORTANT: For this assignment, you can assume that the padding          #
        # and stride of the first convolutional layer are chosen so that           #
        # **the width and height of the input are preserved**. Take a look at      #
        # the start of the loss() function to see how that happens.                #
        ############################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        # 任务：为三层卷积网络初始化权重和偏置。权重应从以0.0为中心的高斯分布初始化，标准差等于weight_scale；
        # 偏置应初始化为零。所有权重和偏置应存储在字典self.params中。卷积层的权重和偏置使用键'W1'和'b1'；
        # 隐藏全连接层的权重和偏置使用键'W2'和'b2'；输出全连接层的权重和偏置使用键'W3'和'b3'。
        # 
        # 重要提示：本作业中，可以假定第一个卷积层的填充和步长参数被选择为保持输入宽度和高度不变。
        # 请参考loss()函数开头的实现方式了解具体实现细节。

        C, H, W = input_dim

        self.params = {}

        self.params['W1'] = weight_scale * np.random.randn(num_filters, C, filter_size, filter_size)
        self.params['b1'] = np.zeros(num_filters)
        
        pool_stride = 2
        H_pool = H // pool_stride
        W_pool = W // pool_stride
        self.conv_output_dim = num_filters * H_pool * W_pool 
        
        self.params['W2'] = weight_scale * np.random.randn(self.conv_output_dim, hidden_dim)
        self.params['b2'] = np.zeros(hidden_dim)
        
        self.params['W3'] = weight_scale * np.random.randn(hidden_dim, num_classes)
        self.params['b3'] = np.zeros(num_classes)

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        ############################################################################
        #                             END OF YOUR CODE                             #
        ############################################################################

        for k, v in self.params.items():
            self.params[k] = v.astype(dtype)

    def loss(self, X, y=None):
        """
        Evaluate loss and gradient for the three-layer convolutional network.

        Input / output: Same API as TwoLayerNet in fc_net.py.
        """
        W1, b1 = self.params["W1"], self.params["b1"]
        W2, b2 = self.params["W2"], self.params["b2"]
        W3, b3 = self.params["W3"], self.params["b3"]

        # pass conv_param to the forward pass for the convolutional layer
        # Padding and stride chosen to preserve the input spatial size
        filter_size = W1.shape[2]
        conv_param = {"stride": 1, "pad": (filter_size - 1) // 2}

        # pass pool_param to the forward pass for the max-pooling layer
        pool_param = {"pool_height": 2, "pool_width": 2, "stride": 2}

        scores = None
        ############################################################################
        # TODO: Implement the forward pass for the three-layer convolutional net,  #
        # computing the class scores for X and storing them in the scores          #
        # variable.                                                                #
        #                                                                          #
        # Remember you can use the functions defined in cs231n/fast_layers.py and  #
        # cs231n/layer_utils.py in your implementation (already imported).         #
        ############################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        '''

        # 卷积 - RELU - 2x2 最大池 - 仿射 - RELU - 仿射 - SoftMax
        # conv - relu - 2x2 max pool - affine - relu - affine - softmax
        out1, cache1 = conv_forward_naive(X, W1, b1, conv_param)
        out2, cache2 = relu_forward(out1)

        out3, cache3 = max_pool_forward_naive(out2, pool_param)

        N = out3.shape[0]
        out3_5 = out3.reshape(N, -1)

        cache3_flatten = out3.shape

        out4, cache4 = affine_forward(out3_5, W2, b2)
        out5, cache5 = relu_forward(out4)

        scores, cache_scores = affine_forward(out5, W3, b3)

        '''
        # 前向传播流程修正
        # 1. 卷积层 + ReLU
        conv_out, cache_conv = conv_forward_fast(X, W1, b1, conv_param)
        relu_out, cache_relu = relu_forward(conv_out)

        # 2. 最大池化层
        pool_out, cache_pool = max_pool_forward_fast(relu_out, pool_param)

        # 3. 展平操作（将四维张量转换为二维矩阵）
        N = pool_out.shape[0]
        flatten_out = pool_out.reshape(N, -1)  # 形状变为(N, D)
        cache_flatten = pool_out.shape  # 存储原始形状供反向传播使用

        # 4. 第一个全连接层 + ReLU
        affine1_out, cache_affine1 = affine_forward(flatten_out, W2, b2)
        affine1_relu_out, cache_affine1_relu = relu_forward(affine1_out)

        # 5. 输出层（第二个全连接层）
        scores, cache_affine2 = affine_forward(affine1_relu_out, W3, b3)


        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        ############################################################################
        #                             END OF YOUR CODE                             #
        ############################################################################

        if y is None:
            return scores

        loss, grads = 0, {}
        ############################################################################
        # TODO: Implement the backward pass for the three-layer convolutional net, #
        # storing the loss and gradients in the loss and grads variables. Compute  #
        # data loss using softmax, and make sure that grads[k] holds the gradients #
        # for self.params[k]. Don't forget to add L2 regularization!               #
        #                                                                          #
        # NOTE: To ensure that your implementation matches ours and you pass the   #
        # automated tests, make sure that your L2 regularization includes a factor #
        # of 0.5 to simplify the expression for the gradient.                      #
        ############################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        '''

        loss, dscores = softmax_loss(scores, y)
        loss += 0.5 * self.reg * (np.sum(W1 ** 2) + np.sum(W2 ** 2) + np.sum(W3 ** 2))

        dhidden2, dW3, db3 = affine_backward(dscores, cache_scores)

        dhidden_relu = relu_backward(dhidden2, cache5)
        dhidden1, dW2, db2 = affine_backward(dhidden_relu, cache4)

        dpool_flatten = dhidden1.reshape(cache3_flatten)

        dmax_pool = max_pool_backward_naive(dpool_flatten, cache3)

        drelu = relu_backward(dmax_pool, cache2)

        dX, dW1, db1 = conv_backward_naive(drelu, cache1)

        dW3 += self.reg * W3
        dW2 += self.reg * W2
        dW1 += self.reg * W1

        grads = {'W1': dW1, 'b1': db1, 'W2': dW2, 'b2': db2, 'W3': dW3, 'b3': db3}

        '''
        # 计算Softmax损失和初始梯度
        loss, dscores = softmax_loss(scores, y)

        # 添加L2正则化项（所有权重）
        reg_loss = 0.5 * self.reg * (np.sum(W1**2) + np.sum(W2**2) + np.sum(W3**2))
        loss += reg_loss

        # 反向传播流程
        # 1. 输出层（第二个全连接层）
        daffine2, dW3, db3 = affine_backward(dscores, cache_affine2)
        dW3 += self.reg * W3  # 加入正则化梯度

        # 2. 第一个全连接层 + ReLU
        daffine1_relu = relu_backward(daffine2, cache_affine1_relu)
        daffine1, dW2, db2 = affine_backward(daffine1_relu, cache_affine1)
        dW2 += self.reg * W2

        # 3. 展平层的反向传播（恢复四维形状）
        dpool_flatten = daffine1.reshape(cache_flatten)

        # 4. 最大池化层反向传播
        dmax_pool = max_pool_backward_fast(dpool_flatten, cache_pool)

        # 5. ReLU层反向传播
        drelu = relu_backward(dmax_pool, cache_relu)

        # 6. 卷积层反向传播
        dX, dW1, db1 = conv_backward_fast(drelu, cache_conv)
        dW1 += self.reg * W1

        # 梯度存储
        grads = {
            'W1': dW1, 'b1': db1,
            'W2': dW2, 'b2': db2,
            'W3': dW3, 'b3': db3
        }


        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        ############################################################################
        #                             END OF YOUR CODE                             #
        ############################################################################

        return loss, grads

        
