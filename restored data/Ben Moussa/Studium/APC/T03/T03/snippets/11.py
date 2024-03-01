for i in range(N_sim):
    y = C@x0
    x0 = A@x0 + B@u
    x_data.append(x0)
    
    y_hat = C@x0_observer
    x0_observer = A@x0_observer + B@u + K@(y-y_hat)
    x_hat_data.append(x0_observer)