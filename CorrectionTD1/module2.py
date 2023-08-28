import json
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

#Partie 2

    #ex2.1
import pandas as pd

    # Create a DataFrame from the variable 'rando' using the from_dict function
df = pd.DataFrame.from_dict(rando)

    # Check the dimensions of the DataFrame
dimensions = df.shape
print("Dimensions of the DataFrame:", dimensions)
print()

    #ex2.2
    # View the beginning of the DataFrame
print("Beginning of the DataFrame:")
print(df.head())
print()

    # View the end of the DataFrame
print("End of the DataFrame:")
print(df.tail())
print()

    #ex2.3
    # Example of using iloc
subset = df.iloc[:, 1:4]
print("Subset using iloc:")
print(subset)
print()

    # Print the column names
print(df.columns)
print()

    # Example of using loc to change a value in a column
df.loc[df['nom'] == 'test', 'nom'] = 0
print("Updated DataFrame:")
print(df)
print()

    #ex2.4
difficulte_counts = df["difficulte"].value_counts()
print("difficulte_counts:")
print(difficulte_counts)
print()

    #ex2.5
print("temps_parcours:")
print(df["temps_parcours"])
print()

    #ex2.6
df["temps_parcours"] = df["temps_parcours"].str.rstrip(" min").astype(int)
print("temps_parcours without min:")
print(df["temps_parcours"])
print()

    #ex2.7
average_temps_parcours = df["temps_parcours"].mean()
print("average_temps_parcours:")
print(average_temps_parcours)
print()

    # Clean the values in the "longueur" column and replace the comma with a dot
df["longueur"] = df["longueur"].str.rstrip(" km").str.replace(",", ".")

    # Convert the values to float
df["longueur"] = df["longueur"].astype(float)
    
    # Compute the mean of the "longueur" column grouped by "vocation"
grouped_data = df.groupby("vocation")["longueur"].mean()
print("Compute the mean of the 'longueur' column grouped by 'vocation':")
print(grouped_data)
print()

    #ex2.8
    # Group the data by difficulty level and compute the mean travel time
grouped_data = df.groupby("difficulte")["temps_parcours"].mean()

    # Print the average travel time for each difficulty level
print("Compute the mean of the 'longueur' column grouped by 'vocation':")
print(grouped_data)
print()
