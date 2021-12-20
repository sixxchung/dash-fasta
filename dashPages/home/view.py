import dash_bootstrap_components as dbc
from dash import dcc 
from dash import html 
import dash_admin_components as dac

#from pages.home.model import dataframe

content = dac.TabItem(
    [
        html.P(
            'home sweet home'
        )
    ],
    id='content_home',
)
