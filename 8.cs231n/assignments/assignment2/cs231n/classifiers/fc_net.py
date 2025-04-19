from builtins import range
from builtins import object
import numpy as np

from ..layers import *
from ..layer_utils import *

def affine_bn_relu_forward(x,w,b,gamma,beta,bn_param):
    a,fc_cache=affine_forward(x,w,b)
    bn_out,bn_cache= batchnorm_forward(a,gamma,beta,bn_param)
    out,relu_cache= relu_forward(bn_out)
    cache=(fc_cache,bn_cache,relu_cache)
    return out,cache

def affine_bn_relu_backward(dout,cache):
    fc_cache,bn_cache,relu_cache=cache
    dr=relu_backward(dout,relu_cache)
    dbn,dgamma,dbeta=batchnorm_backward(dr,bn_cache) 
    dx,dw,db=affine_backward(dbn,fc_cache)
    return dx,dw,db,dgamma,dbeta

def affine_ln_relu_forward(x,w,b,gamma,beta,bn_param):
    a,fc_cache=affine_forward(x,w,b)
    ln_out,ln_cache= layernorm_forward(a,gamma,beta,bn_param)
    out,relu_cache= relu_forward(ln_out)
    cache=(fc_cache,ln_cache,relu_cache)
    return out,cache

def affine_ln_relu_backward(dout,cache):
    fc_cache,ln_cache,relu_cache=cache
    dr=relu_backward(dout,relu_cache)
    dln,dgamma,dbeta=layernorm_backward(dr,ln_cache) 
    dx,dw,db=affine_backward(dln,fc_cache)
    return dx,dw,db,dgamma,dbeta

class FullyConnectedNet(object):
    """Class for a multi-layer fully connected neural network.

    Network contains an arbitrary number of hidden layers, ReLU nonlinearities,
    and a softmax loss function. This will also implement dropout and batch/layer
    normalization as options. For a network with L layers, the architecture will be

    {affine - [batch/layer norm] - relu - [dropout]} x (L - 1) - affine - softmax

    where batch/layer normalization and dropout are optional and the {...} block is
    repeated L - 1 times.

    Learnable parameters are stored in the self.params dictionary and will be learned
    using the Solver class.
    """

    """用于实现多层全连接神经网络的类。

    网络包含任意数量的隐藏层、ReLU非线性激活函数和Softmax损失函数。
    可选实现随机失活(dropout)和批量/层归一化(batch/layer normalization)。
    对于包含L层的网络，其架构为：

    {仿射层 - [批量/层归一化] - ReLU - [随机失活]} x (L - 1) - 仿射层 - Softmax

    其中批量/层归一化和随机失活为可选模块，{...}块会被重复L-1次。

    可学习参数存储在self.params字典中，并通过Solver类进行学习。
    """

    def __init__(
        self,
        hidden_dims,
        input_dim=3 * 32 * 32,
        num_classes=10,
        dropout_keep_ratio=1,
        normalization=None,
        reg=0.0,
        weight_scale=1e-2,
        dtype=np.float32,
        seed=None,
    ):
        """Initialize a new FullyConnectedNet.

        Inputs:
        - hidden_dims: A list of integers giving the size of each hidden layer.
        - input_dim: An integer giving the size of the input.
        - num_classes: An integer giving the number of classes to classify.
        - dropout_keep_ratio: Scalar between 0 and 1 giving dropout strength.
            If dropout_keep_ratio=1 then the network should not use dropout at all.
        - normalization: What type of normalization the network should use. Valid values
            are "batchnorm", "layernorm", or None for no normalization (the default).
        - reg: Scalar giving L2 regularization strength.
        - weight_scale: Scalar giving the standard deviation for random
            initialization of the weights.
        - dtype: A numpy datatype object; all computations will be performed using
            this datatype. float32 is faster but less accurate, so you should use
            float64 for numeric gradient checking.
        - seed: If not None, then pass this random seed to the dropout layers.
            This will make the dropout layers deteriminstic so we can gradient check the model.
        """

        """初始化全连接网络
        
        输入参数：
        - hidden_dims: 各隐藏层尺寸的整数列表
        - input_dim: 输入数据的维度（整数）
        - num_classes: 分类类别数量（整数）
        - dropout_keep_ratio: 0到1之间的标量，表示保留神经元的比例
            当值为1时表示不使用随机失活
        - normalization: 归一化类型，可选值为"batchnorm"、"layernorm"或None（默认）
        - reg: L2正则化强度（标量）
        - weight_scale: 权重初始化标准差（标量）
        - dtype: numpy数据类型对象，所有计算将使用该类型
            float32速度更快但精度较低，梯度检查时应使用float64
        - seed: 随机种子，传递给随机失活层以实现确定性计算
        """

        self.normalization = normalization
        self.use_dropout = dropout_keep_ratio != 1
        self.reg = reg
        self.num_layers = 1 + len(hidden_dims)
        self.dtype = dtype
        self.params = {}

        ############################################################################
        # TODO: Initialize the parameters of the network, storing all values in    #
        # the self.params dictionary. Store weights and biases for the first layer #
        # in W1 and b1; for the second layer use W2 and b2, etc. Weights should be #
        # initialized from a normal distribution centered at 0 with standard       #
        # deviation equal to weight_scale. Biases should be initialized to zero.   #
        #                                                                          #
        # When using batch normalization, store scale and shift parameters for the #
        # first layer in gamma1 and beta1; for the second layer use gamma2 and     #
        # beta2, etc. Scale parameters should be initialized to ones and shift     #
        # parameters should be initialized to zeros.                               #
        ############################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        '''
        # 待办任务：初始化网络参数，将所有值存储在self.params字典中            #
        # 第一层参数使用W1和b1，第二层使用W2和b2，依此类推                     #
        # 权重应从均值为0、标准差为weight_scale的正态分布初始化                 #
        # 偏置应初始化为零向量                                                #
        #                                                                      #
        # 使用批量归一化时，第一层的缩放和偏移参数使用gamma1和beta1表示        #
        # 第二层使用gamma2和beta2，依此类推                                   #
        # 缩放参数应初始化为1，偏移参数应初始化为0                             #

        '''

        self.params['W1'] = weight_scale * np.random.randn(input_dim, hidden_dims[0])
        self.params['b1'] = np.zeros(hidden_dims[0])
        if self.normalization is not None:
          self.params['gamma1'] = np.ones(hidden_dims[0])
          self.params['beta1'] = np.zeros(hidden_dims[0])

        for i in range(2, self.num_layers):
          self.params[f'W{i}'] = weight_scale * np.random.randn(hidden_dims[i-2], hidden_dims[i - 1])
          self.params[f'b{i}'] = np.zeros(hidden_dims[i - 1])
          if self.normalization is not None:
            self.params[f'gamma{i}'] = np.ones(hidden_dims[i - 1])
            self.params[f'beta{i}'] = np.zeros(hidden_dims[i - 1])

        self.params[f'W{self.num_layers}'] = weight_scale * np.random.randn(hidden_dims[-1], num_classes)
        self.params[f'b{self.num_layers}'] = np.zeros(num_classes)


        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        ############################################################################
        #                             END OF YOUR CODE                             #
        ############################################################################

        # When using dropout we need to pass a dropout_param dictionary to each
        # dropout layer so that the layer knows the dropout probability and the mode
        # (train / test). You can pass the same dropout_param to each dropout layer.

        # 使用随机失活时，需要向每个失活层传递包含概率和模式（训练/测试）的参数字典
        # 所有失活层可共享同一个dropout_param字典
        self.dropout_param = {}
        if self.use_dropout:
            self.dropout_param = {"mode": "train", "p": dropout_keep_ratio}
            if seed is not None:
                self.dropout_param["seed"] = seed

        # With batch normalization we need to keep track of running means and
        # variances, so we need to pass a special bn_param object to each batch
        # normalization layer. You should pass self.bn_params[0] to the forward pass
        # of the first batch normalization layer, self.bn_params[1] to the forward
        # pass of the second batch normalization layer, etc.

        # 使用批量归一化时，需要为每个BN层维护滑动均值/方差的跟踪参数
        # 前向传播时需传递对应的bn_param对象：
        # 第1个BN层使用self.bn_params[0]，第2个用self.bn_params[1]，依此类推
        self.bn_params = []
        if self.normalization == "batchnorm":
            self.bn_params = [{"mode": "train"} for i in range(self.num_layers - 1)]
        if self.normalization == "layernorm":
            self.bn_params = [{} for i in range(self.num_layers - 1)]

        # Cast all parameters to the correct datatype.
        # 确保所有参数转换为指定数据类型
        for k, v in self.params.items():
            self.params[k] = v.astype(dtype)

    def loss(self, X, y=None):
        """Compute loss and gradient for the fully connected net.
        
        Inputs:
        - X: Array of input data of shape (N, d_1, ..., d_k)
        - y: Array of labels, of shape (N,). y[i] gives the label for X[i].

        Returns:
        If y is None, then run a test-time forward pass of the model and return:
        - scores: Array of shape (N, C) giving classification scores, where
            scores[i, c] is the classification score for X[i] and class c.

        If y is not None, then run a training-time forward and backward pass and
        return a tuple of:
        - loss: Scalar value giving the loss
        - grads: Dictionary with the same keys as self.params, mapping parameter
            names to gradients of the loss with respect to those parameters.
        """

        """计算全连接网络的损失值和梯度
        
        输入参数:
        - X: 输入数据数组，形状为 (N, d_1, ..., d_k)
        - y: 标签数组，形状为 (N,)。y[i] 表示 X[i] 的标签

        返回值:
        如果 y 为 None，则运行测试阶段的前向传播并返回：
        - scores: 形状为 (N, C) 的分类得分数组，其中
            scores[i, c] 表示样本 X[i] 在类别 c 上的得分

        如果 y 不为 None，则运行训练阶段的前向+反向传播，返回元组：
        - loss: 标量损失值
        - grads: 参数字典，键与self.params相同，值为对应参数的损失梯度
        """

        X = X.astype(self.dtype)
        mode = "test" if y is None else "train"

        # Set train/test mode for batchnorm params and dropout param since they
        # behave differently during training and testing.

        # 为批量归一化和随机失活层设置训练/测试模式
        if self.use_dropout:
            self.dropout_param["mode"] = mode
        if self.normalization == "batchnorm":
            for bn_param in self.bn_params:
                bn_param["mode"] = mode
        scores = None
        ############################################################################
        # TODO: Implement the forward pass for the fully connected net, computing  #
        # the class scores for X and storing them in the scores variable.          #
        #                                                                          #
        # When using dropout, you'll need to pass self.dropout_param to each       #
        # dropout forward pass.                                                    #
        #                                                                          #
        # When using batch normalization, you'll need to pass self.bn_params[0] to #
        # the forward pass for the first batch normalization layer, pass           #
        # self.bn_params[1] to the forward pass for the second batch normalization #
        # layer, etc.                                                              #
        ############################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        '''
        # 待办任务：实现全连接网络的前向传播，计算X的分类得分并存入scores变量     #
        #                                                                       #
        # 使用随机失活时，需将self.dropout_param传递给每个失活层的前向传播       #
        #                                                                       #
        # 使用批量归一化时，需将self.bn_params[0]传递给第一层BN的前向传播        #
        # self.bn_params[1]传递给第二层BN，依此类推                  #   
        
        '''

        caches = {}
        layer_input = X

        for i in range(1,self.num_layers):
          W, b = self.params[f'W{i}'], self.params[f'b{i}']

          if self.normalization == 'batchnorm':
            gamma = self.params[f'gamma{i}']
            beta = self.params[f'beta{i}']
            layer_input, caches[f'bn_cache{i}'] = affine_bn_relu_forward(layer_input, W, b, gamma, beta, self.bn_params[i-1])
          elif self.normalization == 'layernorm':
            gamma = self.params[f'gamma{i}']
            beta = self.params[f'beta{i}']
            layer_input, caches[f'ln_cache{i}'] = affine_ln_relu_forward(layer_input, W, b, gamma, beta, self.bn_params[i-1])

          else:
            affine_out, affine_cache = affine_forward(layer_input, W, b)
            relu_out, relu_cache = relu_forward(affine_out)
            caches[f'affine_cache{i}'] = affine_cache
            caches[f'relu_cache{i}'] = relu_cache
            layer_input=relu_out
          
          if self.use_dropout:
            layer_input, dropout_cache = dropout_forward(layer_input, self.dropout_param)
            caches[f'dropout_cache{i}'] = dropout_cache
        
        W=self.params[f"W{self.num_layers}"]
        b=self.params[f"b{self.num_layers}"]
        scores,affine_cache=affine_forward(layer_input,W,b)
        caches['affine_cache' + str(self.num_layers)] = affine_cache
               

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        ############################################################################
        #                             END OF YOUR CODE                             #
        ############################################################################
        
        # If test mode return early.
        if mode == "test":
            return scores

        loss, grads = 0.0, {}
        ############################################################################
        # TODO: Implement the backward pass for the fully connected net. Store the #
        # loss in the loss variable and gradients in the grads dictionary. Compute #
        # data loss using softmax, and make sure that grads[k] holds the gradients #
        # for self.params[k]. Don't forget to add L2 regularization!               #
        #                                                                          #
        # When using batch/layer normalization, you don't need to regularize the   #
        # scale and shift parameters.                                              #
        #                                                                          #
        # NOTE: To ensure that your implementation matches ours and you pass the   #
        # automated tests, make sure that your L2 regularization includes a factor #
        # of 0.5 to simplify the expression for the gradient.                      #
        ############################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        '''
        # 待办任务：实现全连接网络的反向传播                                     #
        # 1. 将损失值存入loss变量                                                #
        # 2. 将梯度存入grads字典                                                 #
        # 3. 使用softmax计算数据损失                                             #
        # 4. 确保grads[k]存储self.params[k]的梯度                                #
        # 5. 添加L2正则化项（注意：正则化系数需包含0.5以简化梯度计算）            #
        #                                                                       #
        # 注意：使用批量/层归一化时，不需要对scale/shift参数进行正则化           #
        '''

        loss, dscores = softmax_loss(scores, y)
        W=self.params[f"W{self.num_layers}"]
        affine_cache=caches[f'affine_cache{self.num_layers}']
        d_relu_out, dW, db = affine_backward(dscores, affine_cache)
        grads[f"W{self.num_layers}"]=dW+self.reg*W
        grads[f"b{self.num_layers}"]=db
        
        for i in range(self.num_layers-1,0,-1):
          if self.use_dropout:
            d_relu_out=dropout_backward(d_relu_out,caches[f'dropout_cache{i}'])

          if self.normalization=='batchnorm':
            W=self.params[f"W{i}"]
            bn_cache = caches[f'bn_cache{i}']
            d_affine_out, dW, db, dgamma, dbeta = affine_bn_relu_backward(d_relu_out, bn_cache)
            grads[f"W{i}"]=dW+self.reg*W
            grads[f"b{i}"]=db
            grads[f"gamma{i}"]=dgamma
            grads[f"beta{i}"]=dbeta
            d_relu_out=d_affine_out
          
          elif self.normalization == 'layernorm':
            W=self.params[f"W{i}"]
            ln_cache = caches[f'ln_cache{i}']
            d_affine_out, dW, db, dgamma, dbeta = affine_ln_relu_backward(d_relu_out, ln_cache)
            grads[f"W{i}"]=dW+self.reg*W
            grads[f"b{i}"]=db
            grads[f"gamma{i}"]=dgamma
            grads[f"beta{i}"]=dbeta
            d_relu_out=d_affine_out
          
          else:
            W=self.params[f"W{i}"]
            affine_cache = caches[f'affine_cache{i}']
            relu_cache = caches[f'relu_cache{i}']
            d_affine_out = relu_backward(d_relu_out, relu_cache)
            d_relu_out, dW, db = affine_backward(d_affine_out, affine_cache)
            grads[f"W{i}"]=dW+self.reg*W
            grads[f"b{i}"]=db
        
        for i in range(1, self.num_layers + 1):
          W = self.params[f'W{i}']
          loss += 0.5 * self.reg * np.sum(W * W)  


        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        ############################################################################
        #                             END OF YOUR CODE                             #
        ############################################################################

        return loss, grads
