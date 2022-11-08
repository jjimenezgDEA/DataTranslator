import dash
from dash import html
from dash.dependencies import Input,Output
from dash import dcc 
import plotly.express as px
import pandas as pd

df=pd.read_csv('dfv.csv')

app=dash.Dash(__name__)

app.layout=html.Div(children=[ 
    html.H1(children='Gráfico de Likes vs Dislikes',style={'color':'skyblue'}),
    dcc.Graph(id='likes_plot'),
])


if __name__=='__main__':
    app.run_server(debug=True)