import geopandas as gpd
import folium


# Lee el archivo
departamentos = gpd.read_file(r"D:\backup\Documents\U Distrital\INGENIERIA CIVIL\2023-3\PROGRAMACION 2\Actividad Sep 20\data\Departamentos.zip")

m = folium.Map(location=[4.5, -74.5], zoom_start=6)

# Añadir los departamentos al mapa
folium.GeoJson(departamentos).add_to(m)

# Guarda el mapa en un archivo HTML
m.save('mapa.html')



departamentos_ordenados = sorted(departamentos['DeNombre'].unique())
opciones_dropdown = [{'label': depto, 'value': depto} for depto in departamentos_ordenados]


def display_departamento(departamento_seleccionado):
    m = folium.Map(location=[4.60, -74.08], zoom_start=6)
    
    departamento_lista = departamentos_ordenados

    if departamento_seleccionado in departamento_lista:
        departamento_mapa = departamentos[departamentos['DeNombre'] == departamento_seleccionado]
        folium.GeoJson(departamento_mapa).add_to(m)

    m.save('temp_map.html')
    return open('temp_map.html', 'r').read()

mapa_departamento = display_departamento



