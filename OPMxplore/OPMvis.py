import pandas as pd
import plotly.graph_objs as go
import seaborn as sns
from matplotlib import pyplot as plt

def make_plotly_dict(df,x_col,y_col,z_col,hover,color_by,colorbar_title,chart_title):
    trace1 = go.Scatter3d(
        x=df[x_col],
        y=df[y_col],
        z=df[z_col],
        text=df[hover],
        mode='markers',
        marker=dict(
            color = df[color_by],
            colorscale = 'Viridis',
            colorbar = dict(title = colorbar_title),
            line=dict(color='rgb(140, 140, 170)')
        )
    )

    d=[trace1]
    l=dict(height=700, width=1000, title=chart_title)
    fig = dict(data=d, layout=l)
    return fig

# plotting functions
def stat_plot(df, xvar, yvar, title):
    # plot aesthetics
    sns.set()
    sns.set_style('whitegrid')
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 8)
    # get data
    df_inp = df
    # Create violin plot    
    ax1 = sns.violinplot(x=xvar,
                         y=yvar,
                         data=df_inp,
                         saturation=0.5,
                         inner='box', # Remove the bars inside the violins
                         ax=ax)

    ax1 = sns.swarmplot(x=xvar, y=yvar, data=df, alpha='0.5', color='k')
    # Set title with matplotlib
    plt.title(title)

def brill_3d(high_type,df,x,y,z):
    """
    high_type: choose 'Transmembrane', 'Peptides', 'Monotopic/peripheral'
    query_id: df_id 
    x:column name
    y:column name
    z:column name
    """
    selection=df[df['type']==high_type]
    selection.iplot(kind='scatter3d',
                    x=x,
                    y=y,
                    z=z,
                    size=15,
                    categories='class',
                    text='name',
                    title='Brilliant 3D Protein Scatter', 
                    colors=['blue','pink','yellow'],
                    width=0.5,
                    margin=(0,0,0,0),
                    opacity=1,
                    theme='white')

def swarm_plot(df, xvar, yvar, title):
    # plot aesthetics
    sns.set()
    sns.set_style('whitegrid')
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 8)
    # get swarm
    ax1 = sns.swarmplot(x=xvar, y=yvar, data=df, alpha='0.5', color='r')
    # Set title with matplotlib
    plt.title(title)

def scatter_plot(df, category):
    
    df.iplot(
            kind = 'scatter',
            mode = 'markers',
            y = 'thickness', 
             x = 'gibbs',
             text='pdbid',
             xTitle = 'dG to fold or insert in membrane',
             yTitle = 'Hydrophobic_Thickness',
             theme='white',categories=category, colors = ['blue','pink','yellow','green']
             )    