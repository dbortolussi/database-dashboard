from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.Div(className="panel-container",
        children=html.Div([
            html.Div([html.H1("Dashboard")]),
            html.Div(className="content", children=[
            html.Div("Panel 1", className="panel"),
            html.Div("Panel 2", className="panel"),
            html.Div("Panel 3", className="panel"),
            html.Div("Panel 4", className="panel"),
            html.Div("Panel 5", className="panel"),
            html.Div("Panel 6", className="panel")]),
        ])
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
