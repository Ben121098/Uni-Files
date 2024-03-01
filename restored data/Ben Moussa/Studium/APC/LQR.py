import numpy as np
import pickle
import os, sys

P = P0 = pickle.load(open("P_mat.dat","rb"))
# P = np.array([[0,0],[0,0]])
Q = np.eye(2)
A = np.array([[1,1],[0,1]])
B = np.array([[1],[1]])
K = -1
R= 1

Ps = [P]

n = 50
for k in range(n):
    P = Q + A.T@P@A - A.T@P@B@np.linalg.inv(R+B.T@P@B)@B.T@P@A
    Ps.append(P)
    
K = -np.linalg.inv(B.T@P@B+R)@B.T@P@A

print(P, P0, K, sep="\n\n")