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
df = pd.read_csv(os.path.dirname(__file__)+"/letter_frequency.csv") # reading csv files
print(df.keys())

#%%
plt.plot(df['letter'], df.frequency,label='Ransom')# label will let us create a legend for our graph
plt.show()

# %%
plt.plot(
    df.letter, 
    df.frequency,
    label='letter frequency',
    color="DeepPink",
    linewidth=2,
    linestyle=":", #possible "-." ":" "--" "-"
    marker="d" # possible "x" "s" "o" "*" "h" "d"
    )# label will let us create a legend for our graph

plt.legend(fontsize = 15)
plt.xlabel('letter',fontsize=20,color="red")
plt.ylabel('frequency',fontsize=20,color="blue")

plt.text(0,0.07,'this is c')
plt.title('Dalideco', fontsize=40)
plt.show()


#%%
print(type(df))
print(type(df.letter))
print(df.head())

# %%
plt.scatter(
    df.letter, 
    df.frequency,
    label='letter frequency',
    color="DeepPink",
    marker="s" # possible "x" "s" "o" "*" "h" "d"
    )# label will let us create a legend for our graph

plt.legend(fontsize = 15)
plt.xlabel('letter',fontsize=20,color="red")
plt.ylabel('frequency',fontsize=20,color="blue")

plt.text(0,0.07,'this is c')
plt.title('Dalideco', fontsize=40)
plt.show()
plt.clf()

#%%
plt.hist(df.frequency)# can be replaced by df['frequency'].hist
#alpha argument sets the transparency
plt.show()
plt.clf()

# %%
plt.bar(df.x, df.y ,yerr=df.error,bottom=df.z) #vertical bars
#use teh bottom argument to both cat and dog kidnapping on top of each other for exp
plt.barh(df.x,df.y)#horizontal bars
plt.hist(df.mass,bins=40,range=(2,12),density=True) #histogram bins = number of divisions and rage = min and max to show
#density= True makes the bars use proportion insted of count
plt.xscale('log')# puts the x axis on a logarithmic scale
plt.clf()#clears graph so you can start fresh
plt.yticks([0,2,4,6,8,10])#modifies the values shown on the yaxis
plt.yticks([0,2,4,6,8,10],['0B','2B','4B','6B','8B','10B']) #modifies the variables on the y axis names
plt.scatter(x,y, s=popsize)# s is the array that contains the size of each point
plt.grid(True) #shows gridlines 


#introduction to matplotlib 
fig,ax = plt.subplots()# we can use plt.subplots for multiple plots
plt.show()#fig is the figure and ax represents the axis
ax.plot(seattle_weather['month'],seattle_weather['MLY'],marker="",linestyle="",color="")
ax.set_xlabel('xlabel', color='red')# same as plt.xlabel along with .set_ylabel() and .set_title()
ax.subplots(3,2,sharey=True)#example 
#sharedy set to True makes tche graphs have the same range in the y axis
ax[0,0]plot()#example
ax2 = ax.twinx()#a twin that shares the same x axis but different y axis
ax.tick_params('y', colors='red')
ax.annotate(">1 degree", xy=(pd.Timestamp("2018-05-05"),1), \
    xytext=(pd.Timestamp('2008-10-08')), \
    arrowprops={"arrowstyle":"->","color":"gray"})#annotate a place in the graph
#pd.Timestamp makes is doable with date objects
#xytext optional argument that decides the place of the text
# we add empty arrowprops argument to show arrow and we can custmize it
ax.bar()# corresponds to plt.bar()
ax.set_xticklabels(medium.index, rotation = 90)
ax.hist(y, label ="", bins=[],histtype="step")#same as hist , we can put bins to be a sequence of numbers
# histtype optional argument put to "step" causes histogram's body to be transparent(only border shown)
ax.errorbar(x,y , yerr=z)#line plot with error on each point
ax.boxplot([])# create a box plot
