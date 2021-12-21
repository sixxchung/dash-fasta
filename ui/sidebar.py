import dash_bootstrap_components as dbc
from dash import dcc, html 
import dash_admin_components as dac

# Sidebar
subitems = [
    dac.SidebarMenuSubItem(id='menu_gallery_1', label='Gallery 1', icon='arrow-circle-right', 
        badge_label='Soon',
        badge_color='success'
    ), 
    dac.SidebarMenuSubItem(id='menu_gallery_2', label='Gallery 2', icon='arrow-circle-right', 
        badge_label='Soon', 
        badge_color='success'
    )
]
sideMenu = 	dac.SidebarMenu(
    [
        dac.SidebarHeader(children="Cards"),
        dac.SidebarMenuItem(id='menu_basic_cards',  label='Basic cards',  icon='box'),
        dac.SidebarMenuItem(id='menu_social_cards', label='Social cards', icon='id-card'),
        dac.SidebarMenuItem(id='menu_tab_cards',    label='Tab cards',    icon='image'),

        dac.SidebarHeader(children="Boxes"),
        dac.SidebarMenuItem(id='menu_basic_boxes', label='Basic boxes',      icon='desktop'),
        dac.SidebarMenuItem(id='menu_value_boxes', label='Value/Info boxes', icon='suitcase'),

        dac.SidebarHeader(children="Gallery"),
        dac.SidebarMenuItem(label='Galleries', icon='cubes', 
            children=subitems),
        
        dac.SidebarHeader(children="etc."),
        dac.SidebarMenuItem(id='menu_stock', label='Stock plot',  icon='desktop'),
    ]
)
sidebar = dac.Sidebar(
    sideMenu,
    title='Alyx Admin',
	skin="dark",
    color="primary",
	brand_color="primary",
    url="https://onesixx.com",
    #src="https://adminlte.io/themes/AdminLTE/dist/img/user2-160x160.jpg",
    src="assets/user-01.jpg",
    elevation=3,
    opacity=0.8
)
