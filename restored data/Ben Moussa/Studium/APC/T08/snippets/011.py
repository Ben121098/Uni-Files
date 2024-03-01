# Maximum number of iterations
max_iter = 100

# Initialize matrix describing the invariant set
invariant_mat = np.zeros((0,2))

# run loop
for n_f in range(max_iter):
    
    # extend the matrix describing the invariant set
    invariant_mat = np.vstack([invariant_mat, F @ mp(A_cl,n_f), G @ K @ mp(A_cl,n_f)])
    
    # termination criterion
    one_vec = np.ones((invariant_mat.shape[0],1))
    
    # compute vertices of current iterate of the maximum invariant set
    verts = compute_polytope_vertices(invariant_mat,one_vec)
    
    # compute predecessor states of the current vertices
    verts_next = [A_cl @ np.reshape(vert,(-1,1)) for vert in verts]
    
    # check if all verts lie inside the current iterate of the maximum invariant set
    in_omega = [all(invariant_mat @ vert <= one_vec) for vert in verts_next]
    
    # if all predecessor verts inside the current iterate of the maximum invariant set -> break
    if all(in_omega):
        print('Algorithm converged after ' + str(n_f+1) + ' step(s).')
        break