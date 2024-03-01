# add terminal constraint
g_.append(x_terminal.T@P@x_terminal)
lb_g.append(-np.inf)
ub_g.append(alpha)

g = vertcat(*g_)
lbg = vertcat(*lb_g)
ubg = vertcat(*ub_g)

# solver creation
prob = {'f':J,'x':xu,'g':g}
solver_with_terminal_set = nlpsol('solver','ipopt',prob)