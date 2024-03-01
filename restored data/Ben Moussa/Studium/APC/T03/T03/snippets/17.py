# Discrete-time model in state space form
step_size = 0.1
A_discrete = linalg.expm(A*step_size)
B_discrete = np.linalg.inv(A) @ (linalg.expm(A*step_size) - np.eye(nx)) @ B