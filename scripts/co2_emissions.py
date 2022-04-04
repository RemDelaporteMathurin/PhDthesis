import numpy as np

data = np.genfromtxt("annual-co2-emissions-per-country.csv", delimiter=",", names=True, dtype=None, encoding=None)

indexes = np.where(data["Entity"] == "World")

year_start = 1931

years = data["Year"][indexes]
co2_emissions_world = data["Annual_CO2_emissions"][indexes]

total_co2 = co2_emissions_world[np.where(years > year_start)].sum()  # in tonnes CO2

print(f"{total_co2:.2e} t CO2 since {year_start}")
