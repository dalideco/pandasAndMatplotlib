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

df.sort_values("weight_kg") # we can put ascending argument as false and we can also use an array for mutiple columns

#%%
for lab,row in df.iterrows():
    print("{} : {}".format(lab,row['frequency']))

#%%
df[column].cumsum() #returns cumulative sum of column
cummax(), cummin() #etc
df.drop_duplicates(subset="column")#argument subet can receive an array
pandaSeries.value_counts()# returens the number of each value
pandaSeries.value_counts(normalize = True,sort=True) #gets proportions and gets them sorted
.sum()
df.groupby('type').agg([min,max,sum,np.mean,np.median]) # an array could be used for multiple columns
df.pivot_table(values="weight_kg",index="type",aggfunc=[np.median, np.mean, min ,max])#does the saem thing . 
#we can another column with columns argument
#fill_value= 0 replaces NaN with 0
#margins = True add an all column (for each type in this case)
df.set_index("names")#can use multiple columns with array
df.reset_index()#can set argument drop to True to delete previous index
df.sort_index(level=['color','type'],ascending=[True,False])

