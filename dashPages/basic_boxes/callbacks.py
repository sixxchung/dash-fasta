from app_dash import dash_app
from dash.dependencies      import Input, Output, State

from components.example_plots     import plot_scatter
# Update figure on slider change
@dash_app.callback(
    Output('box-graph', 'figure'),
    [Input('controlbar-slider', 'value')] )
def update_box_graph(value):
    return plot_scatter(value)
