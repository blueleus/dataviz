import matplotlib.pyplot as plt
import numpy as np

from collections import Counter

from parse import parse, MY_FILE


def visualize_days():
    """Visualizar datos por día de la semana."""

    # tomar nuestros datos analizados que analizamos antes
    data_file = parse(MY_FILE, ",")

    # crea una nueva variable, 'counter', para iterar a través de cada
    # línea de datos en los datos analizados, y cuente cuántos incidentes
    # sucedieron en cada uno los día de la semana.
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # separar los datos del eje x (los días de la semana) de la
    # variable 'counter' de los datos del eje y (el número de
    # incidentes por cada día)
    data_list = [
        counter["Monday"],
        counter["Tuesday"],
        counter["Wednesday"],
        counter["Thursday"],
        counter["Friday"],
        counter["Saturday"],
        counter["Sunday"]
    ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # Asignar los datos a un plot.
    plt.plot(data_list)

    # Asigna etiquetas a el plot a partir de day_list
    plt.xticks(range(len(day_tuple)), day_tuple)

    # guarda el plot!
    plt.savefig("Days.png")

    # cierra la figura
    plt.clf()


def visualize_type():
    """Visualice los datos por categoría en un gráfico de barras."""

    # tomar nuestros datos analizados
    data_file = parse(MY_FILE, ",")

    # crea una nueva variable, 'counter', para iterar a través de cada línea
    # de datos en los datos analizados, y cuenta cuántos incidentes ocurren
    # por categoria
    counter = Counter(item["Category"] for item in data_file)

    # Establecer las etiquetas que se basan en las 'keys' de nuestro 'counter'.
    # Dado que el orden no importa, solo podemos usar counter.keys()
    labels = tuple(counter.keys())

    # Establecer exactamente donde las etiquetas se deben fijar en el eje x.
    xlocations = np.arange(len(labels)) + 0.5

    # Ancho de cada barra
    width = 0.5

    # Asignar datos a un gráfico de barras
    plt.bar(xlocations, counter.values(), width=width)

    # Asigna etiquetas y marca la ubicación a x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # Dé un poco más de espacio para que las etiquetas del eje x no se corten en el
    # grafico
    plt.subplots_adjust(bottom=0.4)

    # Hacer el gráfico/figura general más grande
    plt.rcParams["figure.figsize"] = 12, 8

    # ¡Guarda la gráfica!
    plt.savefig("Type.png")

    # Cerrar la figura
    plt.clf()


def main():
    visualize_days()
    visualize_type()


if __name__ == "__main__":
    main()
