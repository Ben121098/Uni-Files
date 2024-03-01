# state feedback matrix
K = np.array([[-1, -1]])

# closed-loop system
A_cl = A_sys+B_sys@K