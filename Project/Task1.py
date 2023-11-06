import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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

#help with outliers
t = 75

r_1to4 = np.sqrt(x_1to4 ** 2 + y_1to4 ** 2)
r0_1to4 = np.percentile(r_1to4, t)

r_21to24 = np.sqrt(x_21to24 ** 2 + y_21to24 ** 2)
r0_21to24 = np.percentile(r_21to24, t)

# Define a colormap based on energy ranges
colors = ['blue', 'green', 'yellow', 'orange', 'red', 'purple']  # Colors corresponding to energy_range
colormap = plt.cm.colors.ListedColormap(colors)

# Create subplots for both intensity maps
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Method 1 Intensity Map for Months 1-4
circle_1to4 = plt.Circle((0, 0), r0_1to4, color='r', fill=False)
ax1.add_patch(circle_1to4)
scatter_1to4 = ax1.scatter(
    method1_intensity_1to4.index.get_level_values(0),
    method1_intensity_1to4.index.get_level_values(1),
    c=method1_intensity_1to4,
    cmap=colormap,
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
    cmap=colormap,
    s=30
)
ax2.set_xlabel('X Position (arcsec)')
ax2.set_ylabel('Y Position (arcsec)')
ax2.set_title('Intensity Map for Method 1 (Months 21-24)')
fig.colorbar(scatter_21to24, ax=ax2, label='Method 1 Intensity')

plt.show()


df['energy.kev'] = df['energy.kev'].astype('category')

# Iterate through each 'energy.kev' category and plot the KDE


for category in df['energy.kev'].cat.categories:
    subset = df[df['energy.kev'] == category]
    sns.kdeplot(subset['duration.s'], label=category, fill=True)

plt.legend(title='Energy.kev')
plt.xlabel('Duration.s')
plt.title('Density Plot by Energy.kev Category')
  
plt.show() 


#Method 2


duration_1to4 = df_months_1_to_4['duration.s'].values
#energy_kev_1to4 = df_months_1_to_4['energy.kev'].apply(lambda x: (int(x.split('-')[0]) + int(x.split('-')[1])) / 2).values
energy_kev_1to4 = df['energy.kev'].astype('category')


# Normalize "duration.s" and "energy.kev" (e.g., between 0 and 1)
duration_normalized = (df['duration.s'] - df['duration.s'].min()) / (df['duration.s'].max() - df['duration.s'].min())
energy_normalized = (df['energy.kev'] - df['energy.kev'].min()) / (df['energy.kev'].max() - df['energy.kev'].min())

def estimate_intensity(duration, energy):
    # Define your intensity estimation logic here
    # This can be a simple combination of duration and energy or a more complex function

    # For example, a simple linear combination:
    return 0.5 * duration + 0.5 * energy

# Calculate intensity for Method 2
method2_intensity_1to4 = estimate_intensity(df_months_1_to_4['duration_normalized'], df_months_1_to_4['energy_normalized'])

# Create a new figure for Method 2
fig, ax3 = plt.subplots(figsize=(8, 8))

# Method 2 Intensity Map for Months 1-4
circle_1to4 = plt.Circle((0, 0), r0_1to4, color='r', fill=False)
ax3.add_patch(circle_1to4)
scatter_1to4 = ax3.scatter(
    method2_intensity_1to4,
    method1_intensity_1to4.index.get_level_values(1),  # Use the same Y values as Method 1
    c=method2_intensity_1to4,
    cmap=colormap,
    s=30
)
ax3.set_xlabel('Method 2 Intensity')
ax3.set_ylabel('Y Position (arcsec)')
ax3.set_title('Intensity Map for Method 2 (Months 1-4)')
colorbar_1to4 = fig.colorbar(scatter_1to4, ax=ax3, label='Method 2 Intensity')

plt.show()