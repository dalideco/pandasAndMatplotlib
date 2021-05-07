import seaborn as sns

#%%
sns.countplot(x="column",data=df,hue="column" )
sns.scatterplot(x="column",y="column",data=df, hue="column", hue_order=[] , 
    size="column",
    col="",
    row="",
    col_order=[],
    row_order=[],
    col_wrap=2
    )
sns.relplot(kind="line/scatter", x="",y="",data=df , hue="",hue_order="",hue="",style="",
    markers=True, dashes=False, ci="sd")

#countplot is same as bar
#scatterplot is same as scatter hue=different_colors, size=different_sizes, style=different_styles
#_order modifies the order
#markers add marks points
#dashes=False removes difference in lines
#style makes difffrence style in both lines and markers
