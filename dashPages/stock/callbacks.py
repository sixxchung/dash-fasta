#from dashapp import app
#from mainApp import apps
from dashApp import apps


from dash.dependencies      import Input, Output, State

from dashPages.stock.model  import df

@apps.callback(Output('my-graph', 'figure'),
                [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    dff = df[df['Stock'] == selected_dropdown_value]
    return {'data': [{'x': dff.Date, 'y': dff.Close,  'line': {'width': 3, 'shape': 'spline'}  }],
            'layout': { 'margin': {'l':30, 'r':20, 'b':30, 't':20} } }
