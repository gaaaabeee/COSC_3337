import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Load dataset
df = pd.read_csv('Solar_flare_RHESSI_2004_05.csv')

#get df with proper months
months_1_to_4 = ((df['year'] == 2004) & (df['month'].between(1, 4)))
df_months_1_to_4 = df[months_1_to_4]

months_21_to_24 = ((df['year'] == 2005) & (df['month'].between(9, 12)))
df_months_21_to_24 = df[months_21_to_24]

#filter energy range by KeV
energy_range = [(6, 12), (12, 25), (25, 50), (50, 100), (100, 300), (300, 800)]

# Group data by location based on (X, Y)
grouped_data = df_months_1_to_4.groupby(['x.pos.asec', 'y.pos.asec'])

# Method 1: Intensity Estimation based on total.counts
# Calculate intensity for Method 1 for each location
method1_intensity = grouped_data['total.counts'].sum()





# Method 1 Intensity Map
plt.figure(figsize=(10, 8))
plt.scatter(method1_intensity.index.get_level_values(0), method1_intensity.index.get_level_values(1), c=method1_intensity, cmap='viridis', s=30)
plt.colorbar(label='Method 1 Intensity')
plt.xlabel('X Position (arcsec)')
plt.ylabel('Y Position (arcsec)')
plt.title('Intensity Map for Method 1 (Months 1-4)')
plt.show()


