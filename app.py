from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div("Dashboard", className="panel-container", children=[
  html.Div("Panel 1", className="panel"),
  html.Div("Panel 2", className="panel"),
  html.Div("Panel 3", className="panel"),
  html.Div("Panel 4", className="panel"),
  html.Div("Panel 5", className="panel"),
  html.Div("Panel 6", className="panel"),
]  
)

if __name__ == '__main__':
    app.run_server(debug=True)
