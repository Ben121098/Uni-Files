# Pole placement
New_eigen_val = np.array([0.3, 0.5])
K = (control.place(A.T,C.T,New_eigen_val)).T
print(K)