# -*- coding: utf-8 -*-
"""
Created on Sun May 10 08:13:04 2020

@author: Christens
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output
from dash.dependencies import Input, Output
import plotly.graph_objs as go


#colors = {"background": "#F3F6FA", "background_div": "white", 'text': '#7FDBFF'}
#df = pd.read_csv('assets/Ohio_Brews_4app.csv')

tab_1_layout = html.Div([
            # html.H3('Patient Demographics'),
             dbc.Row([html.Div([
#                    dbc.Col(html.Div([
#                        html.H6('Ohio Brew Map'),#, style={'textAlign': 'center'}),
#                        html.Iframe(id='map',srcDoc=open('assets/CountyBrewMap.html').read(),width='50%', height='600')
#
#                    ]), width=5),

                    dbc.Col(html.Div([
                        html.H6('Curling Club Map'),#, style={'textAlign': 'center'}),
                        html.Iframe(id='map',srcDoc=open('assets/CurlClubMap.html').read(),width='50%', height='600')

                    ]), width={"size": 6, "offset": 3}),
                ])]),

                dbc.Row(html.Div([
                    html.Div([
                        html.H6('Race - Age Disrtibution', style={'textAlign': 'center'}),
                        dcc.Graph(
                                id='example-graph-6',
                                figure={
                                'data': [
                                        #go.Scatter(
                                                #x=df['Latitude'],
                                                #y=df['Latitude'],
                               #)
                                ],
                                'layout': {
                                    'title': 'Graph-6'
                                }
                            }
                        )
                    ])
                ])
                )
            ]
        )