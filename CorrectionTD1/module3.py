import json
import matplotlib.pyplot as plt
import pandas as pd

    # Specify the path to the JSON file
json_file_path = r"./evg_esp_veg.json"

    # Open the JSON file in read mode
with open(json_file_path, "r") as file:
    # Load the JSON data
    d_json = json.load(file)


    # Access the fields of the dataset
fields = d_json['fields']


    # Access the list of hikes
hikes = d_json['values']

    # Save the list of fields in a variable 'var'
var = d_json['fields']

    # Save the list of hikes in a variable 'rando'
rando = d_json['values']

    # Create a DataFrame from the variable 'rando' using the from_dict function
df = pd.DataFrame.from_dict(rando)

#Partie 3

    #ex3.1

    # Group the data by difficulty level and count the number of hikes in each group
grouped_data = df.groupby("difficulte").size()

    # Plot the bar chart
grouped_data.plot.bar()

    # Set the chart title and axis labels
plt.title("Distribution of Hikes by Difficulty Level")
plt.xlabel("Difficulty Level")
plt.ylabel("Number of Hikes")

    # Display the chart
plt.show()
print()


    #ex3.2
    # Sort the series by index in alphabetical order
grouped_data = grouped_data.sort_index()

    # Plot the bar chart
grouped_data.plot.bar()

    # Set the chart title and axis labels
plt.title("Distribution of Hikes by Difficulty Level")
plt.ylabel("Number of Hikes")

    # Display the chart
plt.show()

    #ex 3.3
    # Plot the pie chart
grouped_data.plot.pie()

    # Set the chart title
plt.title("Distribution of Hikes by Difficulty Level")
print()

    # Display the chart
plt.show()
