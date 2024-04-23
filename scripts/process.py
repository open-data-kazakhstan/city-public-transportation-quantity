import openpyxl
import csv
from datapackage import Package

def data_package():
    package = Package()
    package.infer(r'data/public-transport-quantity-final.csv')
    package.commit()
    package.save(r"datapackage.json")

workbook = openpyxl.load_workbook('archive/public-transport-quantity.xlsx')
worksheet = workbook.active
desired_columns = [1, 34]
new_values = ["region","quantity","year"]
with open('archive/public-transport-quantity.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(new_values)
    for row in worksheet.iter_rows(min_row=7, max_row=27):
            values = [cell.value for cell in row if cell.column in desired_columns]
            if row[0].row > 6:
                values.append("2022")
            writer.writerow(values)

def rename_first_column_cells(input_file, output_file, new_names):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        # Modify the first cell of each row with new names
        for new_name, row in zip(new_names, reader):
            if row:  # Check if row is not empty
                row[0] = new_name
                writer.writerow(row)
input_file = 'archive/public-transport-quantity.csv'
output_file = 'data/public-transport-quantity-final.csv'
new_names = ["region", "Abai", "Akmolinskaya","Aktubinskaya","Almatinskaya","Atyrauskaya","West Kazakhstan","Zhambylskaya","Zhetisu","Karagandinskaya","Kostanaiskaya","Kyzylordinskaya","Mangistauskaya","Pavlodarskaya","North Kazakhstan","Turkestanskaya","Ulytau","East Kazakhstan","Astana city","Almaty city","Shimkent city"]
rename_first_column_cells(input_file, output_file, new_names)

data_package();