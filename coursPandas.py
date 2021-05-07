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
#can use parse_dates argument that takes an array containing the date columns
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



df.drop_duplicates(subset="column")#argument subset can receive an array
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
# we can also use isnull() method
df.isna().any # returns if there are any missing values to each column
df.isna().sum().plot(kind="bar") # plots the missing data for each column on a bar
df.dropna() # removes rown containing NaN
df.fillna(0) #replaces all NaNs with 0 
pd.DataFrame(dictionary) #converts dictionary into pandas dataFrame
pd.read_csv('name.csv')#reads csv file into a dataframe
df.to_csv('name.csv')#writes dataframe in a csv file
df.plot(x="",y="",kind="")


#mergin 
df.merge(df1 , on="ward",suffixes=('_df','_df1'),how="left") # same as sql inner join on ward
#suffixes argument allows us to tell the difference between the columns 
#argument how specifies if it is a left or right join
df.merge(df1, on="" , how="inner/outer/left/right",right_on="",left_on="", \
    right_index="True/False" , left_index="True/False", indicator='True/False',\
        validate="None/one_to_one/one_to_many/many_to_many/many_to_one") 
# we can use left_on and right_on for different column names 
# if for exp left_on is an index specify left_index=True
#set indicator to True to get a column _merge that specifies where de row came from(left_only/right_only/both)

df['column'].isin(df1['column'])# works for each row of the df1 column
pd.concat([df1,df2,df3], ignore_index=True, \
    keys=['table1','table2','table3'],sort="True/False",join="inner/outer",\
        verify_integrity="True/False")
#ignore index true create new index and removes the tables indexes
#sort leaves the rows sorted as they were in their original table
df.append()#same as concat but without the keys and join argument
pd.merge_ordered(fill_method="ffill")# same as df.merge() 
#fill_method decides how to fill NaN
df.corr()#prints correlation matrix
pd.merge_asof(df,df1, on="", suffixes=('',''), direction="backward/forward/nearest")
#default backward direction returns the columns oof the right table 
#   where the on is the nearest inferior to the on of the left table row
df.melt(id_vars=[], value_vars=[], var_name='', value_name='')
#melts table of many columns with more rows with variable and value column
pd.to_datetime(df['year']+'-'+df['month'])#converts to date type
df['column'].unique()#get a series of all the different values of that column
