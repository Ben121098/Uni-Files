x_k = x0
X_traj_lqr = [x0]
U_traj_lqr = []

for _ in range(sim_steps):
    
    # LQR feedback
    u_k = -K@x_k
    
    # simulate system
    x_k = system(x_k,u_k)
    
    # update data lists
    X_traj_lqr.append(x_k)
    U_traj_lqr.append(u_k)