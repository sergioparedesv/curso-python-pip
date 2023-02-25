from readcsv import read_csv_file
from proces import count_classes
from graf import plot_pie_chart

if __name__ == '__main__':
    # Código que se ejecutará solo si el archivo se está ejecutando como un programa principal
    data = read_csv_file('csv/data.csv')
    class_counts = count_classes(data)
    plot = plot_pie_chart(class_counts)