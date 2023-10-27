import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv('Solar_flare_RHESSI_2004_05.csv')

# Get data for Months 1-4 in 2004
months_1_to_4 = ((df['year'] == 2004) & (df['month'].between(1, 4)))
df_months_1_to_4 = df[months_1_to_4]

# Get data for Months 21-24 in 2005
months_21_to_24 = ((df['year'] == 2005) & (df['month'].between(9, 12)))
df_months_21_to_24 = df[months_21_to_24]

# Filter energy range by KeV
energy_range = [(6, 12), (12, 25), (25, 50), (50, 100), (100, 300), (300, 800)]

# Group data by location based on (X, Y)
grouped_data_1to4 = df_months_1_to_4.groupby(['x.pos.asec', 'y.pos.asec'])
grouped_data_21to24 = df_months_21_to_24.groupby(['x.pos.asec', 'y.pos.asec'])

# Method 1: Intensity Estimation based on total.counts
# Calculate intensity for Method 1 for each location
method1_intensity_1to4 = grouped_data_1to4['total.counts'].sum()
method1_intensity_21to24 = grouped_data_21to24['total.counts'].sum()

# Calculate the radial distance (r_1to4) for each location
x_1to4 = grouped_data_1to4['x.pos.asec'].mean()
y_1to4 = grouped_data_1to4['y.pos.asec'].mean()

x_21to24 = grouped_data_21to24['x.pos.asec'].mean()
y_21to24 = grouped_data_21to24['y.pos.asec'].mean()

t = 80

r_1to4 = np.sqrt(x_1to4 ** 2 + y_1to4 ** 2)
r0_1to4 = np.percentile(r_1to4, t)

r_21to24 = np.sqrt(x_21to24 ** 2 + y_21to24 ** 2)
r0_21to24 = np.percentile(r_21to24, t)

# Create subplots for both intensity maps
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Method 1 Intensity Map for Months 1-4
circle_1to4 = plt.Circle((0, 0), r0_1to4, color='r', fill=False)
ax1.add_patch(circle_1to4)
scatter_1to4 = ax1.scatter(
    method1_intensity_1to4.index.get_level_values(0),
    method1_intensity_1to4.index.get_level_values(1),
    c=method1_intensity_1to4,
    cmap='viridis',
    s=30
)
ax1.set_xlabel('X Position (arcsec)')
ax1.set_ylabel('Y Position (arcsec)')
ax1.set_title('Intensity Map for Method 1 (Months 1-4)')
fig.colorbar(scatter_1to4, ax=ax1, label='Method 1 Intensity')

# Method 1 Intensity Map for Months 21-24
circle_21to24 = plt.Circle((0, 0), r0_21to24, color='r', fill=False)
ax2.add_patch(circle_21to24)
scatter_21to24 = ax2.scatter(
    method1_intensity_21to24.index.get_level_values(0),
    method1_intensity_21to24.index.get_level_values(1),
    c=method1_intensity_21to24,
    cmap='viridis',
    s=30
)
ax2.set_xlabel('X Position (arcsec)')
ax2.set_ylabel('Y Position (arcsec)')
ax2.set_title('Intensity Map for Method 1 (Months 21-24)')
fig.colorbar(scatter_21to24, ax=ax2, label='Method 1 Intensity')

plt.show()

