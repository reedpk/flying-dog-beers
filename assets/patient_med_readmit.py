# -*- coding: utf-8 -*-
"""
Created on Sun May 10 08:31:13 2020

@author: Christens
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import plotly.graph_objs as go

#tab_2_layout = html.Div([
#            html.Div([
#                html.Div([
#                    html.H6('Medical Specialty'),
#                    dcc.Graph(
#                        id='med-graph-1',
#                        figure={
#                            'data': [
#
#                            ],
#                            'layout': {
#                                'title': 'Graph-1'
#                            }
#                        }
#                    )
#                ], className="six columns"),
#
#                html.Div([
#                    html.H6('Readmission'),
#                    dcc.Graph(
#                        id='med-graph-2',
#                        figure={
#                            'data': [
#
#                            ],
#                            'layout': {
#                                'title': 'Graph-2'
#                            }
#                        }
#                    )
#                ], className="six columns"),
#
#            ], className="row", style={"margin": "1% 3%"})
#    ])




df = pd.read_csv('assets/CurlingClub3.csv')
#df = pd.read_csv('CurlingClub3.csv')
#print(df.head())

df = df[['Region','Club','Address','City','State','Type','Sheets','Year_Fnded']]

df2 =df.where(df['Region']=='Grand National Curling Club')
df2=df2.dropna()
#print(df2.head(10))

#OBrew_g=df.groupby('Region')[["Brewery", "County"]].count()
#OBrew_g=OBrew_g.reset_index()
#OBrew_g.columns=['Region','BCount','CCount']
fig =go.Figure(data=[go.Bar(x=df['Region'],y=df['Club'])])

#, y=OBrew_g['Brewery']
tab_2_layout = html.Div([
 dash_table.DataTable(
         id='BrewTable',
         style_data={
        'whiteSpace': 'normal',
        },
        data=df2.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns],
        page_action='none',
        #fixed_columns={'headers': True, 'data': 1},
        style_table={'minWidth': '100%', 'height': '500px', 'overflowY': 'auto'},
        css=[{
        'selector': '.dash-spreadsheet td div',
        'rule': '''
            line-height: 20px;
            max-height: 30px; min-height: 30px; height: 30px;
            display: block;
            overflow-y: hidden;
        '''
    }],
    tooltip_data=[
        {
            column: {'value': str(value), 'type': 'markdown'}
            for column, value in row.items()
        } for row in df.to_dict('rows')
    ],
    tooltip_duration=None,
    #editable=True, # if you wnt the user able to edit the table

        style_cell={
        #'width': '{}%'.format(len(df.columns)),
        #'textOverflow': 'ellipsis',
        #'overflow': 'hidden',
        'font-family': 'cursive',
        'font-size': '20px',
    }
    #style_as_list_view=True,
    ),
     dcc.Graph(id='BrewTable',
           figure=fig           
    )
     
 ])
 
 
#@app.callback(
#         Output('BrewTable-Out', 'figure')
#         [Input('BrewTable','data'),
#          Input('BrewTable','columns')])
 
def display_output(rows,columns):
     df=pd.DataFrame(rows,columns=[c['name'] for c in df.columns])
     return{
             'data':[{
                     'type':'parcoords',
                     'dimensions':[{
                             'label':col['name'],
                             'values':df[col['id']]
                             } for col in columns]
     }]
     }
                                                   
 
 
 
 
 
 
 
 
 
 
 