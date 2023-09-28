import dash
from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc
import time

area3 = dbc.Container([
    dcc.Store(id="store"),
    # html.H3('Registro de afectaciones'), # Formato de Texto
    # html.Hr(),              # Agrega una linea abajo del titulo
    dbc.Row([
        #dbc.Col('NOTICIAS', md=4, style={'background-color':'#1E90FF','text-align': 'center'}), # md= ancho del bloque, style= para qye se vea el color
        #dbc.Col('EMPRESA', md=4, style={'background-color':'#86BCFF','text-align': 'center'}),
        #dbc.Col('CONOCENOS', md=4, style={'background-color':'#B3D3FF','text-align': 'center'}),
        #html.Br(), 
        #dbc.Col('.', md=12, style={'background-color':'white','text-align': 'center', 'text-color':'white'}),
        # dbc.Button('BUSCAR',  className="ms-12",color="none",
        #         style={"background": "linear-gradient(to right, #86BCFF, #F0FFFF)", 'text-align': 'center', 'width': '40%', 'outline':True}),
        dbc.Tabs(
            [
                dbc.Tab(label="NOTICIAS", tab_id="noticias"),
                dbc.Tab(label="EMPRESA", tab_id="empresa"),
                dbc.Tab(label="CONOCENOS", tab_id="conocenos"),
            ],
            id="tabs",
            active_tab="noticias",
        ),
        html.Div(id="tab-content", className="p-4"),
    ])
])
