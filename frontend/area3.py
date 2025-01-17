import dash
from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc
import time

area3 = dbc.Container([
    dcc.Store(id="store"),
    dbc.Row([
        #
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
