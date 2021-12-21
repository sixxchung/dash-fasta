import dash_bootstrap_components as dbc
from dash import dcc, html 
import dash_admin_components as dac

from dashPages.gallery_2.model import dataframe

content = dac.TabItem(
    [
        html.H1("GDP viewer"),
        html.Hr(),
        dcc.Graph(id='graph-with-slider'),
        dcc.Slider(
            id='year-slider',
            min=dataframe()['year'].min(),
            max=dataframe()['year'].max(),
            value=dataframe()['year'].min(),
            marks={str(year): str(year) for year in dataframe()['year'].unique()},
            step=None
        )
    ],
    id='content_gallery_2',
)
