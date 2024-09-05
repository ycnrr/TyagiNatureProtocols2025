'''
@author: Sidharth Tyagi, Emre Kiziltug 
v2.1 - 12-22-2022
'''
# -*- coding: utf-8 -*-

from dask.array.routines import transpose
import os
import PySimpleGUI as sg
import tkinter

import tkinter as tk

from tkinter import filedialog

 

import PySimpleGUI as sg



def process(file_paths):
    import pandas as pd
    import numpy as np
    import os
    import glob
    import matplotlib.pyplot as plt
    
    
    
    ACT_path = file_paths[0]
    ACT_cap_path = file_paths[1]
    ACT_par_path = file_paths[2]
    ACT_vrev_path = file_paths[3]
    FIN_path = file_paths[4]
    FIN_cap_path = file_paths[5]
    FIN_par_path = file_paths[6]
    SIN_path = file_paths[7]
    SIN_cap_path = file_paths[8]
    SIN_par_path = file_paths[9]
    output_path = file_paths[10]
    if output_path == "":
        cur_dir = os.getcwd()
        output_path = cur_dir + "/Process"
    else: 
        output_path = output_path + "/Process"
    if not os.path.exists(output_path):
        
        os.makedirs(output_path)
    
    nan_value = float("NaN")
   
    if FIN_path != "":
        FIN_data = pd.read_csv(FIN_path)
        FIN_data = FIN_data.iloc[: , 1:]
        InactivationCap = pd.read_csv(FIN_cap_path)
        InactivationCap.rename(columns = {list(InactivationCap)[0]:'Variable'}, inplace=True)
        InactivationParam = pd.read_csv(FIN_par_path)
        InactivationParam.rename(columns = {list(InactivationParam)[0]:'Variable'}, inplace=True)
        InactivationCap.replace("", nan_value, inplace = True)
        InactivationCap.dropna(how='all', axis = 1, inplace = True)
        InactivationCap.dropna(how='all', axis = 0, inplace = True)
        InactivationCapNames = InactivationCap.columns.values.tolist()
        NewCol = []
        for string in InactivationCapNames:
            new_string = string.replace(":", "_")
            NewCol.append(new_string)
        InactivationCap.columns = NewCol
        InactivationCap.at[0,"Variable"] = "Inactivation cap"

    
    if SIN_path != "":
        SIN_data = pd.read_csv(SIN_path)
        SIN_data = SIN_data.iloc[: , 1:]
        SInactivationCap = pd.read_csv(SIN_cap_path)
        SInactivationCap.rename(columns = {list(SInactivationCap)[0]:'Variable'}, inplace=True)
        SInactivationParam = pd.read_csv(SIN_par_path)
        SInactivationParam.rename(columns = {list(SInactivationParam)[0]:'Variable'}, inplace=True)
        SInactivationCap.replace("", nan_value, inplace = True)
        SInactivationCap.dropna(how='all', axis = 1, inplace = True)
        SInactivationCap.dropna(how='all', axis = 0, inplace = True)
        SInactivationCapNames = SInactivationCap.columns.values.tolist()
        NewCol = []
        for string in SInactivationCapNames:
            new_string = string.replace(":", "_")
            NewCol.append(new_string)
        SInactivationCap.columns = NewCol
        SInactivationCap.at[0,"Variable"] = "SInactivation cap"
    
    if ACT_path != "":
        ACT_data = pd.read_csv(ACT_path)
        ACT_data.dropna(how='all', axis = 1, inplace = True)
        ACT_data = ACT_data.iloc[: , 1:]
        ActivationCap = pd.read_csv(ACT_cap_path)
        ActivationCap.rename(columns = {list(ActivationCap)[0]:'Variable'}, inplace=True)
        ActivationParam = pd.read_csv(ACT_par_path)
        ActivationParam.rename(columns = {list(ActivationParam)[0]:'Variable'}, inplace=True)
        ActivationVrev = pd.read_csv(ACT_vrev_path)
        ActivationVrev.rename(columns = {list(ActivationVrev)[0]:'Variable'}, inplace=True)
        ActivationVrev.replace("", nan_value, inplace = True)
        ActivationVrev.dropna(how='all', axis = 1, inplace = True)
        ActivationVrev.dropna(how='all', axis = 0, inplace = True)
        ActivationVrevNames = ActivationVrev.columns.values.tolist()
        NewCol = []
        for string in ActivationVrevNames:
            new_string = string.replace(":", "_")
            NewCol.append(new_string)
        ActivationVrev.columns = NewCol
        
        ActivationCap.replace("", nan_value, inplace = True)
        ActivationCap.dropna(how='all', axis = 1, inplace = True)
        ActivationCap.dropna(how='all', axis = 0, inplace = True)
        ActivationCapNames = ActivationCap.columns.values.tolist()
        NewCol = []
        for string in ActivationCapNames:
            new_string = string.replace(":", "_")
            NewCol.append(new_string)
        ActivationCap.columns = NewCol
        ActivationCap.at[0,"Variable"] = "Activation cap"
        
        #ActivationCap.replace(regex=True, inplace=True, to_replace=r'[^0-9.\-]', value=r'')
        #ActivationCap = ActivationCap.astype('float64')
        
        
        vertical_stack = pd.concat([ActivationCap, ActivationParam, ActivationVrev],axis = 0)
        vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
        vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
        if FIN_path != "":
             vertical_stack = pd.concat([vertical_stack,InactivationCap,InactivationParam],axis = 0)
             vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
             vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
        if SIN_path != "":
                vertical_stack = pd.concat([vertical_stack,SInactivationCap,SInactivationParam],axis = 0)
                vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
                vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
        
        vertical_stack = pd.concat([vertical_stack,ACT_data],axis = 0)
        vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
        vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
        if FIN_path != "":
            vertical_stack = pd.concat([vertical_stack,FIN_data],axis = 0)
            vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
            vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
        if SIN_path != "":  
            vertical_stack = pd.concat([vertical_stack,SIN_data],axis = 0)
    
    if ACT_path == "":
        if FIN_path != "":
            vertical_stack = pd.concat([InactivationCap,InactivationParam],axis = 0)
            vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
            vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
            if SIN_path != "":
                vertical_stack = pd.concat([vertical_stack,SInactivationCap,SInactivationParam],axis = 0)
                vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
                vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
            vertical_stack = pd.concat([vertical_stack,FIN_data],axis = 0)
            vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
            vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
            if SIN_path != "":
                vertical_stack = pd.concat([vertical_stack,SIN_data],axis = 0)
        else:
            vertical_stack = pd.concat([SInactivationCap,SInactivationParam],axis = 0)
            vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
            vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
            vertical_stack = pd.concat([vertical_stack,SIN_data],axis = 0)
                
   
    
   

    vertical_stack.to_csv(output_path+"/master_data.csv") 
    #File will output to previously designated path
    return 0

#Fast inactivation
def fast_inactivation (file_paths):
    import pandas as pd
    import numpy as np
    import os
    import glob
    import matplotlib.pyplot as plt
    
    data_path = file_paths[0]
    output_path = file_paths[1]
    if output_path == "":
        cur_dir = os.getcwd()
        output_path = cur_dir + "/Fast_inactivation"
    else: 
        output_path = output_path + "/Fast_inactivation"
    if not os.path.exists(output_path):
        
        os.makedirs(output_path)
    InactivationDf = pd.read_csv(data_path)
    nan_value = float("NaN")
    InactivationDf.replace("", nan_value, inplace = True)
    InactivationDf.dropna(how='all', axis = 1, inplace = True)
    InactivationColNames = InactivationDf.columns.values.tolist()
    NewCol = []
    for string in InactivationColNames:
        new_string = string.replace(":", "_")
        NewCol.append(new_string)
    InactivationDf.columns = NewCol
    InactivationDf.replace(regex=True, inplace=True, to_replace=r'[^0-9.\-]', value=r'')
    InactivationDf = InactivationDf.astype('float64') 

    MembPotent = InactivationDf.iloc[:, 0]
    InactivationDf.iloc[:, 0] = MembPotent
    InactivationDfColumns = InactivationDf.columns.values.tolist()
    InactivationDf = InactivationDf[InactivationDfColumns[1:]]
    
    Initial = InactivationDf.head(4)
    End = InactivationDf.tail(4)
    InitialMean = pd.DataFrame(Initial.mean())
    EndMean = pd.DataFrame(End.mean())
    Diff = InitialMean - EndMean
    Range = InactivationDf.max(axis=0) - InactivationDf.min(axis=0)
    Range = pd.DataFrame(Range)
    nordiff = Diff/Range
    nordiff = nordiff.transpose()
    output1 = InactivationDf
    output1.insert(0,'Membrane Potential (mV)',MembPotent)
    output1['Membrane Potential (mV)'] = 'FIN_' +  output1['Membrane Potential (mV)'].astype(str)
 
    out1_loc = output_path + "/unfiltered_normalized_fast_inactivation_data.csv"
    output1.to_csv(out1_loc) 
 
    InactivationDf = InactivationDf[InactivationDfColumns[1:]]
    faulty = pd.DataFrame()
    for column in nordiff:
        if nordiff.at[0,column] <0.8:
            faulty = pd.concat((faulty, InactivationDf[column]), axis = 1)
            InactivationDf.drop(column, inplace=True, axis=1)
    output2 = InactivationDf
    output2.insert(0,'Membrane Potential (mV)',MembPotent)

    out2_loc = output_path + "/filtered_normalized_fast_inactivation_data.csv"
    output2.to_csv(out2_loc) 
    
    InactivationDf = InactivationDf.iloc[: , 1:]
    CurrStd = pd.DataFrame(InactivationDf.std(axis = 0, ddof=0))
    CurrStd = CurrStd.transpose()
    Volt = MembPotent
    from scipy import optimize
    def Boltzmann(x, v, k):
        return 1/(1+np.exp((-v+x)/k))
    
    v_0 = -70
    k_0 = 9
    
    def DoubleBoltzmann(x, y0, A, z1, z2, k1, k2, p):
        B = np.exp((x-z1)/k1)
        C = np.exp((x-z2)/k2)
        return y0+ A*(p/(1+B)+(1-p)/(1+C))
    
    y0_0 = 1
    A_0 = 33
    z1_0 = -82
    z2_0 = -40
    k1_0 = -8.3
    k2_0 = -3.2
    p_0 = 0.9
    floatlist = []
    floatlist2 = []
    doublehalf1 = []
    doublehalf2 = []
    SingleBoltFitParams = pd.DataFrame()
    DoubleBoltFitParams = pd.DataFrame()
    for column in InactivationDf:
        try:
            Curr = InactivationDf[column].values
            params, params_covariance = optimize.curve_fit(Boltzmann, Volt, Curr, p0 = ([v_0, k_0]))
            plt.figure(figsize = (6,4))
            plt.scatter(Volt, Curr, label = InactivationDf[column].name)
            plt.plot(Volt, Boltzmann(Volt, params[0], params[1]), label = 'Single Boltzmann')
            plt.legend(loc='best')
            out_img_path = output_path + "/Fit_visualizations/"
            if not os.path.exists(out_img_path):
                os.makedirs(out_img_path)
            plt.savefig(out_img_path + column +'_single_FIN.png')
            diff = Curr - Boltzmann(Volt, params[0], params[1])
            rms = (np.sqrt(np.sum(np.square(diff)/len(diff))))
            normrms = rms / CurrStd.at[0,column]
            floatlist.append(normrms)
            params = pd.DataFrame(params)
            SingleBoltFitParams = pd.concat((SingleBoltFitParams, params), axis = 1) 
            params2, params_covariance = optimize.curve_fit(DoubleBoltzmann, Volt, Curr, p0 = ([y0_0, A_0, z1_0, z2_0, k1_0, k2_0, p_0]), maxfev = 300)
            plt.figure(figsize = (6,4))
            plt.scatter(Volt, Curr, label = InactivationDf[column].name)
            plt.plot(Volt, DoubleBoltzmann(Volt, params2[0], params2[1], params2[2], params2[3], params2[4], params2[5], params2[6]), label = 'Double Boltzmann')
            plt.legend(loc='best')
            plt.savefig(out_img_path + column +'_double_FIN.png')
            diff2 = Curr - DoubleBoltzmann(Volt, params2[0], params2[1], params2[2], params2[3], params2[4], params2[5], params2[6])
            rms2 = (np.sqrt(np.sum(np.square(diff2)/len(diff2))))
            normrms2 = rms2 / CurrStd.at[0,column]
            floatlist2.append(normrms2)
            doublehalf1.append(params2[2])
            doublehalf2.append(params2[3])
            params2 = pd.DataFrame(params2)
            DoubleBoltFitParams = pd.concat((DoubleBoltFitParams, params2), axis = 1)
            
        except:
            string = 'Failed'
            faileddf = pd.DataFrame([string])
            floatlist2.append('Failed')
            doublehalf1.append(0)
            doublehalf2.append(0)
            DoubleBoltFitParams = pd.concat((DoubleBoltFitParams, faileddf), axis = 1)
            pass
    doublediff = abs(np.subtract(doublehalf1, doublehalf2))
    bin = [] 
    for i in range(len(floatlist)):
        if floatlist2[i] == "Failed":
            bin.append('single')
        elif doublediff[i] < 15:
            bin.append('single')
        elif doublediff[i] > 100:
            bin.append('single')
        elif floatlist2[i] < floatlist[i]:
            bin.append('double')
        else:
            bin.append('single')
    ID = pd.DataFrame({"FIN_Single Boltzmann":floatlist,"FIN_Double Boltzmann":floatlist2,"FIN_Bin":bin}) 
    ID = ID.transpose()
    ID.columns = InactivationDf.columns.values.tolist()
    DoubleBoltFitParams.columns = InactivationDf.columns.values.tolist()
    DoubleBoltFitParams = DoubleBoltFitParams.rename(index={0:'FIN_y0', 1:'FIN_A', 2:'FIN_z1', 3:'FIN_z2', 4:'FIN_k1', 5:'FIN_k2', 6:'FIN_p'})
    SingleBoltFitParams.columns = InactivationDf.columns.values.tolist()
    SingleBoltFitParams = SingleBoltFitParams.rename(index={0:'FIN_v',1:'FIN_k'})
    ID_final = pd.concat([ID, SingleBoltFitParams,DoubleBoltFitParams], axis=0)
    ID_final.to_csv(output_path + "/FIN_fit_parameters.csv")

    return 0

def slow_inactivation (file_paths):
    import pandas as pd
    import numpy as np
    import os
    import glob
    import matplotlib.pyplot as plt
    
    data_path = file_paths[0]
    output_path = file_paths[1]
    if output_path == "":
        cur_dir = os.getcwd()
        output_path = cur_dir + "/Slow_inactivation"
    else: 
        output_path = output_path + "/Slow_inactivation"
    if not os.path.exists(output_path):
        
        os.makedirs(output_path)
        
    SlowInactivationDf = pd.read_csv(data_path)
    nan_value = float("NaN")
    SlowInactivationDf.replace("", nan_value, inplace = True)
    SlowInactivationDf.dropna(how='all', axis = 1, inplace = True)
    SlowInactivationColNames = SlowInactivationDf.columns.values.tolist()
    NewCol = []
    for string in SlowInactivationColNames:
        new_string = string.replace(":", "_")
        NewCol.append(new_string)
    SlowInactivationDf.columns = NewCol
    SlowInactivationDf.replace(regex=True, inplace=True, to_replace=r'[^0-9.\-]', value=r'')
    SlowInactivationDf = SlowInactivationDf.astype('float64')
    MembPotent = SlowInactivationDf['mV']
    SlowInactivationDf['mV'] = MembPotent
    SlowInactivationDfColumns = SlowInactivationDf.columns.values.tolist()
    SlowInactivationDf = SlowInactivationDf[SlowInactivationDfColumns[1:]]
    Initial = SlowInactivationDf.head(2)
    End = SlowInactivationDf.tail(2)
    InitialMean = pd.DataFrame(Initial.mean())
    EndMean = pd.DataFrame(End.mean())
    Diff = InitialMean - EndMean
    Range = SlowInactivationDf.max(axis=0) - SlowInactivationDf.min(axis=0)
    Range = pd.DataFrame(Range)
    nordiff = Diff/Range
    nordiff = nordiff.transpose()
    output1 = SlowInactivationDf
    output1.insert(0,'Membrane Potential (mV)',MembPotent)
    output1['Membrane Potential (mV)'] = 'SIN_' +  output1['Membrane Potential (mV)'].astype(str)
    out1_loc = output_path + "/unfiltered_normalized_slow_inactivation_data.csv"
    output1.to_csv(out1_loc) 
    faulty = pd.DataFrame()
    for column in nordiff:
        if nordiff.at[0,column] <0.5:
            faulty = pd.concat((faulty, SlowInactivationDf[column]), axis = 1)
            SlowInactivationDf.drop(column, inplace=True, axis=1)
    output2 = SlowInactivationDf
    
    out2_loc = output_path + "/filtered_normalized_slow_inactivation_data.csv"
    output2.to_csv(out2_loc) 

    SlowInactivationDf = SlowInactivationDf.iloc[: , 1:]
    CurrStd = pd.DataFrame(SlowInactivationDf.std(axis = 0, ddof=0))
    CurrStd = CurrStd.transpose()
    Volt = MembPotent
    from scipy import optimize
    def Boltzmann(x, v, k):
        return (min + (max-min)/(1+np.exp((x-v)/k)))
    
    v_0 = -70
    k_0 = 9
    
    def DoubleBoltzmann(x, y0, A, z1, z2, k1, k2, p):
        B = np.exp((x-z1)/k1)
        C = np.exp((x-z2)/k2)
        return y0+ A*(p/(1+B)+(1-p)/(1+C))
    
    y0_0 = 1
    A_0 = 33
    z1_0 = -62
    z2_0 = -50
    k1_0 = -8.3
    k2_0 = -3.2
    p_0 = 0.9
    floatlist = []
    floatlist2 = []
    SingleBoltFitParams = pd.DataFrame()
    DoubleBoltFitParams = pd.DataFrame()
    for column in SlowInactivationDf:
        try:
            Curr = SlowInactivationDf[column].values
            print(type(Curr))
            max = Curr.max(axis=0)
            min = Curr.min(axis=0)
            params, params_covariance = optimize.curve_fit(Boltzmann, Volt, Curr, p0 = ([v_0, k_0]))
            plt.figure(figsize = (6,4))
            plt.scatter(Volt, Curr, label = SlowInactivationDf[column].name)
            plt.plot(Volt, Boltzmann(Volt, params[0], params[1]), label = 'Single Boltzmann')
            plt.legend(loc='best')
            out_img_path = output_path + "/Fit_visualizations/"
            if not os.path.exists(out_img_path):
                os.makedirs(out_img_path)
            plt.savefig(out_img_path + column +'_single_SIN.png')
            diff = Curr - Boltzmann(Volt, params[0], params[1])
            rms = (np.sqrt(np.sum(np.square(diff)/len(diff))))
            normrms = rms / CurrStd.at[0,column]
            floatlist.append(normrms)
            params = pd.DataFrame(params)
            SingleBoltFitParams = pd.concat((SingleBoltFitParams, params), axis = 1) 
            params2, params_covariance = optimize.curve_fit(DoubleBoltzmann, Volt, Curr, p0 = ([y0_0, A_0, z1_0, z2_0, k1_0, k2_0, p_0]), maxfev = 300)
            plt.figure(figsize = (6,4))
            plt.scatter(Volt, Curr, label = SlowInactivationDf[column].name)
            plt.plot(Volt, DoubleBoltzmann(Volt, params2[0], params2[1], params2[2], params2[3], params2[4], params2[5], params2[6]), label = 'Double Boltzmann')
            plt.legend(loc='best')
            plt.savefig(out_img_path + column +'_double_SIN.png')
            diff2 = Curr - DoubleBoltzmann(Volt, params2[0], params2[1], params2[2], params2[3], params2[4], params2[5], params2[6])
            rms2 = (np.sqrt(np.sum(np.square(diff2)/len(diff2))))
            normrms2 = rms2 / CurrStd.at[0,column]
            floatlist2.append(normrms2)
            params2 = pd.DataFrame(params2)
            DoubleBoltFitParams = pd.concat((DoubleBoltFitParams, params2), axis = 1)    
        except:
            string = 'Failed'
            faileddf = pd.DataFrame([string])
            floatlist2.append('Failed')
            DoubleBoltFitParams = pd.concat((DoubleBoltFitParams, faileddf), axis = 1)
            pass
    bin = [] 
    for i in range(len(floatlist)):
        if floatlist2[i] == "Failed":
            bin.append('single')
        elif floatlist2[i] < floatlist[i]:
            bin.append('double')
        else:
            bin.append('single')
    ID = pd.DataFrame({"SIN_Single Boltzmann":floatlist,"SIN_Double Boltzmann":floatlist2,"SIN_Bin":bin}) 
    ID = ID.transpose()
    ID.columns = SlowInactivationDf.columns.values.tolist()
    DoubleBoltFitParams.columns = SlowInactivationDf.columns.values.tolist()
    DoubleBoltFitParams = DoubleBoltFitParams.rename(index={0:'SIN_y0', 1:'SIN_A', 2:'SIN_Va', 3:'SIN_Vb', 4:'SIN_k1', 5:'SIN_k2', 6:'SIN_p'})
    SingleBoltFitParams.columns = SlowInactivationDf.columns.values.tolist()
    SingleBoltFitParams = SingleBoltFitParams.rename(index={0:'SIN_V0.5',1:'SIN_k'})
    ID_final = pd.concat([ID, SingleBoltFitParams,DoubleBoltFitParams], axis=0)
    ID_final.to_csv(output_path + "/SIN_fit_parameters.csv")
    return 0

# Activation
def conductance(file_paths):
    import pandas as pd
    import numpy as np
    import os
    import glob
    import matplotlib.pyplot as plt
    import chardet
    data_path = file_paths[0]
    param_path = file_paths[1]
    output_path = file_paths[2]
    
    if output_path == "":
        cur_dir = os.getcwd()
        output_path = cur_dir + "/Activation"
    else: 
        output_path = output_path + "/Activation"
    if not os.path.exists(output_path):
        
        os.makedirs(output_path)
    
    with open(data_path, 'rb') as rawdata:
        result = chardet.detect(rawdata.read(100000))
    PeakDf = pd.read_csv(data_path)
    PeakColNames = PeakDf.columns.values.tolist()
    NewCol = []
    for string in PeakColNames:
        new_string = string.replace(":", "_")
        NewCol.append(new_string)
    PeakDf.columns = NewCol
    # Optional - number of rows to drop if desired
    # nrows = 4
    # PeakDf = PeakDf.iloc[:-nrows,:]
    PeakDf.replace(regex=True, inplace=True, to_replace=r'[^0-9.\-]', value=r'')
    PeakDf = PeakDf.astype('float64')
    ParamDf = pd.read_csv(param_path)
    NewCol[0] = 'IDENTIFIER'
    ParamDf.columns = NewCol
    ParamDf.replace(to_replace = ["Failed"], value = 0.00002, inplace = True) 
    PeakDf_Copy = PeakDf.copy()
    PeakDfColumns = PeakDf_Copy.columns.values.tolist()
    #Creates membrane potential dataframe
    MembPotent = PeakDf.iloc[:, 0]
    MembDf = pd.DataFrame(MembPotent)
    
    for i in range(2,len(PeakDfColumns)):
        MembDf['Membrane Potential'+str(i)] = MembDf.iloc[:, 0]
    
    #Renames columns
    MembDf.columns = PeakDfColumns[1:]
    #Creates dataframes containing reversal potential and capacitance parameters while preserving column headers
    Vrev = pd.DataFrame(columns=ParamDf.columns)
    Cap = pd.DataFrame(columns=ParamDf.columns)
    RevRows = ParamDf.loc[0, :]
    Vrev = Vrev.append(RevRows, ignore_index = True)
    CapRows = ParamDf.loc[1, :]
    Cap = Cap.append(CapRows, ignore_index = True)
    # PeakDf_Copy = PeakDf[PeakDfColumns[1:]].div(PeakDf['Membrane Potential'],axis=0)
    PeakDf_Copy = PeakDf[PeakDfColumns[1:]]
    RevDf = pd.DataFrame(columns = PeakDfColumns[1:]).reindex_like(PeakDf_Copy).dropna()
    RevDf = RevDf.append(Vrev, ignore_index = False)
    del RevDf['IDENTIFIER']
    for i in range (1, len(MembPotent)):
        RevDf.loc[i] = RevRows
    DenomDf = MembDf - RevDf
    CondDf = PeakDf_Copy/DenomDf
    NormCond = (CondDf-CondDf.min())/(CondDf.max()-CondDf.min())
    output1 = NormCond
    output1.insert(0,'Membrane Potential (mV)',MembPotent)
    output1['Membrane Potential (mV)'] = 'ACT_' +  output1['Membrane Potential (mV)'].astype(str)

    out1_loc = output_path + "/unfiltered_normalized_conductance_data.csv"
    output1.to_csv(out1_loc) 
    
    NormCond = NormCond.iloc[: , 1:]
    NormCond = NormCond.dropna(axis=1, how='all')
    VoltError = pd.DataFrame()
    #Correction for voltage error
    for column in NormCond:
        if ((NormCond[column].diff() > 0.4).any()):
            VoltError = pd.concat((VoltError, NormCond[column]), axis = 1)
            NormCond.drop(column, inplace=True, axis=1)
    for column in NormCond:
        if ((NormCond[column].diff() < -0.4).any()):
            VoltError = pd.concat((VoltError, NormCond[column]), axis = 1)
            NormCond.drop(column, inplace=True, axis=1)
    output2 = NormCond
    output2.insert(0,'Membrane Potential (mV)',MembPotent)
 
    out2_loc = output_path + "/filtered_normalized_conductance_data.csv"    
    output2.to_csv(out2_loc) 
    
    NormCond = NormCond.iloc[: , 1:]
    from scipy import optimize
    def Boltzmann(x, v, k):
        return 1/(1+np.exp((v-x)/k))
    
    v_0 = -30
    k_0 = 9
    
    def DoubleBoltzmann(x, y0, A, z1, z2, k1, k2, p):
        B = np.exp((x-z1)/k1)
        C = np.exp((x-z2)/k2)
        return y0+ A*(p/(1+B)+(1-p)/(1+C))
    
    y0_0 = 0.009
    A_0 = 33
    z1_0 = -42
    z2_0 = -30
    k1_0 = -8.3
    k2_0 = -3.2
    p_0 = 0.9
    
    #Creating empty structures for RMSD calculations - Single Boltzmann
    # print(NormCond)
    CurrStd = pd.DataFrame(NormCond.std(axis = 0, ddof=0))
    CurrStd = CurrStd.transpose()
    CurrMean = pd.DataFrame(NormCond.mean())
    CurrMean = CurrMean.transpose()
    SingleBoltFitParams = pd.DataFrame()
    floatlist = []
    Volt = MembPotent
    #Creating empty structures for RMSD calculations - Double Boltzmann
    DoubleBoltFitParams = pd.DataFrame()
    floatlist2 = []
    # print (NormCond)
    for column in NormCond:
        try:
            Curr = NormCond[column].values
            params, params_covariance = optimize.curve_fit(Boltzmann, Volt, Curr, p0 = ([v_0, k_0]))
            plt.figure(figsize = (6,4))
            plt.scatter(Volt, Curr, label = NormCond[column].name)
            plt.plot(Volt, Boltzmann(Volt, params[0], params[1]), label = 'Single Boltzmann')
            plt.legend(loc='best')
            out_img_path = output_path + "/Fit_visualizations/"
            if not os.path.exists(out_img_path):
                os.makedirs(out_img_path)
            plt.savefig(out_img_path + column +'_single_conductance.png')
            diff = Curr - Boltzmann(Volt, params[0], params[1])
            rms = (np.sqrt(np.sum(np.square(diff)/len(diff)))) 
            normrms = rms / CurrStd.at[0,column]
            floatlist.append(normrms)
            params = pd.DataFrame(params)
            SingleBoltFitParams = pd.concat((SingleBoltFitParams, params), axis = 1) 
            params2, params_covariance = optimize.curve_fit(DoubleBoltzmann, Volt, Curr, p0 = ([y0_0, A_0, z1_0, z2_0, k1_0, k2_0, p_0]), maxfev = 300)
            plt.figure(figsize = (6,4))
            plt.scatter(Volt, Curr, label = NormCond[column].name)
            plt.plot(Volt, DoubleBoltzmann(Volt, params2[0], params2[1], params2[2], params2[3], params2[4], params2[5], params2[6]), label = 'Double Boltzmann')
            plt.legend(loc='best')
            plt.savefig(out_img_path + column +'_double_conductance.png')
            diff2 = Curr - DoubleBoltzmann(Volt, params2[0], params2[1], params2[2], params2[3], params2[4], params2[5], params2[6])
            rms2 = (np.sqrt(np.sum(np.square(diff2)/len(diff2))))
            normrms2 = rms2 / CurrStd.at[0,column]
            floatlist2.append(normrms2)
            params2 = pd.DataFrame(params2)
            DoubleBoltFitParams = pd.concat((DoubleBoltFitParams, params2), axis = 1)
            
        except:
            string = 'Failed'
            faileddf = pd.DataFrame([string])
            floatlist2.append('Failed')
            DoubleBoltFitParams = pd.concat((DoubleBoltFitParams, faileddf), axis = 1)
            pass
    ColNames = NormCond.columns.values.tolist()
    # print(ColNames)
    bin = [] 
    for i in range(len(floatlist)):
        if floatlist2[i] == "Failed":
            bin.append('single')
        elif floatlist2[i] < floatlist[i]:
            bin.append('double')
        else:
            bin.append('single')
    ID2 = pd.DataFrame({"ACT_Single Boltzmann":floatlist,"ACT_Double Boltzmann":floatlist2,"ACT_Bin":bin}) 
    ID2 = ID2 .transpose()
    ID2.columns = ColNames[:]
    DoubleBoltFitParams.columns = ColNames[:]
    DoubleBoltFitParams = DoubleBoltFitParams.rename(index={0:'ACT_y0', 1:'ACT_A', 2:'ACT_Va', 3:'ACT_Vb', 4:'ACT_k1', 5:'ACT_k2', 6:'ACT_p'})
    SingleBoltFitParams.columns = ColNames[:]
    SingleBoltFitParams = SingleBoltFitParams.rename(index={0:'ACT_V0.5',1:'ACT_k'})
    ID_final = pd.concat([ID2, SingleBoltFitParams,DoubleBoltFitParams], axis=0)
    ID_final.to_csv(output_path + "/Activation_fit_parameters.csv")

#Recovery from Inactivation
def RecInactivation (file_paths):    
    import pandas as pd
    import numpy as np
    import os
    import glob
    import matplotlib.pyplot as plt
    data_path = file_paths[0]
    output_path = file_paths[1]
    if output_path == "":
        cur_dir = os.getcwd()
        output_path = cur_dir + "/Rec_inactivation"
    else: 
        output_path = output_path + "/Rec_inactivation"
    if not os.path.exists(output_path):
        
        os.makedirs(output_path)
    RecInactivationDf = pd.read_csv(data_path)
    nan_value = float("NaN")
    RecInactivationDf.replace("", nan_value, inplace = True)
    RecInactivationDf.dropna(how='all', axis = 1, inplace = True)
    RecInactivationColNames = RecInactivationDf.columns.values.tolist()
    NewCol = []
    for string in RecInactivationColNames:
        new_string = string.replace(":", "_")
        NewCol.append(new_string)
    RecInactivationDf.columns = NewCol
    RecInactivationDf.replace(regex=True, inplace=True, to_replace=r'[^0-9.\-]', value=r'')
    RecInactivationDf = RecInactivationDf.astype('float64')
    Times = RecInactivationDf['Time (ms)']
    RecInactivationDfColumns = RecInactivationDf.columns.values.tolist()
    RecInactivationDf = RecInactivationDf[RecInactivationDfColumns[1:]]

    from scipy import optimize
    def DoubleExp(x, a, b, c, d):
        return (a*np.exp(b*x)+c*np.exp(d*x))
    
    # Starting parameters 
    # a_0 = -70
    # b_0 = 9
    # c_0 = 0
    # d_0 = 0

    floatlist = []
    DoubleExpFitParams = pd.DataFrame()
    
    for column in RecInactivationDf:
        try:
            Curr = RecInactivationDf[column].values
            params, params_covariance = optimize.curve_fit(DoubleExp, Times, Curr)
            plt.figure(figsize = (6,4))
            plt.scatter(Volt, Curr, label = RecInactivationDf[column].name)
            plt.plot(Volt, Boltzmann(Volt, params[0], params[1], params[2], params[3]), label = 'Double Exponential')
            plt.legend(loc='best')
            out_img_path = output_path + "/Fit_visualizations/"
            if not os.path.exists(out_img_path):
                os.makedirs(out_img_path)
            plt.savefig(out_img_path + column +'_REC.png')
            #plt.savefig(column +'_REC.png')
            #plt.show()
            diff = Curr - DoubleExp(Times, params[0], params[1], params[2], params[3])
            rms = (np.sqrt(np.sum(np.square(diff)/len(diff))))
            normrms = rms / CurrStd.at[0,column]
            floatlist.append(normrms)
            params = pd.DataFrame(params)
            DoubleExpFitParams = pd.concat((SingleBoltFitParams, params), axis = 1) 
        except:
            pass
    
    return 0

# If recovery from inactivation data is fit in another program, this function allows for appending those results to the master data
def AddendRecInactivation ():    
    import pandas as pd
    import numpy as np
    import os
    import glob
    import matplotlib.pyplot as plt
    
    MasterFile = pd.read_csv('INSERT PATH TO FILE WITH MASTER DATA, GENERATED BY PROCESS FUNCTION')
    ShortRecParam = pd.read_csv('INSERT PATH TO FILE WITH SHORT RECOVERY FROM INACTIVATION FITS')
    ShortRecParam.rename(columns = {list(ShortRecParam)[0]:'Variable'}, inplace=True)
    nan_value = float("NaN")
    ShortRecParam.replace("", nan_value, inplace = True)
    ShortRecParam.dropna(how='all', axis = 1, inplace = True)
    ShortRecParam.dropna(how='all', axis = 0, inplace = True)
    ShortRecParamNames =  ShortRecParam.columns.values.tolist()
    NewCol = []
    for string in  ShortRecParamNames:
        new_string = string.replace(":", "_")
        NewCol.append(new_string)
    ShortRecParam.columns = NewCol
    ShortRecParam.at[0,"Variable"] = "XX ms Recovery from Inactivation"
    
    LongRecParam = pd.read_csv('INSERT PATH TO FILE WITH LONG RECOVERY FROM INACTIVATION FITS')
    LongRecParam.rename(columns = {list(LongRecParam)[0]:'Variable'}, inplace=True)
    nan_value = float("NaN")
    LongRecParam.replace("", nan_value, inplace = True)
    LongRecParam.dropna(how='all', axis = 1, inplace = True)
    LongRecParam.dropna(how='all', axis = 0, inplace = True)
    LongRecParamNames =  LongRecParam.columns.values.tolist()
    NewCol = []
    for string in  LongRecParamNames:
        new_string = string.replace(":", "_")
        NewCol.append(new_string)
    LongRecParam.columns = NewCol
    LongRecParam.at[0,"Variable"] = "XXX ms Recovery from Inactivation"

    vertical_stack = MasterFile.append(pd.Series("", index=MasterFile.columns), ignore_index=True)
    vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
    vertical_stack = pd.concat([vertical_stack,ShortRecParam],axis = 0)
    vertical_stack = vertical_stack.append(pd.Series("", index=vertical_stack.columns), ignore_index=True)
    vertical_stack = pd.concat([vertical_stack,LongRecParam],axis = 0)
    vertical_stack.to_csv('INSERT FILE NAME FOR MASTER DATA WITH RECOVERY FROM INACTIVATION')
    
    return 0

def my_function(function, file_paths):
    
    if function == "Activation":
        conductance(file_paths)
    elif function == "Fast Inactivation":
        fast_inactivation(file_paths)
    elif function == "Slow Inactivation":
        slow_inactivation(file_paths)
    elif function == "Recovery from Inactivation":
        RecInactivation(file_paths)
    elif function == "Process":
        process(file_paths)
    else:
        return 0
    
    #print(out1_loc)
    # Your code here

    #print(f"Selected function: {function}")

    #print(f"Selected files: {file_paths}")
  

 

layout = [

    [sg.Text("Select a function:",  font=("Arial", 15, "bold"), background_color="#444444")],

    [sg.Button("Activation", font=("Arial", 15, "bold"), button_color=("black", "lavender"), size=(15, 3)),

     sg.Button("Fast Inactivation", font=("Arial", 15, "bold"), button_color=("black", "lavender"), size=(15, 3)),
     
     sg.Button("Slow Inactivation", font=("Arial", 15, "bold"), button_color=("black", "lavender"), size=(15, 3)),

     sg.Button("Recovery from Inactivation", font=("Arial", 15, "bold"), button_color=("black", "lavender"), size=(15, 3)),

     sg.Button("Process",  font=("Arial", 15, "bold"), button_color=("black", "#EEA13B"), size=(20, 3))],
    
    [sg.Submit()]

]







 

window = sg.Window("Automated Patch Clamp Analysis", layout, background_color="#444444")

event, values = window.read()

 

while True:
    #print(event)
    
    

    if event == "Activation":
        window.close()
        #print('aaa')
        

        layout = [

            [sg.Text("Select an Activation data file:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FileBrowse()],

            [sg.Text("Select an Activation reversal potential file:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FileBrowse()],
            
            [sg.Text("Select the output folder:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FolderBrowse()],

            [sg.Submit()]

        ]
        
        window = sg.Window("File Selector", layout, background_color="#444444")
        event2, values = window.read()
        #print(event2)
 
        if event2 == "Submit":
            function = event
            file_paths = values
    
            my_function(function, file_paths)
        
        #print(function)
        #print(file_paths)
        window.close()
        window.close()
        break

        


    elif event == "Fast Inactivation":
        window.close()
        
        layout = [

            [sg.Text("Select an Inactivation data file:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FileBrowse()],
            
            [sg.Text("Select the output folder:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FolderBrowse()],

            [sg.Submit()]

        ]
        window = sg.Window("File Selector", layout, background_color="#444444")
        event2, values = window.read()
 
        if event2 == "Submit":
            function = event
            file_paths = values
    
            my_function(function, file_paths)
        
        window.close()
        window.close()
        break

    elif event == "Slow Inactivation":
        window.close()
        
        layout = [

            [sg.Text("Select a Slow Inactivation data file:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FileBrowse()],
            
            [sg.Text("Select the output folder:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FolderBrowse()],

            [sg.Submit()]

        ]
        window = sg.Window("File Selector", layout, background_color="#444444")
        event2, values = window.read()
 
        if event2 == "Submit":
            function = event
            file_paths = values
    
            my_function(function, file_paths)
        
        window.close()
        window.close()
        break

    elif event == "Process":
        window.close()
        
        layout = [

            [sg.Text("Select the previously generated Activation output file (unfiltered_normalized_conductance_data):", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FileBrowse()],
            
            [sg.Text("Select the Activation capacitance file:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FileBrowse()],
            
            [sg.Text("Select the previously generated Activation fit parameters file:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FileBrowse()],
            
            [sg.Text("Select the Activation reversal potential file:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FileBrowse()],
            
            [sg.Text("Select the previously generated Fast Inactivation output file (unfiltered_normalized_FIN_data):", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FileBrowse()],
            
            [sg.Text("Select the Fast Inactivation capacitance file:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FileBrowse()],
            
            [sg.Text("Select the previously generated Fast Inactivation fit parameters file:", font=("Arial", 12, "bold"), background_color="#444444")],
            
            [sg.Input(), sg.FileBrowse()],
            
            [sg.Text("Select the previously generated Slow Inctivation output file (unfiltered_normalized_conductance_data):", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FileBrowse()],
            
            [sg.Text("Select the Slow Inactivation capacitance file:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FileBrowse()],
            
            [sg.Text("Select the previously generated Slow Inactivation fit parameters file:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FileBrowse()],
            
            [sg.Text("Select the output folder:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FolderBrowse()],

            [sg.Submit()]

        ]
        window = sg.Window("File Selector", layout, background_color="#444444")
        event2, values = window.read()
 
        if event2 == "Submit":
            function = event
            file_paths = values
    
            my_function(function, file_paths)
        
        window.close()
        window.close()
        break
    
    elif event == "Recovery from Inactivation":
        window.close()

        layout = [

            [sg.Text("Select a Recovery from Inactivation data file:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FileBrowse()],
            
            [sg.Text("Select the output folder:", font=("Arial", 12, "bold"), background_color="#444444")],

            [sg.Input(), sg.FolderBrowse()],

            [sg.Submit()]

        ]
        window = sg.Window("File Selector", layout, background_color="#444444")
        event2, values = window.read()
 
        if event2 == "Submit":
            function = event
            file_paths = values
    
            my_function(function, file_paths)
    
        window.close()
        window.close()
        break


 


 

"""def my_function(file_path):

    # Your code here
    print(f"Selected function: {function}")
    print(f"Selected file: {file_path}")

 

layout = [

    [sg.Text("Select a function:")],

    [sg.Radio("Activation", "FUNCTION", default=True),

     sg.Radio("Fast Inactivation", "FUNCTION"),

     sg.Radio("Slow Inactivation", "FUNCTION"),

     sg.Radio("Recovery from Inactivation", "FUNCTION")],

    [sg.Text("Select a file:")],

    [sg.Input(), sg.FileBrowse()],

    [sg.Submit()]

]

 

window = sg.Window("Function Selector", layout)

event, values = window.read()

 

if event == "Submit":

    function = values[0]

    file_path = values[1]

    my_function(function, file_path)

 

window.close()

 

if event == "Submit":

    file_path = values[0]

    my_function(file_path)

 

window.close()"""


#Set directory for outputs
"""path = 'XXXXXXXXX'
os.chdir(path)"""

#Process function concatenates results from files generated by other functions

# Uncomment name of function to run
#if __name__ == '__main__':
    # inactivation()
    # conductance()
    # process()
    # RecInactivation()
    # AddendRecInactivation()
