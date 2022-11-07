import dash
from dash import html

# Parte 1
app=dash.Dash(__name__)

app.layout=html.Div(children=[
    html.Img(src='assets\\sustainability.jpg',
    style={'width':'50%','border':'1px solid red'},
    alt='image'),

    html.H1(children='Importance of Sustainability',style={'color':'blue'}),
    html.P('Sustainability will help us to live better for a long time', style={'color':'green','border':'2px solid blue'})
])

if __name__=='__main__':
    app.run_server(debug=True,port=8051)

