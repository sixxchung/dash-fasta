# dash-fasta
based rusnyder / fastapi-plotly-dash

# How to add a dash page 
> example> add menu stock plot
## 1. Make a new folder(stock) and files 
- dashPages/stock
- dashPages/stock/view.py
- dashPages/stock/model.py
- dashPages/stock/callbacks.py

## 2 Insert a view path to /ui/main.py
```
import dashPages.stock.view
body = dac.Body(
    dac.TabItems([
        #dashPages.home.view.content,
        dashPages.stock.view.content,
    ])
)
```

## 3. Make sidebar to /ui/sidebar.py

```
sideMenu = 	dac.SidebarMenu(
    [ ...   
        dac.SidebarHeader(children="etc."),
        dac.SidebarMenuItem(id='menu_stock', label='Stock plot',  icon='desktop'),
    ]
)
```
## 4. modify input, output callback /ui/sidebar_callbacks.py
```
...
MENU_ITEMS = ( "basic_cards", "social_cards", "tab_cards", 
               "basic_boxes", "value_boxes",
               "gallery_1", "gallery_2",
               "Stock")
def update_breadcrumbs( nClick1, nClick2, nClick3, nClick4, nClick5, nClick6, nClick7, nClick8,
    basic_cards, social_cards, tab_cards, basic_boxes, value_boxes, gallery_1, gallery_2, stock ): 
....

```

## 5 add callbacks path to /routes.py 
```
from dashPages.stock.callbacks import update_graph
```