import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import LogNorm
import os

# Load dataset
df = pd.read_csv('Solar_flare_RHESSI_2004_05.csv')

# Find the largest and smallest x.pos.asec and y.pos.asec values for radius
largest_x = df['x.pos.asec'].max()
smallest_x = df['x.pos.asec'].min()
largest_y = df['y.pos.asec'].max()
smallest_y = df['y.pos.asec'].min()

print("Largest x.pos.asec:", largest_x)
print("Smallest x.pos.asec:", smallest_x)
print("Largest y.pos.asec:", largest_y)
print("Smallest y.pos.asec:", smallest_y)

radius = 1000

def intensityMethod1(df_subset, title):
    weighted_values = df_subset['total.counts']
    intensity, xedges, yedges = np.histogram2d(
        df_subset['x.pos.asec'], df_subset['y.pos.asec'], bins=40, weights=weighted_values
    )
    print(intensity)
   
    extent = [-radius, radius, -radius, radius]
    graph, axis = plt.subplots(figsize=(10, 8))
    sc = axis.imshow(
        intensity.T, extent=extent, origin='lower', aspect='auto', cmap='YlOrRd', alpha=1, norm=LogNorm()
    )
    axis.set_title(title)
    axis.set_xlabel('X Position')
    axis.set_ylabel('Y Position')
    circle = plt.Circle((0, 0), radius, color='black', fill=False)
    axis.add_artist(circle)
    cbar = graph.colorbar(sc, ax=axis, label='Intensity')
    return graph, axis

# Create a directory to save the PNG files
output_dir = 'intensity_graphs_method1'
os.makedirs(output_dir, exist_ok=True)

# Months 1+2+3+4
df_1to4 = df[(df['year'] == 2004) & (df['month'].between(1, 4))]
graph1, axis1 = intensityMethod1(df_1to4, 'Solar Flare Intensity Graph Months 1+2+3+4 - Total.Counts')

# Save the first plot as a PNG file
output_filename1 = os.path.join(output_dir, 'intensity_graph_method1_months_1to4.png')
graph1.savefig(output_filename1, bbox_inches='tight')

# Months 21+22+23+24
df_21to24 = df[(df['year'] == 2005) & (df['month'].between(9, 12))]
graph2, axis2 = intensityMethod1(df_21to24, 'Solar Flare Intensity Graph Months 21+22+23+24 - Total.Counts')

# Save the second plot as a PNG file
output_filename2 = os.path.join(output_dir, 'intensity_graph_method1_months_21to24.png')
graph2.savefig(output_filename2, bbox_inches='tight')

plt.show()



