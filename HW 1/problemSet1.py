import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

