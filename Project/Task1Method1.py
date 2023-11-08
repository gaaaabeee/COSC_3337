import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import LogNorm
import cv2

# Load dataset
df = pd.read_csv('Solar_flare_RHESSI_2004_05.csv')

# Set the circle radius
circle_radius = 900

# Filter data for months 1+2+3+4
m_1to4 = ((df['year'] == 2004) & (df['month'].between(1, 4)))
df_1to4 = df[m_1to4]

# Filter data for months 21+22+23+24
m_21to24 = ((df['year'] == 2005) & (df['month'].between(9, 12)))
df_21to24 = df[m_21to24]


# Create a heatmap for months 1+2+3+4 with a logarithmic color scale for "duration.s" and "energy.kev"
heatmap1, xedges1, yedges1 = np.histogram2d(
    df_1to4['x.pos.asec'], df_1to4['y.pos.asec'], bins=30, weights=df_1to4['total.counts']
)
extent1 = [-circle_radius, circle_radius, -circle_radius, circle_radius]
fig1, ax1 = plt.subplots(figsize=(10, 8))
sc1 = ax1.imshow(
    heatmap1.T, extent=extent1, origin='lower', aspect='auto', cmap='YlOrRd', alpha=0.7, norm=LogNorm()
)
ax1.set_title('Solar Flare Intensity Heatmap (Months 1+2+3+4) - Total.counts')
ax1.set_xlabel('X Position (arcseconds)')
ax1.set_ylabel('Y Position (arcseconds)')
circle1 = plt.Circle((0, 0), circle_radius, color='r', fill=False)
ax1.add_artist(circle1)
cbar1 = fig1.colorbar(sc1, ax=ax1, label='Intensity (Log Scale)')

# Create a heatmap for months 21+22+23+24 with a logarithmic color scale for "duration.s" and "energy.kev"
heatmap2, xedges2, yedges2 = np.histogram2d(
    df_21to24['x.pos.asec'], df_21to24['y.pos.asec'], bins=30, weights=df_21to24['total.counts']
)
extent2 = [-circle_radius, circle_radius, -circle_radius, circle_radius]
fig2, ax2 = plt.subplots(figsize=(10, 8))
sc2 = ax2.imshow(
    heatmap2.T, extent=extent2, origin='lower', aspect='auto', cmap='YlOrRd', alpha=0.7, norm=LogNorm()
)
ax2.set_title('Solar Flare Intensity Heatmap (Months 21+22+23+24) - Total.counts')
ax2.set_xlabel('X Position (arcseconds)')
ax2.set_ylabel('Y Position (arcseconds)')
circle2 = plt.Circle((0, 0), circle_radius, color='r', fill=False)
ax2.add_artist(circle2)
cbar2 = fig2.colorbar(sc2, ax=ax2, label='Intensity (Log Scale)')

plt.show()


