import dash_admin_components as dac
import dash_bootstrap_components as dbc
from dash import dcc 
from dash import html 

#from pages.home.model import dataframe

content = dac.TabItem(id='content_social_cards', 
    children=html.Div(
        [
            dac.UserCard(
              src = "https://adminlte.io/themes/AdminLTE/dist/img/user1-128x128.jpg",
              color = "info",
              title = "User card type 1",
              subtitle = "a subtitle here",
              elevation = 4,
              children="Any content here"
            ),
            dac.UserCard(
              type = 2,
              src = "https://adminlte.io/themes/AdminLTE/dist/img/user7-128x128.jpg",
              color = "success",
              image_elevation = 4,
              title = "User card type 2",
              subtitle = "a subtitle here",
              children="Any content here"
            )
        ], 
        className='row'
    )
)