import pandas as pd

def load_planetary_data(file_path='data/planetary_data.csv'):
    data = pd.read_csv(file_path)
    return data

def display_planet_info(planet_name):
    data = load_planetary_data()
    planet_info = data[data['Planet'] == planet_name].to_dict('records')[0]
    print(f"Planet: {planet_info['Planet']}")
    print(f"Composition: {planet_info['Composition']}")
    print(f"Average Temperature: {planet_info['AverageTemperature (°C)']}°C")
    print(f"Gravity: {planet_info['Gravity (m/s²)']} m/s²")
    print(f"Atmosphere: {planet_info['Atmosphere']}")
