# Luenberger observer
for i in range(N_sim):
    y = C@x0 + np.random.normal(0,np.sqrt(1e-3),ny).reshape(ny,1)
    x0 = A_discrete@x0 + B_discrete@u_k + np.random.normal(0,5e-6,nx).reshape(nx,1)
    x_data.append(x0)
    
    y_hat = C@x0_observer
    x0_observer = A_discrete@x0_observer + B_discrete@u_k + K@(y-y_hat)
    x_hat_data.append(x0_observer)