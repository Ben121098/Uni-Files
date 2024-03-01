The tuning parameters of the Kalman filter are
1. $\underline{Q} = cov(\underline{v})$
2. $\underline{R} = cov(\underline{w})$
3. $\underline{P}(0)$: Covariance of the initial state

If $\left\|\underline{Q}\right\| > \left\|\underline{R}\right\| \rightarrow$ estimator uses more from the measurements and acts fast.\
If $\left\|\underline{Q}\right\| < \left\|\underline{R}\right\| \rightarrow$ estimator uses the measurements less and becomes slower. In this situation the estimator becomes a simulator.\
$\underline{P}(0)$: matters only for initial phase.