#%%
import pandas as pd 
import pathlib
import matplotlib.pyplot as plt
import os

#%%
plt.style.use('seaborn') #possible "fivethirtyeight" "ggplot" "seaborn" "default"

#%%
print("hello")
print(__file__)#/ give file
print(pathlib.Path(__file__).parent.absolute()) # \ give directory
print(pathlib.Path().absolute())# \gives the parent of the directory
print(os.path.dirname(__file__)) # / gives the directory
print(os.path.abspath(__file__))#\gives the file 
print(os.path.dirname(os.path.abspath(__file__)))#\gives the directory


#%%
df = pd.read_csv("letter_frequency.csv") # reading csv files
print(df.keys())
print(df)

#%%
print(type(df))
print(type(df.letter))
print(df.head())


#%%
lett = pd.read_csv('letter_frequency.csv', index_col=0)#it changes the index as the first column of the table
print(lett)

#%%
df.loc["RU"]#get row also double brackets to get it as a dataframe
df.iloc[]#same thing but with numbers 