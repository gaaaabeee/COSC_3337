import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import BoundaryNorm, ListedColormap

# Load dataset
df = pd.read_csv('Solar_flare_RHESSI_2004_05.csv')

# Filter data for months 1+2+3+4
m_1to4 = ((df['year'] == 2004) & (df['month'].between(1, 4)))
df_1to4 = df[m_1to4]

# Filter data for months 21+22+23+24
m_21to24 = ((df['year'] == 2005) & (df['month'].between(9, 12)))
df_21to24 = df[m_21to24]

# Define the energy ranges based on energy.kev values
energy_kev_ranges = [(6, 12), (12, 25), (25, 50), (50, 100), (100, 300), (300, 800)]

# Create a custom colormap and norm
# cmap = ListedColormap(['blue', 'magenta', 'cyan', 'purple', 'teal', 'black'])
cmap = plt.get_cmap('YlGnBu', len(energy_kev_ranges))
boundaries = [range[0] for range in energy_kev_ranges] + [energy_kev_ranges[-1][1]]
norm = BoundaryNorm(boundaries, cmap.N, clip=True)

# Set the circle radius
circle_radius = 900

# Create a heatmap for months 1+2+3+4
heatmap1, xedges1, yedges1 = np.histogram2d(df_1to4['x.pos.asec'], df_1to4['y.pos.asec'], bins=30)
extent1 = [-circle_radius, circle_radius, -circle_radius, circle_radius]
fig1, ax1 = plt.subplots(figsize=(10, 8))
sc1 = ax1.imshow(heatmap1.T, extent=extent1, origin='lower', aspect='auto', cmap=cmap, alpha=0.7, norm=norm)
colorbar_ticks1 = [range[0] for range in energy_kev_ranges] + [800]
ax1.set_title('Solar Flare Intensity Heatmap (Months 1+2+3+4)')
ax1.set_xlabel('X Position (arcseconds)')
ax1.set_ylabel('Y Position (arcseconds)')
circle1 = plt.Circle((0, 0), circle_radius, color='r', fill=False)
ax1.add_artist(circle1)
cbar1 = fig1.colorbar(sc1, ax=ax1, label='Intensity', boundaries=boundaries, ticks=colorbar_ticks1)

# Create a heatmap for months 21+22+23+24
heatmap2, xedges2, yedges2 = np.histogram2d(df_21to24['x.pos.asec'], df_21to24['y.pos.asec'], bins=30)
extent2 = [-circle_radius, circle_radius, -circle_radius, circle_radius]
fig2, ax2 = plt.subplots(figsize=(10, 8))
sc2 = ax2.imshow(heatmap2.T, extent=extent2, origin='lower', aspect='auto', cmap=cmap, alpha=0.7, norm=norm)
colorbar_ticks2 = [range[0] for range in energy_kev_ranges] + [800]
ax2.set_title('Solar Flare Intensity Heatmap (Months 21+22+23+24)')
ax2.set_xlabel('X Position (arcseconds)')
ax2.set_ylabel('Y Position (arcseconds)')
circle2 = plt.Circle((0, 0), circle_radius, color='r', fill=False)
ax2.add_artist(circle2)
cbar2 = fig2.colorbar(sc2, ax=ax2, label='Intensity', boundaries=boundaries, ticks=colorbar_ticks2)
plt.show()


