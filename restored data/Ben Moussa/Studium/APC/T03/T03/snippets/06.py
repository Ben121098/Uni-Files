# Model in state space form
A = np.array([[1.8, -0.81],
      [1, 0.01]]).reshape(nx,nx)
B = np.array([0,-1]).reshape(nx,nu)
C = np.array([1, 0]).reshape(ny,nx)

print(A)
print(B)
print(C)