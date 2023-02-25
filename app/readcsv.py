import csv


def read_csv_file(file_path):
  with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    data = {}
    for row in csv_reader:
      for column, value in row.items():
        if column not in data:
          data[column] = []
        data[column].append(value)
  return data


data = read_csv_file('csv/data.csv')
print(data)
