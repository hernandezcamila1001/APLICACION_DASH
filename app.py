import dash
import geopandas as gpd
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import folium

from backend.calculoInundacion import consultarDepartamento
from frontend.area1 import *
from frontend.area2 import *
from frontend.area3 import *



# Crea la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

@app.callback(
    Output('map-iframe', 'srcDoc'),
    Input('dropdown-departamentos', 'value')
)

def update_map(departamento_seleccionado):
    return mapa_departamento(departamento_seleccionado)


@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab"), Input("store", "data")],
)

def render_tab_content(active_tab, data):
    if active_tab is not None:
        if active_tab == "noticias":
            return html.P('Impacto de lluvias deja a más de 1.600.000 estudiantes sin cLase por daños en colegios (PIE DE CUESTA SANTANDER)'),
        # dbc.Col('NOTICIAS', md=4, style={'background-color':'#86BCFF','text-align': 'center'}),
        elif active_tab == "empresa":
            return dbc.Row(
                [
                    html.P(['''
                            Misión:
                            Nuestra misión es garantizar la seguridad de los colegios en Colombia a través de un 
                            seguimiento constante y alertas tempranas de inundaciones, proporcionando soluciones 
                            tecnológicas y servicios de prevención de alta calidad.

                            Visión:
                            Ser líderes en la protección de la comunidad escolar en Colombia, utilizando la 
                            tecnología más avanzada para prevenir inundaciones y brindar tranquilidad a las 
                            instituciones educativas y sus familias.

                            Objetivos:
                            Desarrollar sistemas de monitoreo avanzados para detectar inundaciones en tiempo real.
                            Establecer alianzas estratégicas con colegios y autoridades locales.
                            Capacitar a nuestros equipos en la gestión de riesgos y respuestas ante emergencias.
                            Ampliar nuestra cobertura en todo el territorio colombiano.
                            Promover la conciencia sobre la importancia de la seguridad escolar.
                            '''                            
                            ]),
                ]
            )
        elif active_tab == "conocenos":
            return dbc.Row(
                [
                    html.P(['''
                    Nombre de la Empresa: Alerta Escolar Colombia S.A.
                    Dirección de la Oficina Principal: Calle 123 #45-67, Bogotá, Colombia

                    Teléfono Principal: +57 301 234 5678

                    Correo Electrónico de Atención al Cliente: contacto@alertaescolarcolombia.com

                    Sitio Web: www.alertaescolarcolombia.com

                    Redes Sociales:
                    Facebook: facebook.com/AlertaEscolarCol
                    Twitter: twitter.com/AlertaEscolarCol
                    LinkedIn: linkedin.com/company/AlertaEscolarCol
                    Instagram: instagram.com/Alerta_EscolarCol
                    
                    Horario de Atención al Cliente:
                    Lunes a Viernes: 8:00 AM - 5:00 PM
                    Sábados: 9:00 AM - 1:00 PM
                    
                    Contacto de Emergencia 24/7:
                    Teléfono de Emergencia: +57 3 333 3333
                         '''])
                ])

    return "No tab selected"



# Define el layout de la aplicación

app.layout = dbc.Container(
    [
    dbc.Row([
        dbc.Col(area1, md = 12, style = {'background-color':'white'}), # md es el ancho de la casilla 
        dbc.Col(area2, md = 6, style = {'background-color':'white'}),
        dbc.Col(area3, md = 6, style = {'background-color':'white'})
    ])  
    ],
    fluid=True
)

@app.callback(
    Output("mapa", "figure"),
    Input("departamento_consultado", "value")
)

def update_map(departamento_consultado):
    return consultarDepartamento(departamento_consultado)

if __name__ == '__main__':
    app.run_server(debug=True)
