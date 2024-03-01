# Prediction horizon
N = 3

# Optimization variables
X = SX.sym("X",(N+1)*nx,1)
U = SX.sym("U",N*nu,1)

# Initialize palceholders
J = 0
g = []
lb_g = []
ub_g = []

# Loop for problem construction
for k in range(N):
    # 01 - Your code here!
    x_k = X[k*nx:(k+1)*nx,:]
    x_k_next = X[(k+1)*nx:(k+2)*nx,:]
    u_k = U[k*nu:(k+1)*nu,:]
    # 01

    # 02 - Your code here!
    # objective
    J += stage_cost_fcn(x_k,u_k)
    # 02
    
    # 03 - Your code here!
    # equality constraints (system equation)
    x_k_next_calc = system(x_k,u_k)
    lb_g.append(np.zeros((nx,1)))
    ub_g.append(np.zeros((nx,1)))
    g.append(x_k_next - x_k_next_calc)
    # 03
    
# Terminal cost
x_terminal = X[N*nx:(N+1)*nx,:]
J += terminal_cost_fcn(x_terminal)

# Create solver
xu = vertcat(X,U)
lbx = -np.inf*np.ones(((N+1)*nx+N*nu,1))
ubx = np.inf*np.ones(((N+1)*nx+N*nu,1))
g = vertcat(*g)
lbg = vertcat(*lb_g)
ubg = vertcat(*ub_g)

prob = {'f':J,'x':xu,'g':g}
solver = nlpsol('solver','ipopt',prob)