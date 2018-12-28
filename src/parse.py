import csv

MY_FILE = "../data/sample_sfpd_incident_all.csv"


def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""

    parsed_data = []

    # Abrir archivo CSV
    opened_file = open(raw_file)

    # Leer archivo CSV
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Omita la primera línea del archivo para los encabezados.
    fields = next(csv_data)

    # Iterar sobre cada fila del archivo csv, comprimir juntos campo -> valor
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Cerrar archivo CSV
    opened_file.close()

    return parsed_data


def main():
    # Call our parse function and give it the needed parameters
    new_data = parse(MY_FILE, ",")

    print(new_data)


if __name__ == "__main__":
    main()
