import pandas as pd
import plotly.graph_objs as go
import seaborn as sns
from matplotlib import pyplot as plt

# def make_plotly_dict(df,
#                      x_col,
#                      y_col,
#                      z_col,
#                      hover,
#                      color_by,
#                      colorbar_title,
#                      chart_title):
#     trace1 = go.Scatter3d(
#         x=df[x_col],
#         y=df[y_col],
#         z=df[z_col],
#         text=df[hover],
#         mode='markers',
#         marker=dict(
#             color = df[color_by],
#             colorscale = 'Viridis',
#             colorbar = dict(title = colorbar_title),
#             line=dict(color='rgb(140, 140, 170)')
#         )
#     )
#
#     d=[trace1]
#     l=dict(height=700, width=1000, title=chart_title)
#     fig = dict(data=d, layout=l)
#     return fig


# plotting functions
def stat_plot(df, xvar, yvar, title):
    """
    Plots ...

    Keyword arguments:
    df : pandas.DataFrame
        The dataframe to search
    xvar : String
        A string describing the subset of the dataframe to return
        (ex: SELECT "selection" )
    yvar : String
        a string representing any further qualifications to the SQL query,
        (ex: "WHERE name LIKE '%channel%'")
    title : string

    Returns:
    -------
    Return value is a list of lines that were added to the figure object.
    Rendered inline within jupyter notebook using magic %matplotlib inline
    """
    # plot aesthetics
    sns.set()
    sns.set_style('whitegrid')
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 8)
    # Create violin plot
    ax1 = sns.violinplot(x=xvar,
                         y=yvar,
                         data=df,
                         saturation=0.5,
                         inner='box',  # Remove the bars inside the violins
                         ax=ax)

    ax1 = sns.swarmplot(x=xvar,
                        y=yvar,
                        data=df,
                        alpha='0.5',
                        color='k')
    # Set title with matplotlib
    plt.title(title)
    return ax


def brill_3d(high_type, df, xvar, yvar, zvar):
    """
    high_type: choose 'Transmembrane', 'Peptides', 'Monotopic/peripheral'
    df: Pandas DataFrame containing the data to plot
    xvar:column name
    yvar:column name
    zvar:column name
    """
    selection = df[df['type'] == high_type]
    ax = selection.iplot(kind='scatter3d',
                         x=xvar,
                         y=yvar,
                         z=zvar,
                         size=15,
                         categories='class',
                         text='name',
                         title='Brilliant 3D Protein Scatter',
                         colors=['blue', 'pink', 'yellow'],
                         width=0.5,
                         margin=(0, 0, 0, 0),
                         opacity=1,
                         theme='white')
    return ax


def swarm_plot(df, xvar, yvar, title):
    """
    df: Pandas DataFrame containing the data to plot
    xvar:column name
    yvar:column name
    zvar:column name
    """
    # plot aesthetics
    sns.set()
    sns.set_style('whitegrid')
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 8)
    # get swarm
    ax1 = sns.swarmplot(x=xvar, y=yvar, data=df, alpha='0.5', color='r')
    # Set title with matplotlib
    plt.title(title)
    return ax


def scatter_plot(df, category):

    ax = df.iplot(
                  kind='scatter',
                  mode='markers',
                  y='thickness',
                  x='gibbs',
                  text='pdbid',
                  xTitle='dG to fold or insert in membrane',
                  yTitle='Hydrophobic_Thickness',
                  theme='white',
                  categories=category,
                  colors=['blue', 'pink', 'yellow', 'green']
                  )
    return ax
