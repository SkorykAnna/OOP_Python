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

df["temps_parcours"] = df["temps_parcours"].str.rstrip(" min").astype(int)


#Partie 5

    #ex5.1
    # Specify the file path
file_path = './caracteristiques-2018.csv'

    # Read the CSV file
df_ch = pd.read_csv(file_path, encoding='latin-1')
print(df_ch.columns)

    #ex5.2
    #Filter the DataFrame to include only the accidents that occurred in Lyon (department (dep) code 690) 
accidents_lyon = df_ch[df_ch['dep'] == 690]
    #count
num_accidents_lyon = accidents_lyon.shape[0]
print("Number of accidents in Lyon: ", num_accidents_lyon)

    #ex5.3
    # Adding additional table
file_path = './vehicules-2018.csv'
df_vehicules = pd.read_csv(file_path, encoding='utf-8')

    # Counting accidents involving bicycles (vehicle category (catv) is 1)
accidents_velo = df_vehicules[df_vehicules['catv'] == 1]
total_accidents_velo = accidents_velo.shape[0]
print("Number of accidents with bicycles:", total_accidents_velo)

    #ex5.4
    # Joining the two tables based on a common column
merged_df = accidents_lyon.join(accidents_velo.set_index('Num_Acc'), on='Num_Acc', lsuffix='_lyon', rsuffix='_velo')

    # Counting the number of accidents involving a bicycle in Lyon
total_accidents_lyon_velo = merged_df.shape[0]
print("Number of bicycle accidents in Lyon:", total_accidents_lyon_velo)

    #ex5.5
    # Join the two tables based on a common column
merged_df = df_ch.join(accidents_velo.set_index('Num_Acc'), on='Num_Acc', lsuffix='_cities')

    # Filter accidents for Lyon (690), Paris (750), and Nantes (440)
lyon_accidents = df_ch[df_ch['dep'] == 690]
paris_accidents = df_ch[df_ch['dep'] == 750]
nantes_accidents = df_ch[df_ch['dep'] == 440]

    # Get the number of bicycle accidents in each city
lyon_count = lyon_accidents.shape[0]
paris_count = paris_accidents.shape[0]
nantes_count = nantes_accidents.shape[0]

    # Create a DataFrame to hold the data
data = {
    'City': ['Lyon', 'Paris', 'Nantes'],
    'Bicycle Accidents': [lyon_count, paris_count, nantes_count],
}
df_city_accidents = pd.DataFrame(data)

    # Plot the histogram
plt.bar(df_city_accidents['City'], df_city_accidents['Bicycle Accidents'])
plt.xlabel('City')
plt.ylabel('Number of Bicycle Accidents')
plt.title('Comparison of Bicycle Accidents in Major Cities')

    # Add value labels
for i, value in enumerate(df_city_accidents['Bicycle Accidents']):
    plt.text(i, value, str(value), ha='center', va='bottom')

plt.show()