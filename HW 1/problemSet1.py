import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Suppress warnings
import warnings
warnings.filterwarnings("ignore")

csv_file = "Videogame_Sales_2016_Processed.csv"

df = pd.read_csv(csv_file)

attr_columns = ['Critic_Score', 'User_Score', 'NA_Sales', 'JP_Sales', 'Global_Sales']

df_columns = df[attr_columns]

cov_matrix = np.cov(df_columns, rowvar=False)

correlation_matrix = df_columns.corr()

print("Covariance Matrix:")
print(cov_matrix)

print("Correlation of attributes:")
print(correlation_matrix)

#There isn't a strong correlation of critic/user score and sales, however there is a strong coorelation
#between NA sales and global sales which might indicate that NA buying trends are similar to the worlds
#trends or that NA is a large chunk of gloval sales

def create_scatterplot(x, y, x_label, y_label, title):
    plt.scatter(x, y, label='Scatterplot', color='blue', marker='o')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


# Create a scatterplot for Critic Score vs. Critic Count
create_scatterplot(df['Critic_Score'], df['Critic_Count'], 'Critic Score', 'Critic Count', 'Critic Score vs. Critic Count')

# Create a scatterplot for User Score vs. Global Sales
create_scatterplot(df['User_Score'], df['Global_Sales'], 'User Score', 'Global Sales', 'User Score vs. Global Sales')

#theres a trend (If you can call it that) of more critcs = means higher score,
#  there is no trend beween user score and global sales.

#question 3

# Count occurrences of 'high,' 'medium,' and 'low' in GS_Category
category_counts = df['GS_Category'].value_counts()

# Get the counts
high_count = category_counts.get('high', 0)
medium_count = category_counts.get('medium', 0)
low_count = category_counts.get('low', 0)

# Create a single figure for all the subplots
plt.figure(figsize=(18, 12))

# High GS_category - Platform
plt.subplot(3, 2, 1)
plt.hist(df[df['GS_Category'] == 'high']['Platform'], bins=20, edgecolor='black')
plt.title(f'High GS_category - Platform (Count: {high_count})')

# Medium GS_category - Platform
plt.subplot(3, 2, 2)
plt.hist(df[df['GS_Category'] == 'medium']['Platform'], bins=20, edgecolor='black')
plt.title(f'Medium GS_category - Platform (Count: {medium_count})')

# Low GS_category - Platform
plt.subplot(3, 2, 3)
plt.hist(df[df['GS_Category'] == 'low']['Platform'], bins=20, edgecolor='black')
plt.title(f'Low GS_category - Platform (Count: {low_count})')

# High GS_category - User_Count
plt.subplot(3, 2, 4)
plt.hist(df[df['GS_Category'] == 'high']['User_Count'], bins=20, edgecolor='black')
plt.title(f'High GS_category - User_Count')

# Medium GS_category - User_Count
plt.subplot(3, 2, 5)
plt.hist(df[df['GS_Category'] == 'medium']['User_Count'], bins=20, edgecolor='black')
plt.title(f'Medium GS_category - User_Count')

# Low GS_category - User_Count
plt.subplot(3, 2, 6)
plt.hist(df[df['GS_Category'] == 'low']['User_Count'], bins=20, edgecolor='black')
plt.title(f'Low GS_category - User_Count')

# Add spacing between subplots
plt.tight_layout()

# Show the figure
plt.show()

#PS2 PS3 and Xbox 360 had lots of high score games and were popular amongst users

#Question 4

# Filter data by GS_Category
low_category = df[df['GS_Category'] == 'low']
medium_category = df[df['GS_Category'] == 'medium']
high_category = df[df['GS_Category'] == 'high']

# Create a single figure for all the box plots
plt.figure(figsize=(12, 8))

# Box plot for User_Score by GS_Category
plt.subplot(2, 2, 1)
plt.boxplot([low_category['User_Score'], medium_category['User_Score'], high_category['User_Score'], df['User_Score']], labels=['Low', 'Medium', 'High', 'All'])
plt.title('User_Score by GS_Category')

# Box plot for Critic_Score by GS_Category
plt.subplot(2, 2, 2)
plt.boxplot([low_category['Critic_Score'], medium_category['Critic_Score'], high_category['Critic_Score'], df['Critic_Score']], labels=['Low', 'Medium', 'High', 'All'])
plt.title('Critic_Score by GS_Category')

# Add spacing between subplots
plt.tight_layout()

# Show the figure
plt.show()


#question 5
# Define the pairs of attributes and their corresponding colors
attribute_pairs = [
    ('Critic_Score', 'NA_Sales'),
    ('NA_Sales', 'User_Score'),
    ('Critic_Score', 'User_Score')
]

colors = {'low': 'red', 'medium': 'green', 'high': 'blue'}

# Create separate scatter plots for each attribute pair
for attribute_x, attribute_y in attribute_pairs:
    plt.figure(figsize=(10, 6))
    plt.scatter(
        df[attribute_x], df[attribute_y], 
        c=df['GS_Category'].map(colors),  # Use colors based on GS_Category
        label=df['GS_Category'],
        alpha=0.5  # Adjust alpha for transparency
    )
    plt.xlabel(attribute_x)
    plt.ylabel(attribute_y)
    plt.title(f'{attribute_x} vs. {attribute_y}')
    plt.legend(title='GS_Category')
    plt.grid(True)
    plt.show()


    #question 6

# Set the style for the plots
sns.set(style="white")

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharex=True, sharey=True)

# Density plot for 'Critic_Score' vs. 'User_Score' for low, medium, and high GS_Category
sns.kdeplot(data=low_category, x='Critic_Score', y='User_Score', cmap="Reds", ax=axes[0], fill=True, alpha=0.7)
sns.kdeplot(data=medium_category, x='Critic_Score', y='User_Score', cmap="Greens", ax=axes[0], fill=True, alpha=0.7)
sns.kdeplot(data=high_category, x='Critic_Score', y='User_Score', cmap="Blues", ax=axes[0], fill=True, alpha=0.7)

# Set labels and titles
axes[0].set_xlabel('Critic_Score')
axes[0].set_ylabel('User_Score')
axes[0].set_title('Density Plot by GS_Category')

# Density plot for 'Critic_Score' vs. 'User_Score' for all instances
sns.kdeplot(data=df, x='Critic_Score', y='User_Score', cmap="YlOrBr", ax=axes[1], fill=True, alpha=0.7)

# Set labels and titles
axes[1].set_xlabel('Critic_Score')
axes[1].set_ylabel('User_Score')
axes[1].set_title('Density Plot for All Instances')

# Show the plots
plt.tight_layout()
plt.show()

#question 7

# Create a frequency table for genre and GS_Category associations
genre_gs_freq_table = pd.crosstab(df['Genre'], df['GS_Category'])

# Display the frequency table
print("Frequency Table for Genre vs. GS_Category Associations:")
print(genre_gs_freq_table)

# Create histograms for Global_Sales for each genre
genres = df['Genre'].unique()

# Create a single figure for all the subplots
plt.figure(figsize=(18, 12))

for i, genre in enumerate(genres):
    plt.subplot(3, 4, i + 1)  # Adjust the number of rows and columns as needed
    plt.hist(df[df['Genre'] == genre]['Global_Sales'], bins=20, edgecolor='black')
    plt.title(f'Global Sales for {genre}')
    plt.xlabel('Global Sales')
    plt.ylabel('Frequency')

# Add spacing between subplots
plt.tight_layout()

# Show the histograms
plt.show()

