# matrices
Q = np.array([[1, 0],
              [0, 1]])
P = Q
R = np.array([[1]])

# stage cost
stage_cost = x.T@Q@x+ u.T@R@u
stage_cost_fcn = Function('stage_cost',[x,u],[stage_cost])

# terminal cost
terminal_cost = x.T@P@x
terminal_cost_fcn = Function('terminal_cost',[x],[terminal_cost])