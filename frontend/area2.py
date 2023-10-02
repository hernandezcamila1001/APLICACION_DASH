import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import geopandas as gpd
import folium

departamentos = gpd.read_file('data/Departamentos.zip') 
departamentos_ordenados = sorted([depto for depto in departamentos['DeNombre'].unique() if depto != "Area en Litigio Cauca - Huila" 
                                  and depto != 'San Andrés Providencia y Santa Catalina'])
opciones_dropdown = [{'label': depto, 'value': depto} for depto in departamentos_ordenados]


area2 = dbc.Container([
    dbc.Card([
    dbc.CardBody([
        html.H5("Registro de afectaciones"),
        html.Hr(),
        dbc.Button('BUSCAR',  className="ms-12",color="none",
                  style={"background": "linear-gradient(to right, #86BCFF, #F0FFFF)", 'text-align': 'center', 'width': '40%', 'outline':True}),

                ])
            ]),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(options=opciones_dropdown, value='Cundinamarca', id='departamento_consultado'),
            dcc.Graph(id="mapa",style={'width': '100%', "height": "600px"})
        ])
    ]),
    dbc.Row([
        dbc.Col([
            #html.Iframe(id='map-iframe', srcDoc='', width='100%', height='600')
        ])
    ])
],
    # Agrega la clase para alinear a la izquierda
    className="justify-content-start"
)


    ]),
    dbc.Row([
        dbc.Col([
            html.Iframe(id='map-iframe', srcDoc='', width='100%', height='600')
        ])
    ])
],
    # Agrega la clase para alinear a la izquierda
    className="justify-content-start"
)

