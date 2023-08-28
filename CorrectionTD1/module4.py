import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

#Partie 4

    #ex4.1
df["longueur"] = df["longueur"].astype(str).str.replace(",", ".").str.rstrip(" km").astype(float)
print("Longueur :")
print(df["longueur"])
print()

    #ex4.2
    # Was chosen nom_var_1 = longueur; nom_var_2 = temps_parcours
df.plot.scatter(x="longueur", y="temps_parcours")
plt.show()

    #ex4.3
    # Renaming of chosen var's
ax = df.plot.scatter(x="longueur", y="temps_parcours")
ax.set_title("Relation entre longueur et temps de parcours")
ax.set_xlabel("Longueur (km)")
ax.set_ylabel("Temps de parcours (minutes)")
plt.show()

    #ex4.4
    # Renaming of chosen var's
ax = df.plot.scatter(x="longueur", y="temps_parcours", label="Données", color="blue", marker="o")
ax.set_title("Relation entre longueur et temps de parcours")
ax.set_xlabel("Longueur (km)")
ax.set_ylabel("Temps de parcours (minutes)")
plt.show()

    # Calculate correlation coefficient
correlation = df["longueur"].corr(df["temps_parcours"])
print("Coefficient de corrélation (R):", correlation)

    #Adding correlation to plot
ax.annotate(f"Corrélation (R) : {correlation:.2f}", xy=(0.5, 0.9), xycoords="axes fraction", color="coral")
plt.show()

    #Adding correlation line to plot
x = np.array([df["longueur"].min(), df["longueur"].max()])
y = correlation * np.array([df["temps_parcours"].min(), df["temps_parcours"].max()])

    # Create scatter plot
ax = df.plot.scatter(x="longueur", y="temps_parcours", label="Données", color="blue", marker="o")
ax.set_title("Relation entre longueur et temps de parcours")
ax.set_xlabel("Longueur (km)")
ax.set_ylabel("Temps de parcours (minutes)")

    # Add correlation annotation to plot
ax.annotate(f"Corrélation (R): {correlation:.2f}", xy=(0.5, 0.9), xycoords="axes fraction", color="coral")

    # Add correlation line to plot
ax.plot(x, y, linestyle="--", color="coral", label="Corrélation")

plt.legend()
plt.show()
