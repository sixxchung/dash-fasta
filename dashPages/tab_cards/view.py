import dash_admin_components as dac

import dash_bootstrap_components as dbc
from dash import dcc 
from dash import html 

#from pages.tab_cards.model import dataframe
         
content = dac.TabItem(id='content_tab_cards', 
    children=[
        html.Div([
            dac.TabBox(
                [
                    dac.TabBoxHeader(
                        dac.TabBoxMenu([
                            dac.TabBoxMenuItem(tab_id='tab_box_1_tab1', label='Tab 01'),
                            dac.TabBoxMenuItem(tab_id='tab_box_1_tab2', label='Tab 02'),
                            dac.TabBoxMenuItem(tab_id='tab_box_1_tab3', label='Tab 03') 
                        ], id='tab_box_1_menu'),
                        collapsible = False,
                        closable = True,
                        title="A card with tabs"
                    ),
                    dac.TabBoxBody(id='tab_box_1')		
                ],
                width=6,
                elevation=2
            ),      
            dac.TabBox(
                [
                    dac.TabBoxHeader(
                        dac.TabBoxMenu(
                        children=[
                            dac.TabBoxMenuItem(tab_id='tab_box_2_tab1', label='Tab 11', color='dark'),
                            dac.TabBoxMenuItem(tab_id='tab_box_2_tab2', label='Tab 22', color='danger'),
                            dac.TabBoxMenuItem(tab_id='tab_box_2_tab3', label='Tab 33', color='primary') 
                        ], id='tab_box_2_menu'),
                        closable=True,
                        title="A card with colorful tabs"
                    ),
                    dac.TabBoxBody(
                        id='tab_box_2'
                    )		
                ],
                color='warning',
                width=6,
                elevation=2
            )
        ], className='row')
    ]
)
