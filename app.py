import dash
from dash import html
import dash_bootstrap_components as dbc

#importamos el frontend
from frontend.main import layout

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = layout

if __name__ =='__main__':
    app.run_server(debug=True)


