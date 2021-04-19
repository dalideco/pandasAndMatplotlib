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
plt.plot(df.index, df.frequency,label='Ransom')# label will let us create a legend for our graph
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
plt.hist(df.frequency)
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