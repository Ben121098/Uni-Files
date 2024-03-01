import numpy as np
import pandas as pd
import os, sys
import subprocess
from matplotlib import pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import casadi as cd

# To use this Python file pease download the corresponsing Excel file with the 
# experimantal data in the same directory with the name "SHF wheat hydrolysate all strains.xls"
os.chdir("C:\\Users\\Young\\Desktop\\Ben Moussa\\Studium\\Data science for bioengineering")
df = pd.read_excel(r"SHF wheat hydrolysate all strains.xls")

df.iloc[15,0]

class SHFdata():
    
    # Class object defintion method
    def __init__(self,path:str="SHF wheat hydrolysate all strains.xls",
                 color:str="red"):
        self.color= color
        
        if color.lower() == 'red':
            tupleY = (22,41)
            tupleX = (1,2)
            ind = 3
        elif color.lower() == "yellow":
            tupleY = (19,41)
            tupleX = (3,4)
            ind = 2
        else:
            raise Exception("\nSpecify the time serie: red or yellow \n\n")
            return
        
        # save specs
        self.pos_tuples_tuples = {"tupleY":tupleY,"tupleX":tupleX}
        self.df = pd.read_excel(r"{}".format(path))
        
        # get the time serie
        self.t_df = self.df.iloc[tupleY[0]:tupleY[1],tupleX[0]]
        self.t0 = self.t_df.to_numpy()
        
        # 1 st groupe data
        self.AB = self.fit_array(self.df.iloc[tupleY[0]:tupleY[1],tupleX[0]+ind])
        self.aB = self.fit_array(self.df.iloc[tupleY[0]:tupleY[1],tupleX[0]+ind+4])
        self.Ab = self.fit_array(self.df.iloc[tupleY[0]:tupleY[1],tupleX[0]+ind+2])
        self.ab = self.fit_array(self.df.iloc[tupleY[0]:tupleY[1],tupleX[0]+ind+6])
        
        # 2 nd groupe data
        self.ab7 = self.fit_array(self.df.iloc[tupleY[0]:tupleY[1],tupleX[0]+ind+8+1]) 
        self.ab2 = self.fit_array(self.df.iloc[tupleY[0]:tupleY[1],tupleX[0]+ind+10+1])
        self.a7b = self.fit_array(self.df.iloc[tupleY[0]:tupleY[1],tupleX[0]+ind+12+1])
        self.a2b = self.fit_array(self.df.iloc[tupleY[0]:tupleY[1],tupleX[0]+ind+14+1])
        
        # 3 rd groupe data
        self.a2b2 = self.fit_array(self.df.iloc[tupleY[0]:tupleY[1],tupleX[0]+ind+22+2]) 
        self.a2b7 = self.fit_array(self.df.iloc[tupleY[0]:tupleY[1],tupleX[0]+ind+20+2])
        self.a7b2 = self.fit_array(self.df.iloc[tupleY[0]:tupleY[1],tupleX[0]+ind+18+2])
        self.a7b7 = self.fit_array(self.df.iloc[tupleY[0]:tupleY[1],tupleX[0]+ind+16+2])
        
        # all data
        self.all_data = {"AB":self.AB,
                         "aB":self.aB,
                         "Ab":self.Ab,
                         "ab":self.ab,
                         
                         "ab7":self.ab7,
                         "ab2":self.ab2,
                         "a7b":self.a7b,
                         "a2b":self.a2b,
                         
                         "a2b2":self.a2b2,
                         "a2b7":self.a2b7,
                         "a7b2":self.a7b2,
                         "a7b7":self.a7b7,}
        
    # Method fitting the array lengths of time and medium mass series to each other
    def fit_array(self,arr):
        arr0 = arr.dropna()
        ind0 = max(self.t_df.index[0],arr0.index[0])
        ind_max = min(self.t_df.index[-1],arr0.index[-1])
        return self.t_df.loc[ind0:ind_max].to_numpy(), arr0.loc[ind0:ind_max].to_numpy()
    
    
    # Method plotting the raw data from the excel file
    def plot_raw(self,code=["AB"],point="x",save=False):
        
        # Plot the results
        plt.figure()
        for code_str in code:
            plt.plot(*self.all_data[code_str],point,label=code_str)
        
        # Set legend and axes nnotations
        plt.legend()
        plt.xlabel("Time [h]")
        plt.ylabel("Medium mass [g]")
        plt.grid()
        
        if save:
            plt.savefig("image.png")
        
        
        
    # method applying Gomperz kineticts to the data
    def gompertz(self,code="AB",gauss=False):
        # data preprocessing
        xs, ys = self.all_data[code]
        y_max = ys[-1]
        self.y_max = float(ys[-1])
        # Avoid log(log(1)) at the last point
        x_relevant, y_relevant = xs[:-1], ys[:-1]
        # Avoid y+max/0 at the first points
        while y_relevant[0] <= 0:
            x_relevant, y_relevant = x_relevant[1:], y_relevant[1:]
        self.x_relevant, self.y_relevant = x_relevant, y_relevant 
        Y = [np.log(np.log(y_max/y0)) for y0 in y_relevant]
        Y = np.array(Y).reshape((-1,1))
        X = x_relevant.reshape((-1,1))
        # breakpoint()
        
        # Definethe model and fit the preprocessed data of the transformed Gompertz
        self.gompertz_model = LinearRegression()
        self.gompertz_model.fit(X, Y)
        
        # Calculate original model parameters from fitting results
        coef = self.gompertz_model.coef_.reshape((1,-1))  
        beta = self.gompertz_model.intercept_.reshape((1,-1))
        self.lamb = float((1-beta)/coef) 
        self.my = float(-coef*y_max/np.exp(1))
        
        # If reuired  use gauss method for more accurate results
        if gauss:
            # Define the symbolic functions and variables
            xs, ys = self.all_data["AB"]
            n = len(ys)
            ps = cd.SX.sym("param",3)
            x = cd.SX.sym("x",1)
            y_max, my, lamb = ps[2], ps[1], ps[0]
            
            gomp = y_max*cd.exp(-cd.exp(my*np.exp(1)/y_max*(lamb-x)+1))
            gompertz = cd.Function("logistic",[x,ps],[gomp])
            y_hats = cd.SX.sym("y_hats",n)
            for i, _ in enumerate(xs):
                y_hats[i] = gompertz(xs[i],ps)
                
            cost = (y_hats-ys).T @ (y_hats-ys)
            J = cd.Function("cost_func",[ps],[cost],["y"],["J"])
            D = cd.Function("cost_derivative",[ps],[cd.jacobian(J(ps),ps)])
            p0 = np.array(list(self.gompertz(code="AB")))
            
            # Iterative computation of the parameters
            p_sol = self.gauss_method(p0,J,D,alpha=0.003)
            
            self.y_max, self.my, self.lamb = p_sol[2], p_sol[1], p_sol[0]
            
            # Convert eventual array notation to float
            self.y_max = float(self.y_max)
            self.my = float(self.my)
            self.lamb = float(self.lamb)
        
        return self.lamb, self.my, self.y_max
    
    
    
    
    
    # Predict values using fitted Gompertz model
    def gompertz_predict(self,xs,code="AB",gauss=False):
        # Sanity check
        if isinstance(xs,(float,int)):
            xs = np.array([xs]).reshape(1,)
        self.gompertz(code=code,gauss=gauss)
        ys = []
        for x0 in xs:
            y0 = self.y_max*np.exp(-np.exp( (self.my*np.exp(1)/self.y_max) * (self.lamb-x0) + 1 ))
            ys.append(y0)
        
        ys = np.array(ys).reshape(xs.shape)
        return ys



    # method applying logistic kineticts to the data
    def logistic(self,code="AB",gauss=False):
        # data preprocessing
        xs, ys = self.all_data[code]
        self.log_y_max = float(ys[-1])
        y_max = ys[-1]
        # Avoid log(log(1)) at the last point
        x_relevant, y_relevant = xs[:-1], ys[:-1]
        # Avoid y+max/0 at the first points
        while y_relevant[0] == 0:
            x_relevant, y_relevant = x_relevant[1:], y_relevant[1:]
        self.x_relevant, self.y_relevant = x_relevant, y_relevant 
        Y = [np.log(y_max/y0-1) for y0 in y_relevant]
        Y = np.array(Y).reshape((-1,1))
        X = x_relevant.reshape((-1,1))
        # breakpoint()
        
        # Definethe model and fit the preprocessed data of the transformed Gompertz
        self.logistic_model = LinearRegression()
        self.logistic_model.fit(X, Y)
        
        # Calculate original model parameters from fitting results
        coef = self.logistic_model.coef_.reshape((1,-1))  
        beta = self.logistic_model.intercept_.reshape((1,-1))
        
        self.log_lamb = float((2-beta)/coef) 
        self.log_my = float(-coef*y_max/4)
        
        # If reuired  use gauss method for more accurate results
        if gauss:
            # Define the symbolic functions and variables
            xs, ys = self.all_data["AB"]
            n = len(ys)
            ps = cd.SX.sym("param",3)
            x = cd.SX.sym("x",1)
            y_max, my, lamb = ps[2], ps[1], ps[0]
            logis = y_max/(1+cd.exp((my*4/y_max)*(lamb-x)+2))
            logistic = cd.Function("logistic",[x,ps],[logis])
            y_hats = cd.SX.sym("y_hats",n)
            for i, _ in enumerate(xs):
                y_hats[i] = logistic(xs[i],ps)
                
            cost = (y_hats-ys).T @ (y_hats-ys)
            J = cd.Function("cost_func",[ps],[cost],["y"],["J"])
            D = cd.Function("cost_derivative",[ps],[cd.jacobian(J(ps),ps)])
            p0 = np.array(list(self.logistic(code="AB")))
            
            # Iterative computation of the parameters
            p_sol = self.gauss_method(p0,J,D,alpha=0.003)
            self.log_y_max, self.log_my, self.log_lamb = p_sol[2], p_sol[1], p_sol[0]
            
            # Convert eventual array notation to float
            self.log_y_max = float(self.log_y_max)
            self.log_my = float(self.log_my)
            self.log_lamb = float(self.log_lamb)
        
        return self.log_lamb, self.log_my, self.log_y_max
    
    
    
    
    # Predict values using fitted logistic model
    def logistic_predict(self,xs,code="AB",gauss=False):
        # Sanity check
        if isinstance(xs,(float,int)):
            xs = np.array([xs]).reshape(1,)
        self.logistic(code=code,gauss=gauss)
        ys = []
        for x0 in xs:
            y0 = self.log_y_max/(  1+np.exp((4*self.log_my/self.log_y_max)*(self.log_lamb-x0)+2)  )
            ys.append(y0)
        
        ys = np.array(ys).reshape(xs.shape)
        return ys


 
    
    
    # Fit linear model specifying exponential groth region
    def linear_fit(self,ind0,ind_max,code="AB"):
        # linear fit boolean to keep track before prediction
        self._linear_fit_done = True
        self.ind0 = ind0
        self.ind_max = ind_max
        self.lin_code = code 
        
        # Define the fitting model
        xs, ys = self.all_data[code]
        x_relevant, y_relevant = xs[ind0:ind_max], ys[ind0:ind_max]
        self.linear_model= LinearRegression()
        self.linear_model.fit(x_relevant.reshape((-1,1)),
                              y_relevant.reshape((-1,1))
                              )
        
        # Get the linear fitting parameters
        self.lin_coef = self.linear_model.coef_.reshape((1,-1))
        self.lin_beta = self.linear_model.intercept_.reshape((1,-1))
        # self.lin_my = selflin_coef/
        
        # linear fit boolean to keep track before prediction
        self._linear_fit_done = True
        
        return self.lin_coef, self.lin_beta
    
    
    
    # Pedict using the fitted linear model (pre-requisite)
    def linear_predict(self,xs): 
        if self._linear_fit_done:
            ys = xs  * self.lin_coef + self.lin_beta
            ys = ys.reshape(xs.shape)
            return ys
        
        else:
            raise Exception("Please catty out the linear fittig before predicting !\n")
            
        
    # Fit the values to Richard model
    def richard(self,code="AB"):
        # Set the symbolic variables and functions
        xs, ys = self.all_data[code]
        n = len(ys)
        ps = cd.SX.sym("param",4)
        x = cd.SX.sym("x",1)
        y_max, my, lamb, v = ps[2], ps[1], ps[0], ps[3]
        rich = y_max*(1+v*cd.exp(1+v)*cd.exp(  (my/y_max)*(1+v)**(1+1/v)*(lamb-x) ))**(-1/v)
        richard = cd.Function("logistic",[x,ps],[rich])
        y_hats = cd.SX.sym("y_hats",n)
        for i, _ in enumerate(xs):
            y_hats[i] = richard(xs[i],ps)
            
        cost = (y_hats-ys).T @ (y_hats-ys)
        J = cd.Function("cost_func",[ps],[cost],["y"],["J"])
        D = cd.Function("cost_derivative",[ps],[cd.jacobian(J(ps),ps)])
        alpha = 0.003
        p0 = np.array(list(self.gompertz(code="AB"))+[0.9])
        
        # Iterative computation of the parameters
        p_sol = self.gauss_method(p0,J,D,alpha=0.003)
        
        # get the solution parameters
        self.rich_y_max = float(p_sol[2])
        self.rich_my = float(p_sol[1])
        self.rich_lamb = float(p_sol[0])
        self.rich_v = float(p_sol[3])
        
        return self.rich_lamb, self.rich_my, self.rich_y_max, self.rich_v
    
    
    # Pedict using the fitted linear model
    def richard_predict(self,xs,code="AB"):
        # Sanity check
        if isinstance(xs,(float,int)):
            xs = np.array([xs]).reshape(1,)
        self.richard(code=code)
        
        y_max = self.rich_y_max
        v = self.rich_v
        my = self.rich_my
        lamb = self.rich_lamb
        ys = []
        for x0 in xs:
            y0 = y_max*(1+v*np.exp(1+v)*np.exp(  (my/y_max)*(1+v)**(1+1/v)*(lamb-x0) ))**(-1/v)
            ys.append(y0)
        
        ys = np.array(ys).reshape(xs.shape)
        return ys
        
        
        
        
        
    # This method compares the plotting results
    def compare_plots(self,code="AB",ind0=-1,ind_max=-1,
                     models=["logistic","gompertz","linear","richrad"],
                     gauss=False, save=False):
        
        plt.figure()
        models_ = [m.lower() for m in models]
        
        # plot original data
        xs, ys = self.all_data[code]
        plt.plot(xs, ys, "bx", label="Original")
        
        # plot Gopmertz model predictions
        if "gompertz" in models_:
            x_num = np.linspace(xs[0], xs[-1],num=100)
            y_pred = self.gompertz_predict(x_num,code=code,gauss=gauss)
            plt.plot(x_num, y_pred, "-k", label="Gompertz")
        
        # Plot linear fitting results if available
        if ("linear" in models_) and (ind0 > -1) and (ind_max > ind0) and (ind_max < len(xs)+1):
            self.linear_fit(ind0, ind_max,code=code)
            y_pred_lin = self.linear_predict(xs[ind0:ind_max])
            plt.plot(xs[ind0:ind_max], y_pred_lin,"y",label="Linear")
            plt.plot(xs[ind0:ind_max], ys[ind0:ind_max], "bo")
        
        # Plot logistic fitting results
        if "logistic" in models_:
            x_num = np.linspace(xs[0], xs[-1],num=100)
            y_pred_log = self.logistic_predict(x_num,code=code,gauss=gauss)
            plt.plot(x_num,y_pred_log,"-r",label="Logistic")
        
        # Plot richard fitting results
        if "richard" in models_:
            x_num = np.linspace(xs[0], xs[-1],num=100)
            y_pred_rich = self.richard_predict(x_num,code=code)
            plt.plot(x_num,y_pred_rich,"-g",label="Richard")
            
            
        # Legend and notations for the axes
        plt.xlabel('tine [h]')
        plt.ylabel("Medium mass [g]")
        plt.legend()
        plt.grid()
        
        if save:
          plt.savefig("image_compare.jpg")  
        
        
        
        
    def gauss_method(self,p0,J,D,alpha=0.0003):
        
        p_list = [p0]
        costs = [10]
        diff = 1
        p0s = [p0]
        counter = 0
        while np.abs(diff) > 1e-8 and counter < 40000:
            counter += 1
            dJ = D(p0)
            p0 = p0 - alpha * dJ.T
            p0s.append(p0)
            cost = J(p0)
            diff = cost - costs[-1]
            costs.append(cost)
            
        if counter >= 39999:
            raise Exception("\nIteration killed: Too much steps")
        # for p in p0 :
        #     if np.isnan(p):
        #         raise Exception("\nKilled due to nan values. Check the learning rat \n")
        
        return p0
        
        
    # Method calculating R and adjuste R
    def calculate_R(self,y_hats,ys,k=2):
        mean = np.mean(ys)
        SSB = np.sum((y_hats)**2)
        SSE = np.sum((y_hats-ys)**2)
        R = SSB/(SSB+SSE)
        n = len(ys)
        R_adj = 1- (1-R**2)*(n-1)/(n-1-k)
        return R, R_adj
            
        
    def __getitem__(self,code="AB",*args):
        if len(args) == 1:
            output = self.all_data[code][args]
        elif len(args) == 2:
            output = self.all_data[code][args[0]:args[1]]
        

# %%
if __name__ == "__main__":
    shf0 = SHFdata()
    # shf0.gompertz(code="AB",gauss=True)
    # shf0.logistic(code="AB",gauss=True)
    code="AB"
    gauss = True
    gauss = False
    shf0.richard(code=code)
    xs, ys = shf0.all_data[code]
    y_hats = shf0.gompertz_predict(xs,code=code,gauss=gauss)
    # y_hats = shf0.richard_predict(xs, code=code)
    # y_hats = shf0.logistic_predict(xs,code=code, gauss=gauss)
    R, R_adj = shf0.calculate_R(y_hats, ys, k=2)
    print(R, R_adj)
    
    plt.figure()
    plt.plot(xs,ys,"x")
    plt.plot(xs,y_hats,"-")
    plt.grid()
            
            

    
# %% define a SHF data class object for both series    
if __name__ == "__main__":
    shf1 = SHFdata(color="yellow")
    shf2 = SHFdata(color="red")
    code = "AB"
    ind0, ind_max = 2, 10
    models = ["gompertz","logistic","richard"]
    # models = ["gompertz","richard"]
    gauss = True
    shf1.compare_plots(code=code,ind0=ind0,ind_max=ind_max,models=models,gauss=gauss)
    
    if "gompertz" in models:
        print("Gompertz results are: my = {} and lambda = {}\n".format(shf1.my,
                                                                   shf1.lamb))
    if "logistic" in models:
        print("Logistic model results are: my = {} and lambda = {}\n".format(shf1.log_my,
                                                                   shf1.log_lamb))
    if "linear" in models:        
        print("Linear fitting results in coef = {}\n".format(shf1.lin_coef))
    
    if "richard" in models:
        print("Richard model results are: my = {}, lambda = {}, v = {} and  y_max = {}\n".format(shf1.rich_my,shf1.rich_lamb,shf1.rich_v,shf1.rich_y_max))
    

# %%
    res = shf1.gompertz()
    print(res)
    code = "AB"
    xs, ys = shf1.all_data[code]
    y_pred = shf1.gompertz_predict(xs,code=code)
    plt.plot(xs, ys, "x", label="original")
    plt.plot(xs, y_pred, "-",label="pred.")
    plt.legend()
    plt.xlabel("time [h]")
    plt.ylabel("medium mass [g]")
    plt.grid()
    
    # print(shf1.a7b7[0],shf1.a7b7[1],sep="\n\n\n")
    # shf1.plot_raw(["AB","Ab","aB","ab"],point="o")
    # shf2.plot_raw(["AB","Ab","aB","ab"],point="o")
    
# %% Linear fitting of growth data (visual estimation of linear phase)
    
# def  
    ind0, ind_max, code = 2, 8, "AB"
    xs_orig, ys_orig = shf1.all_data[code]
    xs, ys = xs_orig[ind0:ind_max], ys_orig[ind0:ind_max]
    model = LinearRegression()
    model.fit(xs.reshape(-1,1),
              ys.reshape(-1,1))
    
    coef = model.coef_.reshape((1,))
    beta = model.intercept_.reshape((1,))
    
    plt.figure()
    plt.plot(xs_orig,ys_orig,"x")
    y_pred = xs * coef + beta
    plt.plot(xs,ys,"o",label="original")
    plt.plot(xs,y_pred,"-",label="prediction")
    plt.legend()
    plt.xlabel("time [h]")
    plt.ylabel("medium mass [g]")
    plt.grid()
    
    # calculate R
    SSB = np.sum((y_pred)**2)
    SSE = np.sum((ys-y_pred)**2)
    R = SSB/(SSB+SSE)
    
    # calculate adjusted R
    n = len(y_pred)
    k = 2
    R_adj = 1- (1-R**2)*(n-1)/(n-1-k)
    
    # calculate MSE
    MSE = SSE/(n-k-1)
    
    # print results
    print(ind0, ind_max)
    print(R)
    print(R_adj)
    print(MSE)
    print("")
    
    

    
# %% investigate best linear combination

def calculate_R(xs,ys):
    model = LinearRegression()
    model.fit(xs.reshape(-1,1),
              ys.reshape(-1,1))
    
    coef = model.coef_.reshape((1,))
    beta = model.intercept_.reshape((1,))
    y_pred = xs * coef + beta
    
    SSB = np.sum((y_pred)**2)
    SSE = np.sum((ys-y_pred)**2)
    R = SSB/(SSB+SSE)
    
    n = len(y_pred)
    k = 2
    R_adj = 1- (1-R**2)*(n-1)/(n-1-k)
    
    return R, R_adj

# shf3 = SHFdata(color="yellow")
# code = "AB"
# xs_orig, ys_orig = shf3.all_data[code]
# Xs, Ys = np.meshgrid(xs_orig, ys_orig)

# X = np.ones(Xs.shape)
# Y = np.ones(Xs.shape)

# X = np.arange(0,14,1)
# Y = np.arange(0,14,1)
# X, Y = np.meshgrid(X, Y)

# Z1 = np.zeros(Xs.shape) 
# Z2 = np.zeros(Xs.shape) 

# ii = 0
# for ind0 in range(len(xs_orig)-5):
#     for ind_max in range(ind0+4,len(xs_orig)):
#         ii += 1
#         x_sampled, y_sampled = xs_orig[ind0:ind_max], ys_orig[ind0:ind_max]
#         Z1[ind_max,ind0], Z2[ind_max,ind0] = calculate_R(x_sampled, y_sampled)
#         # X[ind_max,ind0] = ind0
#         # Y[ind_max,ind0] = ind_max 

# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# surf1 = ax.plot_surface(X, Y, Z1, cmap=cm.coolwarm,
#                         linewidth=0, antialiased=False)

# # Customize the z axis.
# ax.set_zlim(0.6, 1)
# ax.zaxis.set_major_locator(LinearLocator(10))
# # A StrMethodFormatter is used automatically
# ax.zaxis.set_major_formatter('{x:.02f}')

# fig.colorbar(surf1, shrink=0.5, aspect=5)

# %% gauss method for logistic fitting
    
    shf4 = SHFdata(color="yellow")
    xs, ys = shf4.all_data["AB"]
    n = len(ys)
    ps = cd.SX.sym("param",3)
    x = cd.SX.sym("x",1)
    y_max, my, lamb = ps[2], ps[1], ps[0]
    logis = y_max/(1+cd.exp((my*4/y_max)*(lamb-x)+2))
    logistic = cd.Function("logistic",[x,ps],[logis])
    y_hats = cd.SX.sym("y_hats",n)
    for i, _ in enumerate(xs):
        y_hats[i] = logistic(xs[i],ps)
        
    cost = (y_hats-ys).T @ (y_hats-ys)
    J = cd.Function("cost_func",[ps],[cost],["y"],["J"])
    D = cd.Function("cost_derivative",[ps],[cd.jacobian(J(ps),ps)])
    
    p0 = np.array(shf4.logistic(code="AB"))
    p_list = [p0]
    costs = [10]
    alpha = 0.0002
    diff = 1
    counter = 0
    while np.abs(diff) > 1e-4 and counter < 150:
        counter += 1
        dJ = D(p0)
        p0 = p0 - alpha * dJ.T
        cost = J(p0)
        diff = cost - costs[-1]
        costs.append(cost)
        
    print(counter,diff,sep="\n\n")
    
    
    # %% gauss method for Gompertz model fitting
    
    shf4 = SHFdata(color="yellow")
    xs, ys = shf4.all_data["AB"]
    n = len(ys)
    ps = cd.SX.sym("param",3)
    x = cd.SX.sym("x",1)
    y_max, my, lamb = ps[2], ps[1], ps[0]
    gomp = y_max*cd.exp(-cd.exp(my*np.exp(1)/y_max*(lamb-x)+1))
    gompertz = cd.Function("logistic",[x,ps],[gomp])
    y_hats = cd.SX.sym("y_hats",n)
    for i, _ in enumerate(xs):
        y_hats[i] = gompertz(xs[i],ps)
        
    cost = (y_hats-ys).T @ (y_hats-ys)
    J = cd.Function("cost_func",[ps],[cost],["y"],["J"])
    D = cd.Function("cost_derivative",[ps],[cd.jacobian(J(ps),ps)])
    
    p00 = p0 = np.array(shf4.gompertz(code="AB"))
    p_list = [p0]
    costs = [10]
    alpha = 0.06
    diff = 1
    counter = 0
    while np.abs(diff) > 1e-4 and counter < 150:
        counter += 1
        dJ = D(p0)
        p0 = p0 - alpha * dJ.T
        cost = J(p0)
        diff = cost - costs[-1]
        costs.append(cost)
        
    print(counter,diff,sep="\n\n")
    
    # %% gauss method for Richards model
    
    
    
    shf4 = SHFdata(color="yellow")
    xs, ys = shf4.all_data["AB"]
    n = len(ys)
    ps = cd.SX.sym("param",4)
    x = cd.SX.sym("x",1)
    y_max, my, lamb, v = ps[2], ps[1], ps[0], ps[3]
    rich = y_max*(1+v*cd.exp(1+v)*cd.exp(  (my/y_max)*(1+v)**(1+1/v)*(lamb-x) ))**(-1/v)
    richard = cd.Function("logistic",[x,ps],[rich])
    y_hats = cd.SX.sym("y_hats",n)
    for i, _ in enumerate(xs):
        y_hats[i] = richard(xs[i],ps)
        
    cost = (y_hats-ys).T @ (y_hats-ys)
    J = cd.Function("cost_func",[ps],[cost],["y"],["J"])
    D = cd.Function("cost_derivative",[ps],[cd.jacobian(J(ps),ps)])
    alpha = 0.003
    
    def gauss_method(p0,J,dJ,alpha):
        
        p00 = p0 = np.array(list(shf4.gompertz(code="AB"))+[2.4])
        p_list = [p0]
        costs = [10]
        diff = 1
        p0s = [p0]
        counter = 0
        while np.abs(diff) > 1e-8 and counter < 40000:
            counter += 1
            dJ = D(p0)
            p0 = p0 - alpha * dJ.T
            p0s.append(p0)
            cost = J(p0)
            diff = cost - costs[-1]
            costs.append(cost)
            
        print(counter,diff,p0,sep="\n\n")
        return p0
        
    gauss_method(p0,J,dJ,alpha)
        
            
            
    
    
    
    
    
    
