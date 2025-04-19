import numpy as np

from ..rnn_layers import *


class CaptioningRNN:
    """
    A CaptioningRNN produces captions from image features using a recurrent
    neural network.

    The RNN receives input vectors of size D, has a vocab size of V, works on
    sequences of length T, has an RNN hidden dimension of H, uses word vectors
    of dimension W, and operates on minibatches of size N.

    Note that we don't use any regularization for the CaptioningRNN.
    """


    """
    该图像描述模型使用循环神经网络从图像特征生成文字描述。

    RNN接收维度为D的输入向量，词汇表大小为V，处理长度为T的序列，
    隐藏层维度为H，词向量维度为W，支持批量大小为N。

    注意：本模型未使用任何正则化方法。
    """

    def __init__(
        self,
        word_to_idx,
        input_dim=512,
        wordvec_dim=128,
        hidden_dim=128,
        cell_type="rnn",
        dtype=np.float32,
    ):
        """
        Construct a new CaptioningRNN instance.

        Inputs:
        - word_to_idx: A dictionary giving the vocabulary. It contains V entries,
          and maps each string to a unique integer in the range [0, V).
        - input_dim: Dimension D of input image feature vectors.
        - wordvec_dim: Dimension W of word vectors.
        - hidden_dim: Dimension H for the hidden state of the RNN.
        - cell_type: What type of RNN to use; either 'rnn' or 'lstm'.
        - dtype: numpy datatype to use; use float32 for training and float64 for
          numeric gradient checking.
        """

        """
        初始化图像描述模型实例。

        输入参数:
        - word_to_idx: 词汇表字典，包含V个条目，将每个字符串映射到唯一整数索引（范围[0, V)）
        - input_dim: 输入图像特征向量的维度D
        - wordvec_dim: 词向量的维度W
        - hidden_dim: RNN隐藏状态的维度H
        - cell_type: RNN类型，可选'rnn'或'lstm'
        - dtype: numpy数据类型，训练时使用float32，梯度检查时使用float64
        """

        if cell_type not in {"rnn", "lstm"}:
            raise ValueError('Invalid cell_type "%s"' % cell_type)

        self.cell_type = cell_type
        self.dtype = dtype
        self.word_to_idx = word_to_idx
        self.idx_to_word = {i: w for w, i in word_to_idx.items()}
        self.params = {}

        vocab_size = len(word_to_idx)

        self._null = word_to_idx["<NULL>"]
        self._start = word_to_idx.get("<START>", None)
        self._end = word_to_idx.get("<END>", None)

        # Initialize word vectors
        # 初始化词向量
        self.params["W_embed"] = np.random.randn(vocab_size, wordvec_dim)
        self.params["W_embed"] /= 100

        # Initialize CNN -> hidden state projection parameters
        # 初始化CNN特征到隐藏状态的投影参数
        self.params["W_proj"] = np.random.randn(input_dim, hidden_dim)
        self.params["W_proj"] /= np.sqrt(input_dim)
        self.params["b_proj"] = np.zeros(hidden_dim)

        # Initialize parameters for the RNN
        # 初始化RNN参数
        dim_mul = {"lstm": 4, "rnn": 1}[cell_type]
        self.params["Wx"] = np.random.randn(wordvec_dim, dim_mul * hidden_dim)
        self.params["Wx"] /= np.sqrt(wordvec_dim)
        self.params["Wh"] = np.random.randn(hidden_dim, dim_mul * hidden_dim)
        self.params["Wh"] /= np.sqrt(hidden_dim)
        self.params["b"] = np.zeros(dim_mul * hidden_dim)

        # Initialize output to vocab weights
        # 初始化隐藏状态到词汇表的变换参数
        self.params["W_vocab"] = np.random.randn(hidden_dim, vocab_size)
        self.params["W_vocab"] /= np.sqrt(hidden_dim)
        self.params["b_vocab"] = np.zeros(vocab_size)

        # Cast parameters to correct dtype
        # 转换参数数据类型
        for k, v in self.params.items():
            self.params[k] = v.astype(self.dtype)

    def loss(self, features, captions):
        """
        Compute training-time loss for the RNN. We input image features and
        ground-truth captions for those images, and use an RNN (or LSTM) to compute
        loss and gradients on all parameters.

        Inputs:
        - features: Input image features, of shape (N, D)
        - captions: Ground-truth captions; an integer array of shape (N, T + 1) where
          each element is in the range 0 <= y[i, t] < V

        Returns a tuple of:
        - loss: Scalar loss
        - grads: Dictionary of gradients parallel to self.params
        """

        """
        计算训练阶段的损失值。输入图像特征和真实描述，
        使用RNN/LSTM计算所有参数的损失和梯度。

        输入参数:
        - features: 输入图像特征，形状(N, D)
        - captions: 真实描述，整型数组形状(N, T+1)，每个元素范围[0, V)

        返回元组:
        - loss: 标量损失值
        - grads: 与self.params结构相同的梯度字典
        """

        # Cut captions into two pieces: captions_in has everything but the last word
        # and will be input to the RNN; captions_out has everything but the first
        # word and this is what we will expect the RNN to generate. These are offset
        # by one relative to each other because the RNN should produce word (t+1)
        # after receiving word t. The first element of captions_in will be the START
        # token, and the first element of captions_out will be the first word.
        captions_in = captions[:, :-1]
        captions_out = captions[:, 1:]

        # You'll need this
        mask = captions_out != self._null

        # Weight and bias for the affine transform from image features to initial
        # hidden state
        W_proj, b_proj = self.params["W_proj"], self.params["b_proj"]

        # Word embedding matrix
        W_embed = self.params["W_embed"]

        # Input-to-hidden, hidden-to-hidden, and biases for the RNN
        Wx, Wh, b = self.params["Wx"], self.params["Wh"], self.params["b"]

        # Weight and bias for the hidden-to-vocab transformation.
        W_vocab, b_vocab = self.params["W_vocab"], self.params["b_vocab"]

        loss, grads = 0.0, {}
        ############################################################################
        # TODO: Implement the forward and backward passes for the CaptioningRNN.   #
        # In the forward pass you will need to do the following:                   #
        # (1) Use an affine transformation to compute the initial hidden state     #
        #     from the image features. This should produce an array of shape (N, H)#
        # (2) Use a word embedding layer to transform the words in captions_in     #
        #     from indices to vectors, giving an array of shape (N, T, W).         #
        # (3) Use either a vanilla RNN or LSTM (depending on self.cell_type) to    #
        #     process the sequence of input word vectors and produce hidden state  #
        #     vectors for all timesteps, producing an array of shape (N, T, H).    #
        # (4) Use a (temporal) affine transformation to compute scores over the    #
        #     vocabulary at every timestep using the hidden states, giving an      #
        #     array of shape (N, T, V).                                            #
        # (5) Use (temporal) softmax to compute loss using captions_out, ignoring  #
        #     the points where the output word is <NULL> using the mask above.     #
        #                                                                          #
        #                                                                          #
        # Do not worry about regularizing the weights or their gradients!          #
        #                                                                          #
        # In the backward pass you will need to compute the gradient of the loss   #
        # with respect to all model parameters. Use the loss and grads variables   #
        # defined above to store loss and gradients; grads[k] should give the      #
        # gradients for self.params[k].                                            #
        #                                                                          #
        # Note also that you are allowed to make use of functions from layers.py   #
        # in your implementation, if needed.                                       #
        ############################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        # TODO: 实现CaptioningRNN的前向传播和反向传播                          #
        # 前向传播需要完成以下步骤:                                            #
        # (1) 使用仿射变换将图像特征转换为初始隐藏状态，得到形状(N, H)的数组   #
        # (2) 使用词嵌入层将输入描述中的词索引转换为向量，得到形状(N, T, W)     #
        # (3) 使用RNN/LSTM处理词向量序列，生成各时间步的隐藏状态(N, T, H)       #
        # (4) 使用时序仿射变换将隐藏状态转换为词汇表分数(N, T, V)              #
        # (5) 使用时序softmax计算损失，通过掩码忽略NULL位置的损失              #
        #                                                                       #
        # 注意：暂不需要考虑参数正则化                                         #
        #                                                                       #
        # 反向传播需要计算损失对各参数的梯度，梯度应存储在grads字典中          #
        # 提示：可以使用rnn_layers.py中的层函数                                #

        # features(N,D)
        h0,cache_affine=affine_forward(features,W_proj, b_proj)
        # (N, H)
        
        #x: Integer array of shape (N, T)
        word_vectors,cache_embedding=word_embedding_forward(captions_in, W_embed)
        # (N, T, W)

        #x: Input data for the entire timeseries, of shape (N, T, W)
        h_states,cache_rnn=rnn_forward(word_vectors, h0, Wx, Wh, b)
        # (N, T, H)

        # 输入: h_states (N,T,H) -> 输出: scores (N,T,V)
        scores, cache_temporal = temporal_affine_forward(h_states, W_vocab, b_vocab)

        # 输入: scores (N,T,V), captions_out (N,T) -> 输出: loss (标量)
        loss, dscores = temporal_softmax_loss(scores, captions_out, mask)

        # --- 反向传播 ---
        # (4) 梯度: 时序仿射层
        dh_states, grads["W_vocab"], grads["b_vocab"] = temporal_affine_backward(dscores, cache_temporal)
        
        # (3) 梯度: RNN层
        dword_vectors, dh0, grads["Wx"], grads["Wh"], grads["b"] = rnn_backward(dh_states, cache_rnn)
        
        # (2) 梯度: 词嵌入层
        grads["W_embed"] = word_embedding_backward(dword_vectors, cache_embedding)
        
        # (1) 梯度: 投影层
        _, grads["W_proj"], grads["b_proj"] = affine_backward(dh0, cache_affine)


        '''
        # --- 前向传播 ---
        # (1) 图像特征到初始隐藏状态
        h0, cache_affine = affine_forward(features, W_proj, b_proj)
        
        # (2) 词嵌入
        word_vectors, cache_embed = word_embedding_forward(captions_in, W_embed)
        
        # (3) RNN处理序列
        if self.cell_type == 'rnn':
            h_states, cache_rnn = rnn_forward(word_vectors, h0, Wx, Wh, b)
        else:
            raise NotImplementedError("LSTM暂未实现")
        
        # (4) 时序仿射到词汇表
        scores, cache_temporal = temporal_affine_forward(h_states, W_vocab, b_vocab)
        
        # (5) 计算损失
        loss, dscores = temporal_softmax_loss(scores, captions_out, mask)

        # --- 反向传播 ---
        # (4) 梯度: 时序仿射层
        dh_states, grads["W_vocab"], grads["b_vocab"] = temporal_affine_backward(dscores, cache_temporal)
        
        # (3) 梯度: RNN层
        dword_vectors, dh0, grads["Wx"], grads["Wh"], grads["b"] = rnn_backward(dh_states, cache_rnn)
        
        # (2) 梯度: 词嵌入层
        grads["W_embed"] = word_embedding_backward(dword_vectors, cache_embed)
        
        # (1) 梯度: 投影层
        _, grads["W_proj"], grads["b_proj"] = affine_backward(dh0, cache_affine)
        '''

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        ############################################################################
        #                             END OF YOUR CODE                             #
        ############################################################################

        return loss, grads

    def sample(self, features, max_length=30):
        """
        Run a test-time forward pass for the model, sampling captions for input
        feature vectors.

        At each timestep, we embed the current word, pass it and the previous hidden
        state to the RNN to get the next hidden state, use the hidden state to get
        scores for all vocab words, and choose the word with the highest score as
        the next word. The initial hidden state is computed by applying an affine
        transform to the input image features, and the initial word is the <START>
        token.

        For LSTMs you will also have to keep track of the cell state; in that case
        the initial cell state should be zero.

        Inputs:
        - features: Array of input image features of shape (N, D).
        - max_length: Maximum length T of generated captions.

        Returns:
        - captions: Array of shape (N, max_length) giving sampled captions,
          where each element is an integer in the range [0, V). The first element
          of captions should be the first sampled word, not the <START> token.
        """

        """
        运行测试阶段的前向传播，为输入特征生成描述。

        每个时间步：
        1. 嵌入当前词
        2. 将当前词向量和前一隐藏状态输入RNN得到下一隐藏状态
        3. 使用隐藏状态生成词汇表分数
        4. 选择最高分数对应的词作为下一单词

        初始隐藏状态通过对图像特征做仿射变换得到，初始词为<START>标记。
        对于LSTM需要额外维护细胞状态，初始细胞状态设为0。

        输入参数:
        - features: 输入图像特征，形状(N, D)
        - max_length: 生成描述的最大长度T

        返回:
        - captions: 生成的描述数组，形状(N, max_length)，元素为词索引
        """
        N = features.shape[0]
        captions = self._null * np.ones((N, max_length), dtype=np.int32)

        # Unpack parameters
        W_proj, b_proj = self.params["W_proj"], self.params["b_proj"]
        W_embed = self.params["W_embed"]
        Wx, Wh, b = self.params["Wx"], self.params["Wh"], self.params["b"]
        W_vocab, b_vocab = self.params["W_vocab"], self.params["b_vocab"]

        ###########################################################################
        # TODO: Implement test-time sampling for the model. You will need to      #
        # initialize the hidden state of the RNN by applying the learned affine   #
        # transform to the input image features. The first word that you feed to  #
        # the RNN should be the <START> token; its value is stored in the         #
        # variable self._start. At each timestep you will need to do to:          #
        # (1) Embed the previous word using the learned word embeddings           #
        # (2) Make an RNN step using the previous hidden state and the embedded   #
        #     current word to get the next hidden state.                          #
        # (3) Apply the learned affine transformation to the next hidden state to #
        #     get scores for all words in the vocabulary                          #
        # (4) Select the word with the highest score as the next word, writing it #
        #     (the word index) to the appropriate slot in the captions variable   #
        #                                                                         #
        # For simplicity, you do not need to stop generating after an <END> token #
        # is sampled, but you can if you want to.                                 #
        #                                                                         #
        # HINT: You will not be able to use the rnn_forward or lstm_forward       #
        # functions; you'll need to call rnn_step_forward or lstm_step_forward in #
        # a loop.                                                                 #
        #                                                                         #
        # NOTE: we are still working over minibatches in this function. Also if   #
        # you are using an LSTM, initialize the first cell state to zeros.        #
        ###########################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        # TODO: 实现测试阶段采样逻辑                                          #
        # 关键步骤:                                                          #
        # 1. 初始化隐藏状态（对图像特征做仿射变换）                          #
        # 2. 首词使用<START>标记（索引存储在self._start）                    #
        # 3. 每个时间步：                                                   #
        #    a) 嵌入前一词                                                  #
        #    b) 执行RNN/LSTM步骤获取新隐藏状态                              #
        #    c) 生成词汇分数并选择最高分词                                  #
        # 注意：                                                            #
        # - 仍需要支持批量处理                                              #
        # - LSTM需要初始化细胞状态为0                                       #
        # - 不需要在生成<END>后停止，但可以自行实现                          #
        # 提示：需要循环调用rnn_step_forward/lstm_step_forward             #

        # 初始化隐藏状态和细胞状态
        h, _ = affine_forward(features, W_proj, b_proj)  # (N, H)
        c = np.zeros_like(h) if self.cell_type == 'lstm' else None
        
        # 初始化当前词为<START>标记，形状(N, 1)
        current_word = np.full((N, 1), self._start)
        
        for t in range(max_length):
          # 1. 词嵌入（展平为(N, W)）
          word_vecs, _ = word_embedding_forward(current_word, W_embed)
          word_vecs = word_vecs.squeeze(axis=1)  # (N, W)
            
          # 2. RNN/LSTM前向传播
          if self.cell_type == 'rnn':
            h, _ = rnn_step_forward(word_vecs, h, Wx, Wh, b)
          else:  # LSTM
            h, c, _ = lstm_step_forward(word_vecs, h, c, Wx, Wh, b)
            
          # 3. 生成词汇分数并采样
          scores, _ = affine_forward(h, W_vocab, b_vocab)  # (N, V)
          next_word = np.argmax(scores, axis=1)            # (N,)
            
          # 4. 存储结果并准备下一时间步输入
          captions[:, t] = next_word
          current_word = next_word.reshape(-1, 1)  # 保持(N, 1)形状

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        ############################################################################
        #                             END OF YOUR CODE                             #
        ############################################################################
        return captions
