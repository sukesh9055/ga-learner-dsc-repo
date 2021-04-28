# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
df=pd.read_csv(path)

df["Gender"].replace("-","Agender", inplace=True)
df.corr()
total_high=df["Total"].quantile(q=0.99)
super_best=df[df["Total"]>total_high]
super_best_names=list(super_best["Name"])
print(super_best_names)
# Code starts here



