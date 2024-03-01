# terminal cost
terminal_cost = x.T@P@x
terminal_cost_fcn = Function('terminal_cost',[x],[terminal_cost])
