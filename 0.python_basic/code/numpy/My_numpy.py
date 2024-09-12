import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from PIL.ImageChops import offset
from numpy.lib.utils import byte_bounds

z1=np.zeros(9).reshape(3,3)
z1_view=z1[0:2,1:3]
z1_view[...]=1
print(z1)
print(z1_view.base is z1)

z2=np.zeros(9)
z2_view=z2[np.arange(3)]
z2_view[...]=1
print(z2)
print(z2_view.base is z2)

z3=np.arange(10)
z3_view=z3[1:7:3]
z3_stride=z3.strides[0]
z3_view_stride=z3_view.strides[0]

step=z3_view_stride//z3_stride

z3_start=np.byte_bounds(z3)[0]
z3_end=np.byte_bounds(z3)[-1]
z3_view_start=np.byte_bounds(z3_view)[0]
z3_view_end=np.byte_bounds(z3_view)[-1]

offset_start=z3_view_start-z3_start
offset_stop=z3_view_end-z3_end

start=offset_start // z3.itemsize
stop=z3.size+offset_stop // z3.itemsize

print(z3[start:stop:step])
print(z3_view)

