alpha = 0.5

# create figure
fig, ax = plt.subplots(1,1, figsize=(8,8))

# set limits and labels
ax.set_xlim([-1.1, 1.1])
ax.set_xlabel('x1')
ax.set_ylim([-1.1, 1.1])
ax.set_ylabel('x2')

# state constraints (box constraints)
state_constraints = Rectangle((-1,-1),2,2,color='C0',fill=False,linewidth=2.0)
ax.add_artist(state_constraints)

# meshgrid for contour plots
x_vals = np.linspace(-1.1,1.1,100)
y_vals = np.linspace(-1.1,1.1,100)
X, Y = np.meshgrid(x_vals, y_vals)

# input constraints
Z_input = - K[0,0] * X - K[0,1] * Y
ax.contour(X,Y,Z_input, [0.25],colors='C1',linestyles='solid',linewidths=2)
ax.contour(X,Y,Z_input, [-0.25],colors='C1',linestyles='solid',linewidths=2)

# ellipse
Z_ellipse = P[0,0] * X**2 + P[1,1] * Y**2 + P[0,1] * X * Y + P[1,0] * X * Y
ax.contour(X, Y, Z_ellipse, [alpha],colors='C2',linewidths=2,linestyles='-.')

# make legend
legend_elements = [state_constraints,Line2D([0], [0], color='C1', lw=2),Line2D([0], [0], color='C2', lw=2, ls='-.')]
ax.legend(legend_elements, ['state constraints','input constraints','ellipsoidal set'])