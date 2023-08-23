import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import pickle
import casadi
from Kolonne_8_Boeden import template_model
from Kolonne_8_Boeden import template_simulator

## Constants
# constants_str='e0_greek_rho_Ldummy = 45.95 = e0_M_i1 = 0.046069 = e0_M_i2 = 0.018015 = e0_M_i3 = 0.02801 = e0_P_c_i1 = 61.48 = e0_P_c_i2 = 220.64 = e0_Param_VDI2_A_i1 = -8.33801 = e0_Param_hLV_A_i1 = 37.364136 = e0_Param_hL_A_i1 = -286.5152 = e0_Param_VDI2_A_i2 = -7.86975 = e0_Param_hLV_A_i2 = 54.697876 = e0_Param_hL_A_i2 = -306.6468 = e0_Param_hLV_A_i3 = -8.673213 = e0_Param_hL_A_i3 = 0.0 = e0_Param_VDI2_B_i1 = 0.08719 = e0_Param_hLV_B_i1 = 0.21758129 = e0_Param_hL_B_i1 = -0.17589763 = e0_Param_VDI2_B_i2 = 1.90561 = e0_Param_hLV_B_i2 = -0.02827908 = e0_Param_hL_B_i2 = 0.06390862 = e0_Param_hLV_B_i3 = 0.028969195 = e0_Param_hL_B_i3 = 0.0 = e0_Param_VDI2_C_i1 = -3.30578 = e0_Param_hLV_C_i1 = -0.0013882424 = e0_Param_hL_C_i1 = 0.0013536256 = e0_Param_VDI2_C_i2 = -2.30891 = e0_Param_hLV_C_i2 = -6.08415E-5 = e0_Param_hL_C_i2 = 5.03617E-5 = e0_Param_hLV_C_i3 = 1.1047E-6 = e0_Param_hL_C_i3 = 0.0 = e0_Param_VDI2_D_i1 = -0.25986 = e0_Param_hLV_D_i1 = 3.3797E-6 = e0_Param_hL_D_i1 = -3.1434E-6 = e0_Param_VDI2_D_i2 = -2.06472 = e0_Param_hLV_D_i2 = 2.024E-7 = e0_Param_hL_D_i2 = -1.833E-7 = e0_Param_hLV_D_i3 = -3.7E-9 = e0_Param_hL_D_i3 = 0.0 = e0_Param_hLV_E_i1 = -3.3E-9 = e0_Param_hL_E_i1 = 3.1E-9 = e0_Param_hLV_E_i2 = -3.0E-10 = e0_Param_hL_E_i2 = 3.0E-10 = e0_Param_hLV_E_i3 = 0.0 = e0_Param_hL_E_i3 = 0.0 = e0_Param_Labs_sharp = 1.0E-6 = e0_Param_Ldirac_sharp = 1.0E-6 = e0_Param_Lsig_sharp = 1.0E-6 = e0_Param_N2max_sharp = 1.0E-6 = e0_Param_PCsig_sharp = 1.0E-6 = e0_Param_SVmax_sharp = 1.0E-6 = e0_Param_Vmax_sharp = 1.0E-6 = e0_Param_Vmin_sharp = 1.0E-6 = e0_Param_mid_sharp = 1.0E-6 = e0_R = 8.314 = e0_T_c_i1 = 513.9 = e0_T_c_i2 = 647.1 = e0_a_packing = 500.0 = e0_g = 9.81'
# conslist=constants_str.split(" = ")

# condss = []
# for c in condlist:
#     try:
#         float(c)
#     except:
#         condss.append(c)
        
# mes = ""
# for c in condss:
#     mes = mes + "{} = trajectory['Flowsheet.{}'][init_ind]\n".format(c,c)
    
# with open('output.txt', 'w') as file:
#     file.write(mes)
    
    
    
    
## z0
# with open('./Data/Kolonne_8_Boesden_Textabschnitt.txt', 'r') as file:
#     daevar_str =  file.read()

# daevar_list = []

# # print(daevar_str)
# daevar_list=[sub.split(" = ") [0] for sub in daevar_str.split("\n")]
# DAE_vars = [var[14:-2] for var in daevar_list]
# print(DAE_vars)

# model = template_model()
# sim = template_simulator(model)

# n = np.random.randint(len(daevar_list))
# boole = DAE_vars[n] in list(sim.z0.keys())
# print(boole)

# pickle.dump(DAE_vars,open("./Data/DAE_variables.dat","wb"))

# DAE_vars = pickle.load(open("./Data/DAE_variables.dat","rb"))
# mes = ""
# for v in DAE_vars:
#     mes = mes + "simulator.z0['{}'] = trajectory['Flowsheet.'+'{}'][init_ind]\n".format(v,v)
    
# with open('output.txt', 'w') as file:
#     file.write(mes)








# u0
with open('./Data/Kolonne_8_Boesden_Textabschnitt.txt', 'r') as file:
    inputvar_str =  file.read()

inputvar_list = []

# print(daevar_str)
inputvar_list=[sub.split(" = ") [0] for sub in inputvar_str.split("\n")]
INPUT_vars = [var[14:-2] for var in inputvar_list]
print(INPUT_vars)

model = template_model()
sim = template_simulator(model)

n = np.random.randint(len(inputvar_list))
boole = all([INPUT_vars[n] in list(sim.u0.keys()) for n in range(len(INPUT_vars))])
print(boole)

pickle.dump(INPUT_vars,open("./Data/Input_variables.dat","wb"))

INPUT_vars = pickle.load(open("./Data/Input_variables.dat","rb"))

mes = ""
for u in INPUT_vars:
    mes = mes + "simulator.u0['{}'] = trajectory[Flowsheet.'{}'][idx]\n".format(u,u)
    
with open('output.txt', 'w') as file:
    file.write(mes)





# mes = ""
# for u in INPUT_vars:
#     mes = mes + "simulator.u0['{}'] = trajectory['{}'][idx]\n".format(u,u)
    
# with open('us.txt', 'w') as file:
#     file.write(mes)






# ## x0
# order_state_var = ["e0_HU_st0_i1", "e0_HU_st0_i2", "e0_HU_st0_i3", "e0_HU_st1_i1", "e0_HU_st2_i1", "e0_HU_st3_i1", "e0_HU_st4_i1", "e0_HU_st5_i1", "e0_HU_st6_i1", "e0_HU_st7_i1", "e0_HU_st8_i1", "e0_HU_st1_i2", "e0_HU_st2_i2", "e0_HU_st3_i2", "e0_HU_st4_i2", "e0_HU_st5_i2", "e0_HU_st6_i2", "e0_HU_st7_i2", "e0_HU_st8_i2", "e0_HU_st1_i3", "e0_HU_st2_i3", "e0_HU_st3_i3", "e0_HU_st4_i3", "e0_HU_st5_i3", "e0_HU_st6_i3", "e0_HU_st7_i3", "e0_HU_st8_i3", "e0_U_st1", "e0_U_st2", "e0_U_st3", "e0_U_st4", "e0_U_st5", "e0_U_st6", "e0_U_st7", "e0_U_st0", "e0_U_st8", "e0_HU_st9_i1", "e0_HU_st9_i2", "e0_HU_st9_i3", "e0_U_st9", ]
# pickle.dump(order_state_var,open("./Data/State_variables.dat","wb"))
# STATE_vars = pickle.load(open("./Data/State_variables.dat","rb"))
# mes = ""
# for x in STATE_vars:
#     mes = mes + "simulator.x0['{}'] = trajectory['Flowsheet.{}'][init_ind]\n".format(x,x)
    
# with open('output.txt', 'w') as file:
#     file.write(mes)






















