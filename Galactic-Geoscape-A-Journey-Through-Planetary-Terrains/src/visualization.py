import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

def plot_terrain_matplotlib(terrain, title="Planetary Surface"):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    x = range(terrain.shape[0])
    y = range(terrain.shape[1])
    x, y = np.meshgrid(x, y)
    ax.plot_surface(x, y, terrain, cmap='terrain')
    plt.title(title)
    plt.show()

def plot_terrain_plotly(terrain, title="Interactive Planetary Surface"):
    fig = go.Figure(data=[go.Surface(z=terrain)])
    fig.update_layout(title=title)
    fig.show()
