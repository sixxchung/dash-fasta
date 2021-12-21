from dash import html
from dash import dcc 
# https://docs-dash-admin-components.herokuapp.com/l/components
import dash_admin_components as dac

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ui.sidebar import sidebar
# Navbar
top_right_ui = dac.NavbarDropdown(
	badge_label = "!",
    badge_color= "danger",
    src = "https://quantee.ai",
	header_text="2 Items",
    children= [
		dac.NavbarDropdownItem(
			children = "message 1",
			date = "today"
		),
		dac.NavbarDropdownItem(
			children = "message 2",
			date = "yesterday"
		),
	]
)
navbar = dac.Navbar(id= "mybread",
                    color = "white", 
                    text = os.environ.get("WELCOME"), 
                    children = top_right_ui)

### Cards ----
import dashPages.basic_cards.view
import dashPages.social_cards.view
import dashPages.tab_cards.view
### Boxes ----
import dashPages.basic_boxes.view
import dashPages.value_boxes.view
### Gallery ----
import dashPages.gallery_1.view
import dashPages.gallery_2.view

import dashPages.stock.view
# Body
body = dac.Body(
    dac.TabItems([
        #dashPages.home.view.content,

        dashPages.basic_cards.view.content,
        dashPages.social_cards.view.content,
        dashPages.tab_cards.view.content,

        dashPages.basic_boxes.view.content,
        dashPages.value_boxes.view.content,

        dashPages.gallery_1.view.content,
        dashPages.gallery_2.view.content,

        dashPages.stock.view.content
    ])
)

# Controlbar
controlbar = dac.Controlbar(
    [
        html.Br(),
        html.P("Slide to change graph in Basic Boxes"),
        dcc.Slider(
            id='controlbar-slider',
            min=10,
            max=50,
            step=1,
            value=20
        )
    ],
    title = "My right sidebar",
    skin = "light"
)

# Footer
footer = dac.Footer(
	html.A("@DawidKopczyk, Quantee powered by sixx",
		href = "https://onesixx.com", 
		target = "_blank", 
	),
	right_text = "2019 fxxk"
)

# =============================================================================
# App Layout
# =============================================================================
layout = dac.Page([navbar, sidebar, body, controlbar, footer])
