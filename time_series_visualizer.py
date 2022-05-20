import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df_original = pd.read_csv("fcc-forum-pageviews.csv",index_col=['date'])
df_original.sort_values('value', inplace=True)

low_df = int(df_original.shape[0]*0.025)
high_df = int(df_original.shape[0]*0.975)
df = df_original[low_df+1:high_df]

df = df.sort_index()

df2 = df.copy()

df2['Year'] = (pd.DatetimeIndex(df2.index).year)
df2['Month'] = (pd.DatetimeIndex(df2.index).month)

df2.sort_values('Month',inplace=True)

df2.replace({1:'January',2:'February',3:'March',4:'April',5:'May',
                 6:'June',7:'July',8:'August',9:'September',10:'October',
                 11:'November',12:'December'}, inplace=True)      

def draw_line_plot():
    df.index = pd.to_datetime(df.index).date
    fig, ax = plt.subplots(figsize=(20, 5))
    
    plt.plot(df)
    plt.legend([], frameon=False)
    
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
  
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
     
    fig, ax = plt.subplots(figsize=(10, 10))
  
    sns.barplot(data=df2,x='Year',y='value',hue='Month',
            palette='tab20',saturation=1,)

    plt.legend(title='Months',loc=2)

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    fig, axes = plt.subplots(1, 2,figsize=(15, 5),)
    sns.boxplot(data=df2,x='Year',y='value',linewidth=1,ax=axes[0])
    sns.boxplot(data=df2,x='Month',y='value',ax=axes[1])
    
    axes[0].set_ylabel('Page Views')
    axes[1].set_ylabel('Page Views')
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xticks(labels=month,ticks=range(12))

    fig.savefig('box_plot.png')
    return fig