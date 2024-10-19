import numpy as np
from noise import pnoise2

def generate_perlin_noise_terrain(size, scale):
    """Generates a Perlin noise-based terrain."""
    terrain = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            terrain[i][j] = pnoise2(i * scale, j * scale, octaves=6, persistence=0.5, lacunarity=2.0)
    return terrain
