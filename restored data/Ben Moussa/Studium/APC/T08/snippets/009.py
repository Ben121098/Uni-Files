# system matrix
A_sys = np.array([[1, 1],
                  [0, 1]])
# input matrix
B_sys = np.array([[1],
                  [1]])

# state constraints matrix
F = np.array([[ 1, 0],
              [-1, 0],
              [ 0, 1],
              [ 0,-1]])

# input constraints matrix
G = np.array([[ 1],
              [-1]])