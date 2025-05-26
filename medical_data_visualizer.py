import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df =pd.read_csv("medical_examination.csv")

# 2
overweight=[]
BMI=(df["weight"]/((df["height"]*0.01)**2))
for i in BMI:
    if i>25:
        overweight.append(1)
    else:
        overweight.append(0)

df['overweight'] = overweight

# 3
gluc=[]
chol=[]
for val in df["gluc"]:
    if val==1:
        gluc.append(0)
    elif val>1:
        gluc.append(1)
    
for val in df["cholesterol"]:
    if val==1:
        chol.append(0)
    elif val>1:
        chol.append(1)
df["cholesterol"]=chol
df["gluc"]=gluc

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        id_vars=['cardio'], 
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    long= sns.catplot(
        data=df_cat,
        kind='bar',
        x='variable',
        y='total',
        hue='value',
        col='cardio'
    )


    # 8
    fig=long.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df1=df[df['ap_lo'] <= df['ap_hi']]
    df2=df1[df1['height'] >= df1['height'].quantile(0.025)]
    df3=df2[df2['height'] <= df2['height'].quantile(0.975)]
    df4=df3[df3['weight'] >= df3['weight'].quantile(0.025)]

    df_heat = df4[df4['weight'] <= df4['weight'].quantile(0.975)].set_index("id")

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr,ax=ax)

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
