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
df.sort_values("column")#or array and ascending boolean argument



df.drop_duplicates(subset="column")#argument subet can receive an array
pandaSeries.value_counts()# returens the number of each value
pandaSeries.value_counts(normalize = True,sort=True) #gets proportions and gets them sorted
.sum()
df.groupby('type',as_index=True)['column'].agg([min,max,sum,np.mean,np.median]) # an array could be used for multiple columns
#in agg we can specify the name of the columns with a dictionary like ththis {'account': 'count'}
# as_index argument decides whether or not to add default index
df.pivot_table(values="weight_kg",index="type",aggfunc=[np.median, np.mean, min ,max])#does the saem thing . 
#we can another column with columns argument
#fill_value= 0 replaces NaN with 0
#margins = True add an all column (for each type in this case)
df.set_index("names")#can use multiple columns with array
df.reset_index()#can set argument drop to True to delete previous index
df.sort_index(level=['color','type'],ascending=[True,False])

#visualizing with pyplot

df['column'].hist()#same as plt.hist(df['column'])
df.plot(x="", y="", kind="line",rot=45)
#kind can be scatter or bar
df.isna() # returns dataframe with false on missing tables and true on non missing
df.isna().any # returns if there are any missing values to each column
df.isna().sum().plot(kind="bar") # plots the missing data for each column on a bar
df.dropna() # removes rown containing NaN
df.fillna(0) #replaces all NaNs with 0 
pd.DataFrame(dictionary) #converts dictionary into pandas dataFrame
pd.read_csv('name.csv')#reads csv file into a dataframe
df.to_csv('name.csv')#writes dataframe in a csv file


#mergin 
df.merge(df1 , on="ward",suffixes=('_df','_df1'),how="left") # same as sql inner join on ward
#suffixes argument allows us to tell the difference between the columns 
#argument how specifies if it is a left or right join