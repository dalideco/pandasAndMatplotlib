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
# %%
