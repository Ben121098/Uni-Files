%%capture
# initial state
x_k = x0

# initialize lists to hold the solution
X_traj = [x0]
U_traj = []
for _ in range(sim_steps):

    # update initial condition
    lbx[:nx]=x_k
    ubx[:nx]=x_k

    # solve MPC problem
    res = solver(lbx=lbx,ubx=ubx,lbg=lbg,ubg=ubg)

    # extract optimal input
    u_k = res['x'][(N+1)*nx:(N+1)*nx+nu,:]

    # simulate system
    x_k = system(x_k,u_k)

    # update data lists
    X_traj.append(x_k)
    U_traj.append(u_k)
