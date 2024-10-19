from terrain_generator import generate_perlin_noise_terrain
from visualization import plot_terrain_matplotlib, plot_terrain_plotly
from planetary_info import display_planet_info

def main():
    project_name = "Galactic Geoscape: A Journey Through Planetary Terrains"
    print(f"Welcome to {project_name}!\n")
    
    selected_planet = "Mars"
    display_planet_info(selected_planet)
    
    size = 200
    scale = 0.1
    terrain = generate_perlin_noise_terrain(size, scale)
    
    plot_terrain_matplotlib(terrain, title=f'{selected_planet} Surface Visualization - {project_name}')
    plot_terrain_plotly(terrain, title=f'Interactive {selected_planet} Terrain Visualization - {project_name}')

if __name__ == "__main__":
    main()
