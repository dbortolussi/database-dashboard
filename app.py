from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
import numpy as np

app = Dash(__name__)


app.layout = html.Div([
    html.Div(className="panel-container",
        children=html.Div([
            html.Div([html.H1("Dashboard")]),
            html.Div(className="content", children=[
            html.Div(className="panel", style={'display':'flex', 'flex-direction':'column', 'gap':'10px','padding':'0'}, children=[
              html.Div([
              html.H2("Rank Universities by Keyword Relevance",style={'font-size':'1rem', 'margin':'0'}),
              dcc.Input(type="text", id='university-keyword', placeholder="Keyword"),
              html.Button("Submit", id='submit-university-keyword'),], style={'display':'flex', 'height':'5%', 'gap':'5px'}),
              dcc.Graph(id='university-keyword-graph',style={'width': '100%', 'height': '95%', 'border-style':'solid'})
            ]),
            html.Div(className="panel", style={'display':'flex', 'flex-direction':'column', 'gap':'10px','padding':'0'}, children=[
              html.Div([
              html.H2("Rank Faculty by Keyword Relevance",style={'font-size':'1rem', 'margin':'0'}),
              dcc.Input(type="text", id='faculty-keyword', placeholder="Keyword"),
              html.Button("Submit", id='submit-faculty-keyword'),], style={'display':'flex', 'height':'5%', 'gap':'5px'}),
              dash_table.DataTable(id='faculty-keyword-table', style_data={
                  'whiteSpace': 'normal',
                  'height': 'auto',
                  'lineHeight': '15px'}, style_cell={
                  'overflow': 'hidden',
                  'textOverflow': 'ellipsis',
                  'maxWidth': 0
              })
            ]),
            html.Div("Panel 3", className="panel"),
            html.Div("Panel 4", className="panel"),
            html.Div("Panel 5", className="panel"),
            html.Div("Panel 6", className="panel")]),
        ])
    )
])

@app.callback(Output('university-keyword-graph', 'figure'),
              Input('submit-university-keyword','n_clicks'),
              State('university-keyword', 'value'),
              )
def update_univ_graph(n, keyword):

  #Get data and put it in figure
  fig = px.scatter()

  return fig



@app.callback(Output('faculty-keyword-table', 'data'),
              Input('submit-faculty-keyword','n_clicks'),
              State('faculty-keyword', 'value'),
              )
def update_facu_table(n, keyword):


  #Get data and put it in dataframe

  dates = pd.date_range("20130101", periods=6)
  df =  pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

  return df.to_dict('records')




if __name__ == '__main__':
    app.run_server(debug=True)
