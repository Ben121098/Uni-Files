# Tuning paramters of the Kalmann filter 
R = np.array([0.01])
Q = np.diag([0.001, 0.001, 0.001])
P0 = 200*Q