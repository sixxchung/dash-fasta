from main import apps
from dash.dependencies      import Input, Output, State

from components.example_plots     import plot_scatter
# Update figure on slider change
@apps.callback(
    Output('box-graph', 'figure'),
    [Input('controlbar-slider', 'value')] )
def update_box_graph(value):
    return plot_scatter(value)
