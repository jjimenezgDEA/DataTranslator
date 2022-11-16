import dash
from dash import html
from dash.dependencies import Input,Output
from dash import dcc 
import plotly.express as px
import pandas as pd
import numpy as np

df=pd.read_csv('dfv.csv')

app=dash.Dash(__name__)

app.layout=html.Div([ 

    #first row
    html.Div(children=[ 
        html.H1(children='Gráfico de Likes vs Dislikes',style={'color':'skyblue'}),
        html.H2(children='Case Study, Data Translator',style={'color':'skyblue'}),
        html.H3(children='José Jiménez González & Iván López García',style={'color':'skyblue'}),
    ]),

    #second row
    html.Div([ 
        #first col of second row
        html.Div([ 
            html.Img(
                src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Bot%C3%B3n_Me_gusta.svg/1200px-Bot%C3%B3n_Me_gusta.svg.png',
                style={'width':'50%'}),
#        ],style={'display':'inline-block','vertical-align':'top','margin-left':'3vw','margin-top':'3vw'}),
        ],style={'display':'inline-block','width':'30%','vertical-align':'top'}),
    #second col of second row
        html.Div([ 
            dcc.Dropdown(
                id='category-dropdown',
                options=[{'label':i,'value':i} for i in np.sort(df['category_title'].unique())],
                value='Entertainment'
                ),
            dcc.Graph(id='likes_plot')
        ],style={'display':'inline-block','width':'65%','vertical-align':'top'})#,style={'display':'inline-block','vertical-align':'top','margin-left':'3vw','margin-top':'3vw'})
    ])
])


@app.callback( 
    Output('likes_plot','figure'),
    Input('category-dropdown','value')
)

def update_figure(selected_category):
    filtered_df=df[df.category_title==selected_category]
    fig=px.scatter(filtered_df,x='likes',y='dislikes',trendline='ols',trendline_color_override='black')
    fig.update_layout(transition_duration=400)
    return fig

if __name__=='__main__':
    app.run_server(debug=True)