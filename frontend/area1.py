import dash
from dash import html
import dash_bootstrap_components as dbc

area1 = dbc.Card([
        dbc.CardHeader(
            html.Strong("COLEGIOS Y CRECIDAS", style={"font-size": "26px"}),
            style={"background": "linear-gradient(to right, #1E90FF, #F0FFFF)"},
        ),
        dbc.CardBody(
                html.H5("ALERTAS DE INUNDACIONES EN ZONAS EDUCATIVAS"),
                style={"font-size": "20px", "background-color":"#FFFAFA"}
            ),
])
