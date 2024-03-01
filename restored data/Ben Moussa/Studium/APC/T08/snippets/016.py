# Update the terminal cost
J = J_stage  + x_terminal.T @ P @ x_terminal

# solver creation
prob = {'f':J,'x':xu,'g':g}
solver_with_terminal_set_and_penalty = nlpsol('solver','ipopt',prob)