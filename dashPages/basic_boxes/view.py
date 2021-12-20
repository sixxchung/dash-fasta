import dash_admin_components as dac
import dash_bootstrap_components as dbc
from dash import dcc 
from dash import html 

#from pages.home.model import dataframe
from components.example_plots import plot_scatter

content = dac.TabItem(id='content_basic_boxes',                           
    children=html.Div(
        [
            dac.SimpleBox(
            	style = {'height': "600px"},
                title = "Box 1",
                children=[
                    dcc.Graph(
                        id='box-graph',
                        config=dict(displayModeBar=False),
                        style={'width': '38vw'}
                    )
                ]
            ),
            dac.SimpleBox(
            	style = {'height': "600px"},
                title = "Box 2",
                children=[
                    dcc.Graph(
                        figure=plot_scatter(),
                        config=dict(displayModeBar=False),
                        style={'width': '38vw'}
                    )
                ]
            )
        ], 
        className='row'
    )
)