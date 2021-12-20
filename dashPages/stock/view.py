import dash_bootstrap_components as dbc
from dash import dcc 
from dash import html 
import dash_admin_components as dac

#from pages.home.model import dataframe


content = dac.TabItem(
    [
        html.H1('Stock Tickers'),
        dcc.Dropdown(
            id='my-dropdown',
            options=[
                {'label': 'Tesla', 'value': 'TSLA'},
                {'label': 'Apple', 'value': 'AAPL'},
                {'label': 'Coke', 'value': 'COKE'}
            ],
            value='TSLA'
        ),
        dcc.Graph(id='my-graph')
    ],
    id='content_stock',
)