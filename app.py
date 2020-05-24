import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

myheading='Curling Club Map'
tabtitle='Curling!'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    html.Div([
        html.H6('Curling Club Map'),
        html.Iframe(id='map',srcDoc=open('assets/FullCurlmap.html').read(),width='100%', height='800')
    ]),
    
    ]
)

if __name__ == '__main__':
    app.run_server()
