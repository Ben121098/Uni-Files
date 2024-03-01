# Continous-time model in state space form
A = np.array([[-kAB-dvdt/VR, 0, 0],
     [kAB, -kBC-dvdt/VR, kCB],
     [0, kBC, -kCB-dvdt/VR]]).reshape(nx,nx)
B = np.array([[dvdt/VR],[0],[0]]).reshape(nx,nu)
C = np.array([[0, 1, 0]]).reshape(ny,nx)

print(A)
print(B)
print(C)