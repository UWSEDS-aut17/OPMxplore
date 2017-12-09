import pandas as pd
import plotly.graph_objs as go

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