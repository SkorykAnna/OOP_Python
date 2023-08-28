import json
import matplotlib.pyplot as plt
import numpy as np

#Partie 1

    #ex1.1
    # Specify the path to the JSON file
json_file_path = r"./evg_esp_veg.json"

    # Open the JSON file in read mode
with open(json_file_path, "r") as file:
    # Load the JSON data
    d_json = json.load(file)

    #ex1.2        
    # Check the type of the variable
print("Type of the variable: ")
print(type(d_json))  # <class 'dict'>
print()

    # Access the fields of the dataset
fields = d_json['fields']
print("The fields of the dataset: ")
print(fields)
print()

    # Access the list of hikes
hikes = d_json['values']
print("The list of hikese: ")
print(hikes)
print()

    #ex1.3
    # Save the list of fields in a variable 'var'
var = d_json['fields']

    # Save the list of hikes in a variable 'rando'
rando = d_json['values']

    # Check the number of records
record_count = len(rando)
print("Number of records:", record_count)
print()
    # Access the values
values_of_first_record = rando[0]
print("Values of the first record:", values_of_first_record)
print()
    #ex1.4
print()
    # Determine the size of the dataset (number of rows)
row_count = len(rando)
print("Size of the dataset (number of rows):", row_count)
print()
    # Access the dictionary at index 9
record_10 = rando[9]
print("Record at index 9 (row 10):", record_10)

