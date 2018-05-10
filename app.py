import os
import backend
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


app = dash.Dash(__name__)
server = app.server


app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})

app.layout = html.Div([
    dcc.Input(id='my-id', value='Malaysia', type='text'),
    html.Div(id='output-graph')
])


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_data):
    x = backend.location_comparison(10, str(input_data), 'Food')
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': x.index, 'y': x[input_data], 'type': 'bar', 'name': str(input_data)},
            ],
            'layout': {
                'title': 'Locations tags for' + ' ' + str(input_data)
            }
        }
    )


if __name__ == '__main__':
    app.run_server(debug=True)