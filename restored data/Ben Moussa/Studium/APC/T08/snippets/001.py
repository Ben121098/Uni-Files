# system matrix
A = np.array([[4, 3],
              [4, 1]])
# input matrix
B = np.array([[1],
              [1]])
# states
nx = A.shape[1]
x = SX.sym("x",nx,1)

# inputs
nu = B.shape[1]
u = SX.sym("u",nu,1)

# system equation expression
x_next = A@x + B@u

# system equation CasADi function
system = Function("sys",[x,u],[x_next])