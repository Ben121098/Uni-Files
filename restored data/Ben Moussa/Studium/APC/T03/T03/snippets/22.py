for i in range(N_sim):
    # Correction
    Gain_0 = P0@C.transpose()*np.linalg.inv(C@P0@C.transpose()+R)
    x0 = A_discrete@x0 + B_discrete@u_k + np.random.normal(0,5e-6,nx).reshape(nx,1)
    y = C@x0 + np.random.normal(0,np.sqrt(1e-3),ny).reshape(ny,1)
    x0_observer = x0_observer + Gain_0@(y-C@x0_observer)
    y_hat = C@x0_observer
    x_data.append(x0)    
    x_hat_data.append(x0_observer)
    P0 = (np.eye(3)-Gain_0@C)@P0
    # Prediction
    x0_observer = A_discrete@x0_observer + B_discrete@u_k
    P0 = A_discrete @ P0 @ A_discrete.transpose() + Q