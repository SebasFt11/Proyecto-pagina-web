import dash
from dash import html
import dash_bootstrap_components as dbc

from .navegador.navegador import navegador
from .derecho.derecho import derecho
from .izquierdo.izquierdo import izquierdo


layout = dbc.Container([
    html.H1('Clasificación de Suelos',style = {'background-color' : '#188EBE', 'color' : 'white'}),
    dbc.Row([
        dbc.Col(navegador, md=12, style = {'background-color' : '#188EBE'}),
        dbc.Col(izquierdo, md=4, style = {'background-color' : '#D8DFFB'}),
        dbc.Col(derecho, md=8, style = {'background-color' : '#D8FBF9'}),
    ])
])
