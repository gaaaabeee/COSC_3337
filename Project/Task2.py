import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.patches import Circle
import pandas as pd
import seaborn as sns
import os

# Load dataset
df = pd.read_csv('Solar_flare_RHESSI_2004_05.csv')
# Create a copy of the original DataFrame
new_df = df.copy()
# Map the months when the year is 2005
new_df.loc[(new_df['year'] == 2005) & (new_df['month'] <= 12), 'month'] += 12
# Save the modified DataFrame to a new CSV file
new_df.to_csv('Solar_flare_RHESSI_2004_05_modified.csv', index=False)
newdf = pd.read_csv('Solar_flare_RHESSI_2004_05_modified.csv')

#boxplot
fig, ax = plt.subplots(figsize=(10, 8))
boxplot = ax.boxplot(df['total.counts'], vert=False, showfliers=False)
plt.show()

percentile_25 = np.percentile(df['total.counts'], 25)
percentile_85 = np.percentile(df['total.counts'], 85)
d1 = percentile_85
d2 = percentile_25
radius = 1000

# List of months for which you want to create batches
months = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
num_batches = len(months) 

# Create a directory to save the PNG files
output_dir = 'heatmaps_output'
os.makedirs(output_dir, exist_ok=True)

# Number of bins for the heatmap
num_bins = 30
# Define a function to create a heatmap
def create_heatmap(x, y, counts, num_bins):
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=num_bins, weights=counts)
    return heatmap, xedges, yedges
# Define a function to find local maxima
def localMax(arr):
    from scipy.ndimage import maximum_filter
    return arr == maximum_filter(arr, size=3, mode='constant', cval=np.nan)
# Initialize an empty list to store heatmaps
heatmaps = []


# Create a loop to display heatmaps with titles based on batches of months
for i in range(num_batches):
    extent = [-radius, radius, -radius, radius]
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Determine the starting and ending months for the current batch
    start_month = months[i]
    end_month = months[i] + 3 
    # Create a batch for the current 4-month period
    bt = ((newdf['year'] == 2004) | (newdf['year'] == 2005)) & (newdf['month'].between(start_month, end_month))

    # Print the current batch's months
    print(f'Months {start_month}-{end_month}')

    batch = newdf[bt]
    batchX = batch['x.pos.asec'].values
    batchY = batch['y.pos.asec'].values
    batchTotalCount = batch['total.counts'].values

    # Create a heatmap for the current batch
    heatmap, xedges, yedges = create_heatmap(batchX, batchY, batchTotalCount, num_bins)
    
    # Find local maxima in the heatmap
    hotspot_mask = localMax(heatmap)

    # Create a masked array for intensity values
    intensity = np.where(hotspot_mask, heatmap, 0)
    intensity_values = intensity[hotspot_mask]

    if intensity_values.size > 0:
        # Calculate normalization values only if intensity_values is not empty
        norm = Normalize(vmin=np.min(intensity_values), vmax=np.max(intensity_values))
    else:
        # Handle the case when there are no intensity values
        norm = None
    cmap = plt.get_cmap('Reds')
    
    # Plot the heatmap for the current batch with its title
    sc = ax.imshow(
        heatmap.T, extent=extent, origin='lower', aspect='auto', cmap=cmap, norm=norm, alpha=1
    )
    
    # Set the title based on the range of months in the current batch
    plt.title(f'Hotspot Visual: Total.Counts in Months: {start_month}-{end_month}')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    circle = plt.Circle((0, 0), radius, color='black', fill=False)
    ax.add_artist(circle)
    cbar = fig.colorbar(sc, ax=ax, label='Hotspot Intensity')

    # Save the heatmap as a PNG file
    output_filename = os.path.join(output_dir, f'heatmap_{start_month}-{end_month}.png')
    plt.savefig(output_filename, bbox_inches='tight')

    #plt.show()


#Contour Plots 
# Create a directory to save the PNG files
output_dir_d1 = 'kde_plots_output_d1'
os.makedirs(output_dir_d1, exist_ok=True)


output_dir_d2 = 'kde_plots_output_d2'
os.makedirs(output_dir_d2, exist_ok=True)

for i in range(len(months)):
    extent = [-radius, radius]

    # Determine the starting and ending months for the current batch
    start_month = months[i]
    end_month = months[i] + 3

    # Create a batch for the current 4-month period
    bt = ((newdf['year'] == 2004) | (newdf['year'] == 2005)) & (newdf['month'].between(start_month, end_month))

    # Print the current batch's months
    print(f'Months {start_month}-{end_month}')

    batch = newdf[bt]
    batchX = batch['x.pos.asec'].values
    batchY = batch['y.pos.asec'].values
    batchTotalCount = batch['total.counts'].values

    # Create a new figure for each plot
    fig, ax = plt.subplots(figsize=(5, 5))
    
    sns.kdeplot(x=batchX, y=batchY, fill=True, ax=ax, cmap='Reds', weights=(batchTotalCount >= d1))
    
    # Add a black circle
    circle = Circle((0, 0), radius, edgecolor='black', facecolor='none')
    ax.add_patch(circle)

    # Set the title based on the range of months in the current batch
    ax.set_title(f'KDE Plot: D1={d1} in Months: {start_month}-{end_month}')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_xlim(-radius, radius)
    ax.set_ylim(-radius, radius)

    # Save each plot as a PNG file
    plt.tight_layout(pad=3.0)
    plt.savefig(os.path.join(output_dir_d1, f'kde_plot_{start_month}_{end_month}.png'))
    #plt.show()


for i in range(len(months)):
    extent = [-radius, radius]

    # Determine the starting and ending months for the current batch
    start_month = months[i]
    end_month = months[i] + 3

    # Create a batch for the current 4-month period
    bt = ((newdf['year'] == 2004) | (newdf['year'] == 2005)) & (newdf['month'].between(start_month, end_month))

    # Print the current batch's months
    print(f'Months {start_month}-{end_month}')

    batch = newdf[bt]
    batchX = batch['x.pos.asec'].values
    batchY = batch['y.pos.asec'].values
    batchTotalCount = batch['total.counts'].values

    # Create a new figure for each plot
    fig, ax = plt.subplots(figsize=(5, 5))
    
    sns.kdeplot(x=batchX, y=batchY, fill=True, ax=ax, cmap='Reds', weights=(batchTotalCount >= d2))
    
    # Add a black circle
    circle = Circle((0, 0), radius, edgecolor='black', facecolor='none')
    ax.add_patch(circle)

    # Set the title based on the range of months in the current batch
    ax.set_title(f'KDE Plot: D2={d2} in Months: {start_month}-{end_month}')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_xlim(-radius, radius)
    ax.set_ylim(-radius, radius)

    # Save each plot as a PNG file
    plt.tight_layout(pad=3.0)
    plt.savefig(os.path.join(output_dir_d2, f'kde_plot_{start_month}_{end_month}.png'))
    #plt.show()