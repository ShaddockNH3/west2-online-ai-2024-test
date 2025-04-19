import numpy as np

import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as T
import torch.optim as optim
from torch.utils.data import sampler

import PIL

NOISE_DIM = 96

dtype = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor

def sample_noise(batch_size, dim, seed=None):
    """
    Generate a PyTorch Tensor of uniform random noise.

    Input:
    - batch_size: Integer giving the batch size of noise to generate.
    - dim: Integer giving the dimension of noise to generate.

    Output:
    - A PyTorch Tensor of shape (batch_size, dim) containing uniform
      random noise in the range (-1, 1).
    """
    if seed is not None:
        torch.manual_seed(seed)

    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    noise=torch.rand(batch_size,dim) # 形状为 (batch_size, dim)
    noise=2*noise-1 # 线性变换到 [-1, 1)
    return noise

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

def discriminator(seed=None):
    """
    Build and return a PyTorch model implementing the architecture above.
    """

    if seed is not None:
        torch.manual_seed(seed)

    model = None

    ##############################################################################
    # TODO: Implement architecture                                               #
    #                                                                            #
    # HINT: nn.Sequential might be helpful. You'll start by calling Flatten().   #
    ##############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    model=nn.Sequential(
      nn.Flatten(),

      nn.Linear(784,256),
      nn.LeakyReLU(negative_slope=0.2),

      nn.Linear(256,256),
      nn.LeakyReLU(negative_slope=0.2),

      nn.Linear(256,1),
      nn.Sigmoid()
    )

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ##############################################################################
    #                               END OF YOUR CODE                             #
    ##############################################################################
    return model

def generator(noise_dim=NOISE_DIM, seed=None):
    """
    Build and return a PyTorch model implementing the architecture above.
    """

    if seed is not None:
        torch.manual_seed(seed)

    model = None

    ##############################################################################
    # TODO: Implement architecture                                               #
    #                                                                            #
    # HINT: nn.Sequential might be helpful.                                      #
    ##############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    model=nn.Sequential(
      nn.Linear(noise_dim,1024),
      nn.ReLU(inplace=True),

      nn.Linear(1024,1024),
      nn.ReLU(inplace=True),

      nn.Linear(1024,784),
      nn.Tanh()
    )

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ##############################################################################
    #                               END OF YOUR CODE                             #
    ##############################################################################
    return model

def bce_loss(input, target):
    """
    Numerically stable version of the binary cross-entropy loss function in PyTorch.

    Inputs:
    - input: PyTorch Tensor of shape (N, ) giving scores.
    - target: PyTorch Tensor of shape (N,) containing 0 and 1 giving targets.

    Returns:
    - A PyTorch Tensor containing the mean BCE loss over the minibatch of input data.
    """
    bce = nn.BCEWithLogitsLoss()
    return bce(input.squeeze(), target)

def discriminator_loss(logits_real, logits_fake):
    """
    Computes the discriminator loss described above.

    Inputs:
    - logits_real: PyTorch Tensor of shape (N,) giving scores for the real data.
    - logits_fake: PyTorch Tensor of shape (N,) giving scores for the fake data.

    Returns:
    - loss: PyTorch Tensor containing (scalar) the loss for the discriminator.
    """
    loss = None
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    logits_real = logits_real.view(-1)
    logits_fake = logits_fake.view(-1)

    real_labels=torch.ones_like(logits_real,dtype=torch.float)
    fake_labels=torch.zeros_like(logits_fake,dtype=torch.float)

    loss_real=bce_loss(logits_real,real_labels)
    loss_fake=bce_loss(logits_fake,fake_labels)

    loss=loss_real+loss_fake

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    return loss

def generator_loss(logits_fake):
    """
    Computes the generator loss described above.

    Inputs:
    - logits_fake: PyTorch Tensor of shape (N,) giving scores for the fake data.

    Returns:
    - loss: PyTorch Tensor containing the (scalar) loss for the generator.
    """
    loss = None
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    logits_fake = logits_fake.view(-1)

    target_labels=torch.ones_like(logits_fake,dtype=torch.float)

    loss=bce_loss(logits_fake,target_labels)

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    return loss

def get_optimizer(model):
    """
    Construct and return an Adam optimizer for the model with learning rate 1e-3,
    beta1=0.5, and beta2=0.999.

    Input:
    - model: A PyTorch model that we want to optimize.

    Returns:
    - An Adam optimizer for the model with the desired hyperparameters.
    """
    optimizer = None
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    optimizer=torch.optim.Adam(
      model.parameters(),
      lr=1e-3,
      betas=(0.5,0.999)
    )

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    return optimizer

def ls_discriminator_loss(scores_real, scores_fake):
    """
    Compute the Least-Squares GAN loss for the discriminator.

    Inputs:
    - scores_real: PyTorch Tensor of shape (N,) giving scores for the real data.
    - scores_fake: PyTorch Tensor of shape (N,) giving scores for the fake data.

    Outputs:
    - loss: A PyTorch Tensor containing the loss.
    """
    loss = None
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    loss_real = torch.mean((scores_real - 1) ** 2)/2
    loss_fake = torch.mean(scores_fake ** 2)/2

    loss=loss_real+loss_fake

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    return loss

def ls_generator_loss(scores_fake):
    """
    Computes the Least-Squares GAN loss for the generator.

    Inputs:
    - scores_fake: PyTorch Tensor of shape (N,) giving scores for the fake data.

    Outputs:
    - loss: A PyTorch Tensor containing the loss.
    """
    loss = None
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    loss=torch.mean((scores_fake-1)**2)/2

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    return loss

def build_dc_classifier(batch_size):
    """
    Build and return a PyTorch model for the DCGAN discriminator implementing
    the architecture above.
    """

    ##############################################################################
    # TODO: Implement architecture                                               #
    #                                                                            #
    # HINT: nn.Sequential might be helpful.                                      #
    ##############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    '''
    卷积核 2D：32 个滤波器，5x5，步长 1
    泄漏 ReLU（alpha=0.01）
    最大池化 2x2，步长 2
    卷积核 2D：64 个滤波器，5x5，步长 1
    泄漏 ReLU（alpha=0.01）
    最大池化 2x2，步长 2
    扁平化
    全连接，输出尺寸 4 x 4 x 64
    泄漏 ReLU（alpha=0.01）
    全连接，输出尺寸 1
    '''

    model = nn.Sequential(
        # Input shape: (batch_size, 1, 28, 28)
        nn.Conv2d(1, 32, 5),  # Output: (batch_size, 32, 24, 24)
        nn.LeakyReLU(0.01),
        nn.MaxPool2d(2, 2),    # Output: (batch_size, 32, 12, 12)
        nn.Conv2d(32, 64, 5),  # Output: (batch_size, 64, 8, 8)
        nn.LeakyReLU(0.01),
        nn.MaxPool2d(2, 2),    # Output: (batch_size, 64, 4, 4)
        nn.Flatten(),          # Output: (batch_size, 64 * 4 * 4 = 1024)
        nn.Linear(1024, 1024), # Output: (batch_size, 1024)
        nn.LeakyReLU(0.01),
        nn.Linear(1024, 1)     # Output: (batch_size, 1)
    )
    return model

    '''
    return nn.Sequential(
      nn.Conv2d(1,32,5,padding=2), #(32,28,28)
      nn.LeakyReLU(0.01),
      nn.MaxPool2d(2),

      nn.Conv2d(32,64,5,padding=2),
      nn.LeakyReLU(0.01),
      nn.MaxPool2d(2),

      nn.Flatten(),
      nn.Linear(3136,1024),
      nn.LeakyReLU(0.01),
      
      nn.Linear(1024,1)
    )
    '''
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ##############################################################################
    #                               END OF YOUR CODE                             #
    ##############################################################################


def build_dc_generator(noise_dim=NOISE_DIM):
    """
    Build and return a PyTorch model implementing the DCGAN generator using
    the architecture described above.
    """

    ##############################################################################
    # TODO: Implement architecture                                               #
    #                                                                            #
    # HINT: nn.Sequential might be helpful.                                      #
    ##############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    '''
    全连接，输出尺寸为 1024
    ReLU
    BatchNorm
    全连接，输出尺寸为 7 x 7 x 128
    ReLU
    BatchNorm
    使用 Unflatten() 将图像张量重塑为尺寸为 7、7、128
    ConvTranspose2d：64 个 4x4 滤波器，步长为 2，填充相同（使用 padding=1）
    ReLU
    BatchNorm
    ConvTranspose2d：1 个 4x4 滤波器，步长为 2，填充相同（使用 padding=1）
    TanH
    应为 28x28x1 的图像，重塑为尺寸为 784 的向量（使用 Flatten()）
    '''

    return nn.Sequential(
        # 输入形状: (batch, noise_dim)
        nn.Linear(noise_dim, 1024),              # 映射到高维空间
        nn.ReLU(),
        nn.BatchNorm1d(1024),
        
        nn.Linear(1024, 7 * 7 * 128),               # 准备转置卷积输入
        nn.ReLU(),
        nn.BatchNorm1d(7 * 7 * 128),
        nn.Unflatten(1, (128,7,7)),             # 重塑为 (128,7,7)
        
        nn.ConvTranspose2d(128,64,4,2,padding=1), # 输出 (64,14,14)
        nn.ReLU(),
        nn.BatchNorm2d(64),
        
        nn.ConvTranspose2d(64,1,4,2,padding=1),  # 输出 (1,28,28)
        nn.Tanh(),
        nn.Flatten()                             # 输出形状 (784)
    )

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ##############################################################################
    #                               END OF YOUR CODE                             #
    ##############################################################################

def run_a_gan(D, G, D_solver, G_solver, discriminator_loss, generator_loss, loader_train, show_every=250,
              batch_size=128, noise_size=96, num_epochs=10):
    """
    Train a GAN!

    Inputs:
    - D, G: PyTorch models for the discriminator and generator
    - D_solver, G_solver: torch.optim Optimizers to use for training the
      discriminator and generator.
    - discriminator_loss, generator_loss: Functions to use for computing the generator and
      discriminator loss, respectively.
    - show_every: Show samples after every show_every iterations.
    - batch_size: Batch size to use for training.
    - noise_size: Dimension of the noise to use as input to the generator.
    - num_epochs: Number of epochs over the training dataset to use for training.
    """
    images = []
    iter_count = 0
    for epoch in range(num_epochs):
        for x, _ in loader_train:
            if len(x) != batch_size:
                continue
            D_solver.zero_grad()
            real_data = x.type(dtype)
            logits_real = D(2* (real_data - 0.5)).type(dtype)

            g_fake_seed = sample_noise(batch_size, noise_size).type(dtype)
            fake_images = G(g_fake_seed).detach()
            logits_fake = D(fake_images.view(batch_size, 1, 28, 28))

            d_total_error = discriminator_loss(logits_real, logits_fake)
            d_total_error.backward()
            D_solver.step()

            G_solver.zero_grad()
            g_fake_seed = sample_noise(batch_size, noise_size).type(dtype)
            fake_images = G(g_fake_seed)

            gen_logits_fake = D(fake_images.view(batch_size, 1, 28, 28))
            g_error = generator_loss(gen_logits_fake)
            g_error.backward()
            G_solver.step()

            if (iter_count % show_every == 0):
                print('Iter: {}, D: {:.4}, G:{:.4}'.format(iter_count,d_total_error.item(),g_error.item()))
                imgs_numpy = fake_images.data.cpu().numpy()
                images.append(imgs_numpy[0:16])

            iter_count += 1

    return images



class ChunkSampler(sampler.Sampler):
    """Samples elements sequentially from some offset.
    Arguments:
        num_samples: # of desired datapoints
        start: offset where we should start selecting from
    """
    def __init__(self, num_samples, start=0):
        self.num_samples = num_samples
        self.start = start

    def __iter__(self):
        return iter(range(self.start, self.start + self.num_samples))

    def __len__(self):
        return self.num_samples


class Flatten(nn.Module):
    def forward(self, x):
        N, C, H, W = x.size() # read in N, C, H, W
        return x.view(N, -1)  # "flatten" the C * H * W values into a single vector per image

class Unflatten(nn.Module):
    """
    An Unflatten module receives an input of shape (N, C*H*W) and reshapes it
    to produce an output of shape (N, C, H, W).
    """
    def __init__(self, N=-1, C=128, H=7, W=7):
        super(Unflatten, self).__init__()
        self.N = N
        self.C = C
        self.H = H
        self.W = W
    def forward(self, x):
        return x.view(self.N, self.C, self.H, self.W)

def initialize_weights(m):
    if isinstance(m, nn.Linear) or isinstance(m, nn.ConvTranspose2d):
        nn.init.xavier_uniform_(m.weight.data)

def preprocess_img(x):
    return 2 * x - 1.0

def deprocess_img(x):
    return (x + 1.0) / 2.0

def rel_error(x,y):
    return np.max(np.abs(x - y) / (np.maximum(1e-8, np.abs(x) + np.abs(y))))

def count_params(model):
    """Count the number of parameters in the model. """
    param_count = np.sum([np.prod(p.size()) for p in model.parameters()])
    return param_count
