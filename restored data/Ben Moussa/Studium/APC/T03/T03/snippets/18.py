# Pole placement
New_eigen_val = np.array([0.9, 0.8, 0.7])
K = (control.place(A_discrete.T,C.T,New_eigen_val)).T
print(K)