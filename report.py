import os
import pandas_profiling
import numpy as np
from pandas import read_csv
import matplotlib
import matplotlib.pyplot as plt

from pandas import DataFrame
matplotlib.rcParams["font.sans-serif"]=["SimHei"]#显示中文标签
plt.rcParams["axes.unicode_minus"]=False
matplotlib.use("Agg")
filename=os.listdir("./database")
for file in filename:
    data=read_csv("./database/"+file,encoding="gb18030")
    try:
        columns=list(data.iloc[0,:].values)
        data_=DataFrame(list(data.iloc[1:,1:].values),columns=columns[1:])
        profile=pandas_profiling.ProfileReport(data_)
        profile.to_file("./report/"+file[:-3]+"html")
    except:
        print("File {} is not ready!".format(file))