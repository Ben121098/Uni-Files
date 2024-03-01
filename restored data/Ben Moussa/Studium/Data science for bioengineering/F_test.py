import numpy as np
import pandas as pd
import casadi as cd
import scipy.stats as stats
from Python_File import SHFdata

# %%

sh = SHFdata()
code = "AB"
gauss = True
# gauss = False
xs, ys = sh.all_data[code]
y_hats1 = sh.gompertz_predict(xs,code=code,gauss=gauss)
y_hats2 = sh.logistic_predict(xs,code=code,gauss=gauss)
y_hats3 =  sh.richard_predict(xs,code=code)

print(sh.calculate_R(y_hats1, ys))
print(sh.calculate_R(y_hats2, ys))
print(sh.calculate_R(y_hats3, ys))

# sh.linear_fit(3, 10)
# y_hats4 = sh.linear_predict(xs)
# %% compare gompertz to richard

n= len(xs)
var_g = np.sum((ys-y_hats4)**2)
var_r = np.sum((ys-y_hats3)**2)
df_g = n-1
df_r = n-2
f_calc1 = ((var_g-var_r)/(df_g-df_r))/(var_r/df_r)
f_calc2 = ((var_r-var_g)/(df_r-df_g))/(var_g/df_g)

p_value1 = stats.f.cdf(f_calc1, df_g, df_r)
p_value2 = stats.f.cdf(f_calc2, df_r, df_g)
p = stats.f.cdf((var_g/var_r)**(-1),df_g,df_r)
print(p_value1,p_value2,p)

# %% Validierung

s = SHFdata()
gauss = False
ps1 = s.gompertz(code="AB",gauss=gauss)
ps2 = s.gompertz(code="ab",gauss=gauss)

print(ps1,ps2,sep="\n")

s.plot_raw(code=["AB","Ab","aB","ab"],point="-x",save=True)

