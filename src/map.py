import geojson

import parse as p


def create_map(data_file):
    """Crea un archivo GeoJSON.


    Devuelve un archivo GeoJSON que se puede representar en un
    GitHub Gist en gist.github.com. Simplemente copie el archivo
    de salida y péguelo en un Gist nuevo, luego cree un gist
    público o privado. GitHub renderizará automáticamente
    el archivo GeoJSON como un mapa."""

    # Define el tipo de GeoJSON que estamos creando
    geo_map = {"type": "FeatureCollection"}

    # Define la lista vacía para recopilar cada punto en el gráfico
    item_list = []

    # Iterate sobre nuestros datos para crear el documento GeoJSON.
    # Estamos usando enumerate(), así que obtenemos la línea, también
    # el índice, que es el número de línea.
    for index, line in enumerate(data_file):

        # Omita cualquier coordenada cero ya que esto eliminará
        # nuestro mapa.
        if line['X'] == "0" or line['Y'] == "0":
            continue

        # Configurar un nuevo diccionario para cada iteración.
        data = {}

        # Asignar elementos de línea a los campos GeoJSON apropiados.
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {'title': line['Category'],
                              'description': line['Descript'],
                              'date': line['Date']}
        data['geometry'] = {'type': 'Point',
                            'coordinates': (line['X'], line['Y'])}

        # Agregar diccionario de datos a nuestra item_list
        item_list.append(data)

    # Para cada punto en nuestra item_list, agregamos el punto a nuestro
    # diccionario. setdefault crea una clave llamada 'features' que
    # tiene como valor una lista vacía. Con cada iteración,
    # estamos agregando nuestro punto a esa lista.
    for point in item_list:
        geo_map.setdefault('features', []).append(point)

    # Ahora que todos los datos se analizan en GeoJSON, escriba en un archivo para que
    # podamos subirlo a gist.github.com
    with open('file_sf.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))


def main():
    data = p.parse(p.MY_FILE, ",")

    return create_map(data)


if __name__ == "__main__":
    main()