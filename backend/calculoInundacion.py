import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
import hashlib 

# Importamos los archivos de datos
departamentos = gpd.read_file('data/Departamentos.zip') 
departamentos_ordenados = sorted([depto for depto in departamentos['DeNombre'].unique() if depto != "Area en Litigio Cauca - Huila" 
                                  and depto != 'San Andrés Providencia y Santa Catalina'])
opciones_dropdown = [{'label': depto, 'value': depto} for depto in departamentos_ordenados]

rios = gpd.read_file('data/DrenajeDoble.zip')

colegios = gpd.read_file('data/EstablecimientosEducativos.zip')

def color_por_departamento(departamento):
    hash_object = hashlib.md5(departamento.encode())
    hex_dig = hash_object.hexdigest()
    color = '#' + hex_dig[:6]
    return color

def consultarDepartamento(departamento_consultado):
    # Consulta del departamento buscado
    departamento_buscado = departamentos.query(f"DeNombre == '{departamento_consultado}'")
    rios_departamento_buscado = gpd.overlay(departamento_buscado , rios, how='intersection')
    colegios_departamento_buscado = colegios.query(f"DeNombre == '{departamento_consultado.upper()}'")

    # Buffer de los ríos
    rios_departamento_buscado["buffer"] = rios_departamento_buscado.buffer(500)

    # Otra intersección
    colegios_afectados = gpd.overlay(
        colegios_departamento_buscado,
        rios_departamento_buscado.set_geometry("buffer"),
        how='intersection')

    # Convertir a EPSG 4326
    rios_departamento_buscado_4326 = rios_departamento_buscado.to_crs(epsg=4326)
    rios_departamento_buscado_4326['buffer'] = rios_departamento_buscado_4326['buffer'].to_crs(epsg=4326)
    colegios_afectados_4326 = colegios_afectados.to_crs(epsg=4326)


    # Genera mapa de ríos
    fig = px.choropleth_mapbox(
        geojson=rios_departamento_buscado_4326['buffer'].geometry,
        locations=rios_departamento_buscado_4326.index
    )

    # Agregar colegios al mapa
    fig.add_trace(
        go.Scattermapbox(
            lat=colegios_afectados_4326.geometry.y,
            lon=colegios_afectados_4326.geometry.x,
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=10,  # Hacemos que estos puntos sean ligeramente más grandes
                color='black'  # Color negro para representar el borde
            ),
            text=colegios_afectados_4326['Nombre'],
            hoverinfo='text'
        )
    )

    # Dibuja los puntos centrales (más pequeños y en el color deseado)
    fig.add_trace(
        go.Scattermapbox(
            lat=colegios_afectados_4326.geometry.y,
            lon=colegios_afectados_4326.geometry.x,
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=8,  # Estos puntos son más pequeños, formando el "relleno" del marcador
                color=color_por_departamento(departamento_consultado)
            ),
            text=colegios_afectados_4326['Nombre'],
            hoverinfo='text'
        )
    )

    

    # Configuraciones del mapa
    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox_zoom=5,
        mapbox_center={"lat": 4.6, "lon": -74},
    )

    return fig

