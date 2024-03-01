import numpy as np
import scipy as sp


ys = np.array([4, 3.8, 3.35, 2.8575, 2.3994, 1.9991, 1.6591, 1.3742, 1.137,0.9403,
               0.7775, 0.6427, 0.5313, 0.4391, 0.363, 0.3, 0.248, 0.205, .1694, 0.14])
x0 = np.array([10,4])
x0_real = np.array([1,1])
xs = [x0]
A = np.array([[0.5, 0.25], [0.1, 0.75]])
l1, l2 = 1.1445, 0.9252
K = np.array([[l1],[l2]])
C = np.array([[0, 1]])
xs_real = []

for k in range(1,len(ys)):
    y0 = np.array([ys[k]])
    x0 = (A-K@C)@x0 + K@y0
    xs.append(x0)
    x0_real = A@x0_real
    xs_real.append(x0_real)

xs = np.concatenate(xs,axis=0).reshape((2,-1))
# xs_real = np.concatenate(xs_real,axis=0).reshape((2,-1))

import matplotlib.pyplot as plt

# plt.figure()
# plt.plot(xs[0,:],label="x1")
# plt.plot(xs_real[0,:],label="x1_real")
# plt.legend()
# plt.grid()
    
plt.figure()
plt.plot(xs[1,:],label="x1")
plt.plot(ys,label="x2_real")
plt.legend()
plt.grid()

es = np.array([np.abs((xs[1,k]-ys[k])/ys[k]) for k in range(len(ys))])

plt.figure()
plt.plot(es)
plt.grid()

rev_A = np.linalg.inv(A)
mat_recons = rev_A.copy()
for i in range(len(ys)-3):     
    mat_recons =  mat_recons@rev_A
    
x_anf = mat_recons@x0
print(x_anf)
    