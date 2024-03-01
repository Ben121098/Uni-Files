Model equations which are used in Kalman filter  are given below:\
$\quad{\underline{x}_{k+1}} = \underline{A}\cdot\underline{x}_k+\underline{B}\cdot\underline{u}_k + \underline{v}_k$\
$\quad\underline{y}_{k+1} = \underline{C}\cdot\underline{x}_k+\underline{w}_k$\
where\
$\quad \underline{A}$: state matrix,\
$\quad \underline{x}_k$: state vector,\
$\quad \underline{B}$: input matrix,\
$\quad \underline{u}_k$: input vector,\
$\quad \underline{C}$: output matrix,\
$\quad \underline{y}_k$: output vector,\
$\quad \underline{v}_k$: state noise,\
$\quad \underline{w}_k$: measurement noise,\
$\quad \underline{v}_k$ and $\underline{w}_k$ are Gaussian white noise which means they are independent of each other and of $x$ and $y$. Moreover their mean value is zero.