# Q
Q = np.array([[0.001, 0],
              [0, 0.001]])
# R
R = np.array([[1.0]])

# Compute optimal feedback matrix by solving the DARE
_, _, K_lqr = dare(A_sys,B_sys,Q,R)

# convert to numpy array
K_lqr = -np.array(K_lqr)

# Update the closed-loop
A_cl = A_sys + B_sys @ K_lqr