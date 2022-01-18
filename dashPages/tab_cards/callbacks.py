from appdash import dash_app
from dash.dependencies      import Input, Output, State
from dashPages.tab_cards.model  import text_1, text_2, text_3

@dash_app.callback(
    Output('tab_box_1', 'children'),
    [ Input('tab_box_1_menu', 'active_tab')] )
def display_tabbox1(active_tab):
    if active_tab == 'tab_box_1_tab1':
        return text_1
    elif active_tab == 'tab_box_1_tab2':
        return text_2
    elif active_tab == 'tab_box_1_tab3':
        return text_3

@dash_app.callback(
    Output('tab_box_2', 'children'),
    [Input('tab_box_2_menu', 'active_tab')] )
def display_tabbox2(active_tab):
    if active_tab == 'tab_box_2_tab1':
        return text_1
    elif active_tab == 'tab_box_2_tab2':
        return text_2
    elif active_tab == 'tab_box_2_tab3':
        return text_3
    