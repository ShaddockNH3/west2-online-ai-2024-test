from builtins import range
import numpy as np



def affine_forward(x, w, b):
    """
    Computes the forward pass for an affine (fully-connected) layer.

    The input x has shape (N, d_1, ..., d_k) and contains a minibatch of N
    examples, where each example x[i] has shape (d_1, ..., d_k). We will
    reshape each input into a vector of dimension D = d_1 * ... * d_k, and
    then transform it to an output vector of dimension M.

    Inputs:
    - x: A numpy array containing input data, of shape (N, d_1, ..., d_k)
    - w: A numpy array of weights, of shape (D, M)
    - b: A numpy array of biases, of shape (M,)

    Returns a tuple of:
    - out: output, of shape (N, M)
    - cache: (x, w, b)
    """
    out = None
    ###########################################################################
    # TODO: Implement the affine forward pass. Store the result in out. You   #
    # will need to reshape the input into rows.                               #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    x_reshaped = x.reshape(x.shape[0], -1)
    out = np.dot(x_reshaped, w) + b

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    cache = (x, w, b)
    return out, cache


def affine_backward(dout, cache):
    """
    Computes the backward pass for an affine layer.

    Inputs:
    - dout: Upstream derivative, of shape (N, M)
    - cache: Tuple of:
      - x: Input data, of shape (N, d_1, ... d_k)
      - w: Weights, of shape (D, M)
      - b: Biases, of shape (M,)

    Returns a tuple of:
    - dx: Gradient with respect to x, of shape (N, d1, ..., d_k)
    - dw: Gradient with respect to w, of shape (D, M)
    - db: Gradient with respect to b, of shape (M,)
    """
    x, w, b = cache
    dx, dw, db = None, None, None
    ###########################################################################
    # TODO: Implement the affine backward pass.                               #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    x_reshaped = x.reshape(x.shape[0], -1)
    dw = x_reshaped.T.dot(dout)
    db = np.sum(dout, axis=0)
    dx = dout.dot(w.T)
    dx = dx.reshape(x.shape)

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx, dw, db


def relu_forward(x):
    """
    Computes the forward pass for a layer of rectified linear units (ReLUs).

    Input:
    - x: Inputs, of any shape

    Returns a tuple of:
    - out: Output, of the same shape as x
    - cache: x
    """
    out = None
    ###########################################################################
    # TODO: Implement the ReLU forward pass.                                  #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    out = np.maximum(0, x)

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    cache = x
    return out, cache


def relu_backward(dout, cache):
    """
    Computes the backward pass for a layer of rectified linear units (ReLUs).

    Input:
    - dout: Upstream derivatives, of any shape
    - cache: Input x, of same shape as dout

    Returns:
    - dx: Gradient with respect to x
    """
    dx, x = None, cache
    ###########################################################################
    # TODO: Implement the ReLU backward pass.                                 #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    dx = dout * (x>0)

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx


def batchnorm_forward(x, gamma, beta, bn_param):
    """
    Forward pass for batch normalization.

    During training the sample mean and (uncorrected) sample variance are
    computed from minibatch statistics and used to normalize the incoming data.
    During training we also keep an exponentially decaying running mean of the
    mean and variance of each feature, and these averages are used to normalize
    data at test-time.

    At each timestep we update the running averages for mean and variance using
    an exponential decay based on the momentum parameter:

    running_mean = momentum * running_mean + (1 - momentum) * sample_mean
    running_var = momentum * running_var + (1 - momentum) * sample_var

    Note that the batch normalization paper suggests a different test-time
    behavior: they compute sample mean and variance for each feature using a
    large number of training images rather than using a running average. For
    this implementation we have chosen to use running averages instead since
    they do not require an additional estimation step; the torch7
    implementation of batch normalization also uses running averages.

    Input:
    - x: Data of shape (N, D)
    - gamma: Scale parameter of shape (D,)
    - beta: Shift paremeter of shape (D,)
    - bn_param: Dictionary with the following keys:
      - mode: 'train' or 'test'; required
      - eps: Constant for numeric stability
      - momentum: Constant for running mean / variance.
      - running_mean: Array of shape (D,) giving running mean of features
      - running_var Array of shape (D,) giving running variance of features

    Returns a tuple of:
    - out: of shape (N, D)
    - cache: A tuple of values needed in the backward pass
    """

    """
    批归一化前向传播
    
    训练阶段使用小批量统计量计算样本均值和（无偏）样本方差来归一化数据。
    训练时同时维护特征的指数衰减滑动均值和方差，这些统计量将在测试阶段用于数据归一化。
    
    每个时间步通过动量参数更新滑动均值和方差：
    running_mean = momentum * running_mean + (1 - momentum) * sample_mean
    running_var = momentum * running_var + (1 - momentum) * sample_var
    
    注意：原始批归一化论文建议测试阶段使用大量训练图像计算特征统计量，
    本实现选择使用滑动平均方式（与torch7实现一致），避免额外估计步骤。

    输入：
    - x: 形状为(N, D)的数据
    - gamma: 缩放参数，形状(D,)
    - beta: 偏移参数，形状(D,)
    - bn_param: 包含以下键的字典：
      - mode: 必须为'train'或'test'
      - eps: 数值稳定常数
      - momentum: 滑动平均动量参数
      - running_mean: 形状(D,)的特征滑动均值
      - running_var: 形状(D,)的特征滑动方差

    返回元组：
    - out: 形状(N, D)的输出
    - cache: 反向传播需要的中间变量集合
    """

    mode = bn_param["mode"]
    eps = bn_param.get("eps", 1e-5)
    momentum = bn_param.get("momentum", 0.9)

    N, D = x.shape
    running_mean = bn_param.get("running_mean", np.zeros(D, dtype=x.dtype))
    running_var = bn_param.get("running_var", np.zeros(D, dtype=x.dtype))

    out, cache = None, None
    if mode == "train":
        #######################################################################
        # TODO: Implement the training-time forward pass for batch norm.      #
        # Use minibatch statistics to compute the mean and variance, use      #
        # these statistics to normalize the incoming data, and scale and      #
        # shift the normalized data using gamma and beta.                     #
        #                                                                     #
        # You should store the output in the variable out. Any intermediates  #
        # that you need for the backward pass should be stored in the cache   #
        # variable.                                                           #
        #                                                                     #
        # You should also use your computed sample mean and variance together #
        # with the momentum variable to update the running mean and running   #
        # variance, storing your result in the running_mean and running_var   #
        # variables.                                                          #
        #                                                                     #
        # Note that though you should be keeping track of the running         #
        # variance, you should normalize the data based on the standard       #
        # deviation (square root of variance) instead!                        #
        # Referencing the original paper (https://arxiv.org/abs/1502.03167)   #
        # might prove to be helpful.                                          #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        # 任务：实现训练阶段的批归一化前向传播                                #
        # 使用小批量统计量计算均值和方差，并用其归一化数据                     #
        # 使用gamma和beta对归一化后的数据进行缩放和偏移                      #
        #                                                                     #
        # 将输出存储在out变量，反向传播需要的中间变量存入cache               #
        #                                                                     #
        # 使用计算的样本均值和方差，配合动量参数更新滑动均值和方差             #
        # 注意：尽管需要跟踪滑动方差，但数据归一化应基于标准差（方差平方根）   #
        # 参考原始论文(https://arxiv.org/abs/1502.03167)可能有帮助            #

        mu = np.mean(x, axis=0, keepdims=True)
        var = np.mean((x - mu)**2, axis=0, keepdims=True)

        x_hat = (x - mu) / np.sqrt(var + eps)
        out = gamma * x_hat + beta

        running_mean = momentum*running_mean + (1-momentum)*mu
        running_var = momentum*running_var + (1-momentum)*var

        cache = (x, x_hat, mu, var, gamma, eps)


        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        #######################################################################
        #                           END OF YOUR CODE                          #
        #######################################################################
    elif mode == "test":
        #######################################################################
        # TODO: Implement the test-time forward pass for batch normalization. #
        # Use the running mean and variance to normalize the incoming data,   #
        # then scale and shift the normalized data using gamma and beta.      #
        # Store the result in the out variable.                               #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        # 任务：实现测试阶段的批归一化前向传播                                #
        # 使用滑动均值和方差归一化数据，应用gamma和beta进行缩放和偏移         #
        # 结果存入out变量                                                     #
        
        x_hat = (x - running_mean) / np.sqrt(running_var + eps)
        out = gamma * x_hat + beta
        cache = None

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        #######################################################################
        #                          END OF YOUR CODE                           #
        #######################################################################
    else:
        raise ValueError('Invalid forward batchnorm mode "%s"' % mode)

    # Store the updated running means back into bn_param
    bn_param["running_mean"] = running_mean
    bn_param["running_var"] = running_var

    return out, cache


def batchnorm_backward(dout, cache):
    """
    Backward pass for batch normalization.

    For this implementation, you should write out a computation graph for
    batch normalization on paper and propagate gradients backward through
    intermediate nodes.

    Inputs:
    - dout: Upstream derivatives, of shape (N, D)
    - cache: Variable of intermediates from batchnorm_forward.

    Returns a tuple of:
    - dx: Gradient with respect to inputs x, of shape (N, D)
    - dgamma: Gradient with respect to scale parameter gamma, of shape (D,)
    - dbeta: Gradient with respect to shift parameter beta, of shape (D,)
    """
    dx, dgamma, dbeta = None, None, None
    ###########################################################################
    # TODO: Implement the backward pass for batch normalization. Store the    #
    # results in the dx, dgamma, and dbeta variables.                         #
    # Referencing the original paper (https://arxiv.org/abs/1502.03167)       #
    # might prove to be helpful.                                              #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    x, x_hat, mu, var, gamma, eps = cache
    N, D = dout.shape  # 获取输入维度

    # 计算gamma和beta的梯度
    dgamma = np.sum(dout * x_hat, axis=0)  # 公式5
    dbeta = np.sum(dout, axis=0)          # 公式6

    # 计算中间梯度分量
    dx_hat = dout * gamma                # 公式1
    
    # 计算方差梯度分量
    dvar = np.sum( dx_hat * (x - mu) * (-0.5) * (var + eps)**(-1.5), axis=0 )  # 公式2
    
    # 计算均值梯度分量
    dmu_term1 = np.sum( dx_hat * (-1 / np.sqrt(var + eps)), axis=0 )           # 公式3第一项
    dmu_term2 = dvar * np.sum(-2 * (x - mu), axis=0) / N                      # 公式3第二项
    dmu = dmu_term1 + dmu_term2
    
    # 最终输入梯度合成
    dx = ( dx_hat / np.sqrt(var + eps) ) + \
         ( dvar * 2 * (x - mu) / N ) + \
         ( dmu / N )                         # 公式4

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return dx, dgamma, dbeta


def batchnorm_backward_alt(dout, cache):
    """
    Alternative backward pass for batch normalization.

    For this implementation you should work out the derivatives for the batch
    normalizaton backward pass on paper and simplify as much as possible. You
    should be able to derive a simple expression for the backward pass.
    See the jupyter notebook for more hints.

    Note: This implementation should expect to receive the same cache variable
    as batchnorm_backward, but might not use all of the values in the cache.

    Inputs / outputs: Same as batchnorm_backward
    """
    dx, dgamma, dbeta = None, None, None
    ###########################################################################
    # TODO: Implement the backward pass for batch normalization. Store the    #
    # results in the dx, dgamma, and dbeta variables.                         #
    #                                                                         #
    # After computing the gradient with respect to the centered inputs, you   #
    # should be able to compute gradients with respect to the inputs in a     #
    # single statement; our implementation fits on a single 80-character line.#
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    x, x_hat, mu, var, gamma, eps = cache
    N, D = x.shape
    sigma = np.sqrt(var + eps)
    
    # 计算中间梯度项
    dY = dout * gamma  # 上游梯度乘以gamma
    
    # 三项合成
    term1 = dY
    term2 = -np.mean(dY, axis=0, keepdims=True)
    term3 = -x_hat * np.mean(dY * x_hat, axis=0, keepdims=True)
    
    # 组合梯度
    dx = (term1 + term2 + term3) / sigma
    
    # 参数梯度保持不变
    dgamma = np.sum(dout * x_hat, axis=0)
    dbeta = np.sum(dout, axis=0)
    
    return dx, dgamma, dbeta

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return dx, dgamma, dbeta


def layernorm_forward(x, gamma, beta, ln_param):
    """
    Forward pass for layer normalization.

    During both training and test-time, the incoming data is normalized per data-point,
    before being scaled by gamma and beta parameters identical to that of batch normalization.

    Note that in contrast to batch normalization, the behavior during train and test-time for
    layer normalization are identical, and we do not need to keep track of running averages
    of any sort.

    Input:
    - x: Data of shape (N, D)
    - gamma: Scale parameter of shape (D,)
    - beta: Shift paremeter of shape (D,)
    - ln_param: Dictionary with the following keys:
        - eps: Constant for numeric stability

    Returns a tuple of:
    - out: of shape (N, D)
    - cache: A tuple of values needed in the backward pass
    """
    out, cache = None, None
    eps = ln_param.get("eps", 1e-5)
    ###########################################################################
    # TODO: Implement the training-time forward pass for layer norm.          #
    # Normalize the incoming data, and scale and  shift the normalized data   #
    #  using gamma and beta.                                                  #
    # HINT: this can be done by slightly modifying your training-time         #
    # implementation of  batch normalization, and inserting a line or two of  #
    # well-placed code. In particular, can you think of any matrix            #
    # transformations you could perform, that would enable you to copy over   #
    # the batch norm code and leave it almost unchanged?                      #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    mu = np.mean(x, axis=1, keepdims=True)  # 形状(N,1)
    var = np.var(x, axis=1, keepdims=True) + eps  # 形状(N,1)
    x_hat = (x - mu) / np.sqrt(var)  # 广播机制自动处理
    out = gamma * x_hat + beta  # gamma/beta形状(D,)自动广播到(N,D)

    cache = (x, x_hat, mu, var, gamma, eps)
    
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return out, cache


def layernorm_backward(dout, cache):
    """
    Backward pass for layer normalization.

    For this implementation, you can heavily rely on the work you've done already
    for batch normalization.

    Inputs:
    - dout: Upstream derivatives, of shape (N, D)
    - cache: Variable of intermediates from layernorm_forward.

    Returns a tuple of:
    - dx: Gradient with respect to inputs x, of shape (N, D)
    - dgamma: Gradient with respect to scale parameter gamma, of shape (D,)
    - dbeta: Gradient with respect to shift parameter beta, of shape (D,)
    """
    dx, dgamma, dbeta = None, None, None
    ###########################################################################
    # TODO: Implement the backward pass for layer norm.                       #
    #                                                                         #
    # HINT: this can be done by slightly modifying your training-time         #
    # implementation of batch normalization. The hints to the forward pass    #
    # still apply!                                                            #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    x, x_hat, mu, var, gamma, eps = cache
    N, D = x.shape

    # 参数梯度
    dgamma = np.sum(dout * x_hat, axis=0)  # 公式1
    dbeta = np.sum(dout, axis=0)           # 公式2
    
    # 输入梯度分解
    dx_hat = dout * gamma                  # 缩放项反向传播
    dvar = np.sum(dx_hat * (x - mu) * (-0.5) * (var**-1.5), axis=1, keepdims=True)
    dmu = np.sum(dx_hat * (-1/np.sqrt(var)), axis=1, keepdims=True) + dvar * np.mean(-2*(x - mu), axis=1, keepdims=True)
    
    dx = (dx_hat / np.sqrt(var)) + (dvar * 2*(x - mu)/D) + (dmu/D)

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx, dgamma, dbeta


def dropout_forward(x, dropout_param):
    """
    Performs the forward pass for (inverted) dropout.

    Inputs:
    - x: Input data, of any shape
    - dropout_param: A dictionary with the following keys:
      - p: Dropout parameter. We keep each neuron output with probability p.
      - mode: 'test' or 'train'. If the mode is train, then perform dropout;
        if the mode is test, then just return the input.
      - seed: Seed for the random number generator. Passing seed makes this
        function deterministic, which is needed for gradient checking but not
        in real networks.

    Outputs:
    - out: Array of the same shape as x.
    - cache: tuple (dropout_param, mask). In training mode, mask is the dropout
      mask that was used to multiply the input; in test mode, mask is None.

    NOTE: Please implement **inverted** dropout, not the vanilla version of dropout.
    See http://cs231n.github.io/neural-networks-2/#reg for more details.

    NOTE 2: Keep in mind that p is the probability of **keep** a neuron
    output; this might be contrary to some sources, where it is referred to
    as the probability of dropping a neuron output.
    """
    p, mode = dropout_param["p"], dropout_param["mode"]
    if "seed" in dropout_param:
        np.random.seed(dropout_param["seed"])

    mask = None
    out = None

    if mode == "train":
        #######################################################################
        # TODO: Implement training phase forward pass for inverted dropout.   #
        # Store the dropout mask in the mask variable.                        #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        mask = (np.random.rand(*x.shape) > p)  # 伯努利采样
        out = x * mask / (1 - p)

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        #######################################################################
        #                           END OF YOUR CODE                          #
        #######################################################################
    elif mode == "test":
        #######################################################################
        # TODO: Implement the test phase forward pass for inverted dropout.   #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        out = x

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        #######################################################################
        #                            END OF YOUR CODE                         #
        #######################################################################

    cache = (dropout_param, mask)
    out = out.astype(x.dtype, copy=False)

    return out, cache


def dropout_backward(dout, cache):
    """
    Perform the backward pass for (inverted) dropout.

    Inputs:
    - dout: Upstream derivatives, of any shape
    - cache: (dropout_param, mask) from dropout_forward.
    """
    dropout_param, mask = cache
    mode = dropout_param["mode"]
    p = dropout_param["p"]

    dx = None
    if mode == "train":
        #######################################################################
        # TODO: Implement training phase backward pass for inverted dropout   #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        dx = dout * mask / (1 - p)  # 反向传播梯度

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        #######################################################################
        #                          END OF YOUR CODE                           #
        #######################################################################
    elif mode == "test":
        dx = dout
    return dx


def conv_forward_naive(x, w, b, conv_param):
    """
    A naive implementation of the forward pass for a convolutional layer.

    The input consists of N data points, each with C channels, height H and
    width W. We convolve each input with F different filters, where each filter
    spans all C channels and has height HH and width WW.

    Input:
    - x: Input data of shape (N, C, H, W)
    - w: Filter weights of shape (F, C, HH, WW)
    - b: Biases, of shape (F,)
    - conv_param: A dictionary with the following keys:
      - 'stride': The number of pixels between adjacent receptive fields in the
        horizontal and vertical directions.
      - 'pad': The number of pixels that will be used to zero-pad the input.


    During padding, 'pad' zeros should be placed symmetrically (i.e equally on both sides)
    along the height and width axes of the input. Be careful not to modfiy the original
    input x directly.

    Returns a tuple of:
    - out: Output data, of shape (N, F, H', W') where H' and W' are given by
      H' = 1 + (H + 2 * pad - HH) / stride
      W' = 1 + (W + 2 * pad - WW) / stride
    - cache: (x, w, b, conv_param)
    """

    """
    朴素实现的卷积前向传播。

    输入包含N个数据点，每个点有C个通道，高度H和宽度W。每个输入与F个不同的滤波器进行卷积，
    每个滤波器跨越所有C个通道，具有高度HH和宽度WW。

    输入：
    - x: 输入数据，形状为(N, C, H, W)
    - w: 滤波器权重，形状为(F, C, HH, WW)
    - b: 偏置，形状为(F,)
    - conv_param: 包含以下键的字典：
      - 'stride': 相邻感受野在水平和垂直方向上的像素间隔
      - 'pad': 输入周围零填充的像素数

    填充时，'pad'个零应沿输入的高度和宽度轴对称放置（即两侧相等）。注意不要直接修改原始输入x。

    返回元组：
    - out: 输出数据，形状为(N, F, H', W')，其中H'和W'由下式计算：
      H' = 1 + (H + 2*pad - HH) // stride
      W' = 1 + (W + 2*pad - WW) // stride
    - cache: (x, w, b, conv_param)
    """

    out = None
    ###########################################################################
    # TODO: Implement the convolutional forward pass.                         #
    # Hint: you can use the function np.pad for padding.                      #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pad = conv_param.get('pad', 0)
    stride = conv_param.get('stride', 1)

    x_padded = np.pad(x, 
      ((0, 0), (0, 0),
      (pad, pad), (pad, pad)),
      mode='constant') 
    
    N, C, H, W = x.shape
    F, _, HH, WW = w.shape

    H_out = 1 + (H + 2 * pad - HH) // stride
    W_out = 1 + (W + 2 * pad - WW) // stride

    out = np.zeros((N, F, H_out, W_out))

    for n in range(N):
      for f in range(F):
        for i in range(H_out):
          for j in range(W_out):
            h_start=i*stride
            h_end=h_start+HH
            w_start=j*stride
            w_end=w_start+WW

            window=x_padded[n,:,h_start:h_end,w_start:w_end]
            out[n, f, i, j] = np.sum(window * w[f]) + b[f]

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    cache = (x, w, b, conv_param)
    return out, cache


def conv_backward_naive(dout, cache):
    """
    A naive implementation of the backward pass for a convolutional layer.

    Inputs:
    - dout: Upstream derivatives.
    - cache: A tuple of (x, w, b, conv_param) as in conv_forward_naive

    Returns a tuple of:
    - dx: Gradient with respect to x
    - dw: Gradient with respect to w
    - db: Gradient with respect to b
    """
    dx, dw, db = None, None, None
    ###########################################################################
    # TODO: Implement the convolutional backward pass.                        #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    x, w, b, conv_param = cache
    pad = conv_param['pad']
    stride = conv_param['stride']
    
    N, C, H, W = x.shape
    F, C, HH, WW = w.shape
    _, _, H_out, W_out = dout.shape
    
    # 初始化梯度
    dx = np.zeros_like(x)
    dw = np.zeros_like(w)
    db = np.zeros_like(b)
    
    # 对输入进行对称填充（与正向传播一致）
    x_padded = np.pad(x, ((0, 0), (0, 0), (pad, pad), (pad, pad)), mode='constant')
    dx_padded = np.pad(dx, ((0, 0), (0, 0), (pad, pad), (pad, pad)), mode='constant')
    
    # 计算偏置梯度
    for f in range(F):
        db[f] = np.sum(dout[:, f, :, :])
    
    # 计算权重梯度
    for n in range(N):
        for f in range(F):
            for i in range(H_out):
                for j in range(W_out):
                    h_start = i * stride
                    h_end = h_start + HH
                    w_start = j * stride
                    w_end = w_start + WW
                    
                    # 获取输入窗口
                    window = x_padded[n, :, h_start:h_end, w_start:w_end]
                    # 累加梯度
                    dw[f] += window * dout[n, f, i, j]
    
    # 计算输入梯度
    for n in range(N):
        for f in range(F):
            for i in range(H_out):
                for j in range(W_out):
                    h_start = i * stride
                    h_end = h_start + HH
                    w_start = j * stride
                    w_end = w_start + WW
                    
                    # 梯度传播到输入窗口
                    dx_padded[n, :, h_start:h_end, w_start:w_end] += w[f] * dout[n, f, i, j]
    
    # 去除填充部分
    dx = dx_padded[:, :, pad:-pad, pad:-pad]

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx, dw, db


def max_pool_forward_naive(x, pool_param):
    """
    A naive implementation of the forward pass for a max-pooling layer.

    Inputs:
    - x: Input data, of shape (N, C, H, W)
    - pool_param: dictionary with the following keys:
      - 'pool_height': The height of each pooling region
      - 'pool_width': The width of each pooling region
      - 'stride': The distance between adjacent pooling regions

    No padding is necessary here, eg you can assume:
      - (H - pool_height) % stride == 0
      - (W - pool_width) % stride == 0

    Returns a tuple of:
    - out: Output data, of shape (N, C, H', W') where H' and W' are given by
      H' = 1 + (H - pool_height) / stride
      W' = 1 + (W - pool_width) / stride
    - cache: (x, pool_param)
    """
    out = None
    ###########################################################################
    # TODO: Implement the max-pooling forward pass                            #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    N, C, H, W = x.shape
    pool_height = pool_param['pool_height']
    pool_width = pool_param['pool_width']
    stride = pool_param['stride']

    H_out = 1 + (H - pool_height) // stride
    W_out = 1 + (W - pool_width) // stride

    out = np.zeros((N, C, H_out, W_out))

    for n in range(N):
      for c in range(C):
        for i in range(H_out):
          for j in range(W_out):
            h_start=i*stride
            h_end=h_start+pool_height
            w_start=j*stride
            w_end=w_start+pool_width

            window=x[n,c,h_start:h_end,w_start:w_end]
            out[n, c, i, j] = np.max(window)

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    cache = (x, pool_param)
    return out, cache


def max_pool_backward_naive(dout, cache):
    """
    A naive implementation of the backward pass for a max-pooling layer.

    Inputs:
    - dout: Upstream derivatives
    - cache: A tuple of (x, pool_param) as in the forward pass.

    Returns:
    - dx: Gradient with respect to x
    """
    dx = None
    ###########################################################################
    # TODO: Implement the max-pooling backward pass                           #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    x, pool_param = cache
    dx = np.zeros_like(x)  # 初始化梯度为全零
    
    # 获取池化参数
    pool_height = pool_param['pool_height']
    pool_width = pool_param['pool_width']
    stride = pool_param['stride']
    
    # 获取输入输出尺寸
    N, C, H, W = x.shape
    H_out = dout.shape[2]
    W_out = dout.shape[3]
    
    # 遍历所有数据点、通道、输出位置
    for n in range(N):                  # 遍历批次
        for c in range(C):              # 遍历通道
            for i in range(H_out):      # 输出高度维度
                for j in range(W_out):  # 输出宽度维度
                    # 计算输入窗口位置
                    h_start = i * stride
                    h_end = h_start + pool_height
                    w_start = j * stride
                    w_end = w_start + pool_width
                    
                    # 提取输入窗口区域
                    window = x[n, c, h_start:h_end, w_start:w_end]
                    
                    # 找到最大值的位置（可能有多个相同最大值，取第一个）
                    max_idx = np.unravel_index(np.argmax(window), window.shape)
                    
                    # 将上游梯度传递到最大值位置
                    dx[n, c, h_start + max_idx[0], w_start + max_idx[1]] += dout[n, c, i, j]

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx


def spatial_batchnorm_forward(x, gamma, beta, bn_param):
    """
    Computes the forward pass for spatial batch normalization.

    Inputs:
    - x: Input data of shape (N, C, H, W)
    - gamma: Scale parameter, of shape (C,)
    - beta: Shift parameter, of shape (C,)
    - bn_param: Dictionary with the following keys:
      - mode: 'train' or 'test'; required
      - eps: Constant for numeric stability
      - momentum: Constant for running mean / variance. momentum=0 means that
        old information is discarded completely at every time step, while
        momentum=1 means that new information is never incorporated. The
        default of momentum=0.9 should work well in most situations.
      - running_mean: Array of shape (D,) giving running mean of features
      - running_var Array of shape (D,) giving running variance of features

    Returns a tuple of:
    - out: Output data, of shape (N, C, H, W)
    - cache: Values needed for the backward pass
    """
    out, cache = None, None

    ###########################################################################
    # TODO: Implement the forward pass for spatial batch normalization.       #
    #                                                                         #
    # HINT: You can implement spatial batch normalization by calling the      #
    # vanilla version of batch normalization you implemented above.           #
    # Your implementation should be very short; ours is less than five lines. #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    N, C, H, W = x.shape
    # 调整输入维度：(N, C, H, W) → (N*H*W, C)
    x_reshaped = x.transpose(0, 2, 3, 1).reshape(-1, C)
    # 调用标准批量归一化
    out_reshaped, bn_cache = batchnorm_forward(x_reshaped, gamma, beta, bn_param)
    # 恢复输出维度：(N*H*W, C) → (N, C, H, W)
    out = out_reshaped.reshape(N, H, W, C).transpose(0, 3, 1, 2)
    # 保存缓存（BN缓存 + 原始形状）
    cache = (bn_cache, (N, C, H, W))

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return out, cache


def spatial_batchnorm_backward(dout, cache):
    """
    Computes the backward pass for spatial batch normalization.

    Inputs:
    - dout: Upstream derivatives, of shape (N, C, H, W)
    - cache: Values from the forward pass

    Returns a tuple of:
    - dx: Gradient with respect to inputs, of shape (N, C, H, W)
    - dgamma: Gradient with respect to scale parameter, of shape (C,)
    - dbeta: Gradient with respect to shift parameter, of shape (C,)
    """
    dx, dgamma, dbeta = None, None, None

    ###########################################################################
    # TODO: Implement the backward pass for spatial batch normalization.      #
    #                                                                         #
    # HINT: You can implement spatial batch normalization by calling the      #
    # vanilla version of batch normalization you implemented above.           #
    # Your implementation should be very short; ours is less than five lines. #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    # 从缓存中提取BN缓存和原始形状
    bn_cache, (N, C, H, W) = cache
    # 调整梯度维度：(N, C, H, W) → (N*H*W, C)
    dout_reshaped = dout.transpose(0, 2, 3, 1).reshape(-1, C)
    # 调用标准BN反向传播
    dx_reshaped, dgamma, dbeta = batchnorm_backward(dout_reshaped, bn_cache)
    # 恢复梯度维度：(N*H*W, C) → (N, C, H, W)
    dx = dx_reshaped.reshape(N, H, W, C).transpose(0, 3, 1, 2)

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return dx, dgamma, dbeta


def spatial_groupnorm_forward(x, gamma, beta, G, gn_param):
    """
    Computes the forward pass for spatial group normalization.
    In contrast to layer normalization, group normalization splits each entry
    in the data into G contiguous pieces, which it then normalizes independently.
    Per feature shifting and scaling are then applied to the data, in a manner identical to that of batch normalization and layer normalization.

    Inputs:
    - x: Input data of shape (N, C, H, W)
    - gamma: Scale parameter, of shape (1, C, 1, 1)
    - beta: Shift parameter, of shape (1, C, 1, 1)
    - G: Integer mumber of groups to split into, should be a divisor of C
    - gn_param: Dictionary with the following keys:
      - eps: Constant for numeric stability

    Returns a tuple of:
    - out: Output data, of shape (N, C, H, W)
    - cache: Values needed for the backward pass
    """
    out, cache = None, None
    eps = gn_param.get("eps", 1e-5)
    ###########################################################################
    # TODO: Implement the forward pass for spatial group normalization.       #
    # This will be extremely similar to the layer norm implementation.        #
    # In particular, think about how you could transform the matrix so that   #
    # the bulk of the code is similar to both train-time batch normalization  #
    # and layer normalization!                                                #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    N,C,H,W=x.shape
    x=x.reshape(N,G,C//G,H,W)
    x_mean=np.mean(x,axis=(2,3,4),keepdims=True)
    x_var=np.var(x,axis=(2,3,4),keepdims=True)
    x_std=np.sqrt(x_var+eps)
    x_norm=(x-x_mean)/x_std
    x_norm=x_norm.reshape(N,C,H,W)
    out=gamma*x_norm+beta
    cache=(x,x_mean,x_var,x_std,x_norm,out,gamma,beta,eps,G)

    '''
    N, C, H, W = x.shape
    assert C % G == 0, "Channels must be divisible by groups"

    # 将输入数据分组：(N, C, H, W) → (N, G, C//G, H, W)
    x_group = x.reshape(N, G, C//G, H, W)
    # 计算每组均值和方差（在通道和空间维度上）
    mean = x_group.mean(axis=(2, 3, 4), keepdims=True)
    var = x_group.var(axis=(2, 3, 4), keepdims=True) + eps
    # 归一化
    x_norm_group = (x_group - mean) / np.sqrt(var)
    # 恢复形状为原始输入形状 (N, C, H, W)
    x_norm = x_norm_group.reshape(N, C, H, W)
    # 应用缩放和平移参数
    out = gamma * x_norm + beta

    # 保存反向传播所需的缓存
    cache = (x, x_norm_group, mean, var, gamma, beta, G, eps)
    '''

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return out, cache


def spatial_groupnorm_backward(dout, cache):
    """
    Computes the backward pass for spatial group normalization.

    Inputs:
    - dout: Upstream derivatives, of shape (N, C, H, W)
    - cache: Values from the forward pass

    Returns a tuple of:
    - dx: Gradient with respect to inputs, of shape (N, C, H, W)
    - dgamma: Gradient with respect to scale parameter, of shape (1, C, 1, 1)
    - dbeta: Gradient with respect to shift parameter, of shape (1, C, 1, 1)
    """
    dx, dgamma, dbeta = None, None, None

    ###########################################################################
    # TODO: Implement the backward pass for spatial group normalization.      #
    # This will be extremely similar to the layer norm implementation.        #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    '''

    x, x_norm_group, mean, var, gamma, beta, G, eps = cache
    N, C, H, W = x.shape
    group_size = C // G

    # 计算 dbeta 和 dgamma（沿批次和空间维度求和）
    dbeta = np.sum(dout, axis=(0, 2, 3), keepdims=True)
    dgamma = np.sum(dout * x_norm_group.reshape(N, C, H, W), axis=(0, 2, 3), keepdims=True)

    # 将梯度按分组重新排列
    dx_norm = dout * gamma  # (N, C, H, W)
    dx_norm_group = dx_norm.reshape(N, G, group_size, H, W)

    # 计算输入梯度 dx
    x_group = x.reshape(N, G, group_size, H, W)
    std_inv = 1.0 / np.sqrt(var + eps)
    
    # 计算三个梯度分量
    dx_group = dx_norm_group * std_inv  # 分量1：归一化梯度
    dmean = -np.sum(dx_group, axis=(2, 3, 4), keepdims=True)  # 分量2：均值梯度
    # dvar = np.sum(dx_group * (x_group - mean) * -0.5 * (var ** (-1.5)), axis=(2, 3, 4), keepdims=True)  # 分量3：方差梯度
    group_elements = group_size * H * W
    dvar = np.sum(
        dx_group * (x_group - mean) * (-0.5) * (var ** (-1.5)),
        axis=(2, 3, 4), keepdims=True
    ) / group_elements  # 关键修复：除以 group_elements
    
    # 合并梯度分量
    dx_group = dx_group + dmean / (group_size * H * W) + dvar * 2 * (x_group - mean) / (group_size * H * W)
    dx = dx_group.reshape(N, C, H, W)

    '''

    x,x_mean,x_var,x_std,x_norm,out,gamma,beta,eps,G=cache
    N,C,H,W=dout.shape
    x=x.reshape(N,G,C//G,H,W)
    
    m=C//G*H*W
    dgamma=np.sum(dout*x_norm,axis=(0,2,3),keepdims=True)
    dbeta=np.sum(dout,axis=(0,2,3),keepdims=True)
    dx_norm=(dout*gamma).reshape(N,G,C//G,H,W)
    dx_var=np.sum(dx_norm*(x-x_mean)*(-0.5)*np.power(x_var+eps,-1.5),axis=(2,3,4),keepdims=True)
    dx_mean=np.sum(dx_norm*(-1)/x_std,axis=(2,3,4),keepdims=True)+dx_var*np.sum(-2*(x-x_mean),axis=(2,3,4),keepdims=True)/m
    dx=dx_norm/x_std+dx_var*2*(x-x_mean)/m+dx_mean/m
    dx=dx.reshape(N,C,H,W)

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx, dgamma, dbeta


def svm_loss(x, y):
    """
    Computes the loss and gradient using for multiclass SVM classification.

    Inputs:
    - x: Input data, of shape (N, C) where x[i, j] is the score for the jth
      class for the ith input.
    - y: Vector of labels, of shape (N,) where y[i] is the label for x[i] and
      0 <= y[i] < C

    Returns a tuple of:
    - loss: Scalar giving the loss
    - dx: Gradient of the loss with respect to x
    """
    loss, dx = None, None

    ###########################################################################
    # TODO: Copy over your solution from A1.
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    num_classes=x.shape[1]
    num_train=x.shape[0]

    correct_class_scores=x[np.arange(num_train),y].reshape(-1, 1)

    margins = np.maximum(0, x - correct_class_scores + 1)
    margins[np.arange(num_train), y] = 0

    loss = np.sum(margins) / num_train

    dx = np.zeros_like(x)
    dx[margins > 0] = 1
    dx[np.arange(num_train), y] -= np.sum(margins > 0, axis=1)
    dx /= num_train

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return loss, dx


def softmax_loss(x, y):
    """
    Computes the loss and gradient for softmax classification.

    Inputs:
    - x: Input data, of shape (N, C) where x[i, j] is the score for the jth
      class for the ith input.
    - y: Vector of labels, of shape (N,) where y[i] is the label for x[i] and
      0 <= y[i] < C

    Returns a tuple of:
    - loss: Scalar giving the loss
    - dx: Gradient of the loss with respect to x
    """
    loss, dx = None, None

    ###########################################################################
    # TODO: Copy over your solution from A1.
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    num_train = x.shape[0]

    x = x - np.max(x, axis=1, keepdims=True)

    exp_scores = np.exp(x)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    correct_class_probs = probs[np.arange(num_train), y]
    loss = -np.sum(np.log(correct_class_probs)) / num_train

    dx = probs.copy()
    dx[np.arange(num_train), y] -= 1
    dx /= num_train

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return loss, dx
