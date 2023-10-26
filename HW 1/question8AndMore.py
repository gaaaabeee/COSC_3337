import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

csv_file = "Videogame_Sales_2016_Processed.csv"
df = pd.read_csv(csv_file)

# Select the relevant columns 
selected_columns = ['Year_of_Release', 'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Global_Sales']

# Create a new dataFrame with selected columns
z_processed_df = df[selected_columns].copy()

# Calculate z-scores for the selected columns (mean=0, std=1)
z_processed_df['Year_of_Release'] = (z_processed_df['Year_of_Release'] - z_processed_df['Year_of_Release'].mean()) / z_processed_df['Year_of_Release'].std()
z_processed_df['Critic_Score'] = (z_processed_df['Critic_Score'] - z_processed_df['Critic_Score'].mean()) / z_processed_df['Critic_Score'].std()
z_processed_df['Critic_Count'] = (z_processed_df['Critic_Count'] - z_processed_df['Critic_Count'].mean()) / z_processed_df['Critic_Count'].std()
z_processed_df['User_Score'] = (z_processed_df['User_Score'] - z_processed_df['User_Score'].mean()) / z_processed_df['User_Score'].std()
z_processed_df['User_Count'] = (z_processed_df['User_Count'] - z_processed_df['User_Count'].mean()) / z_processed_df['User_Count'].std()

# Split the data into independent variables (X) and the dependent variable (y)
X = z_processed_df[['Year_of_Release', 'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count']]
y = z_processed_df['Global_Sales']

# Fit a linear regression model
model = LinearRegression()
model.fit(X, y)

# Get the R-squared value
r_squared = r2_score(y, model.predict(X))

# Get the coefficients of the regression function
coefficients = model.coef_

# Print the results
print(f"R-squared (R2) of the linear model: {r_squared:.4f}")
print("Coefficients of the regression function:")
for i, coef in enumerate(coefficients):
    print(f"Coefficient for {X.columns[i]}: {coef:.4f}")

#question 9


whole_tree_columns = ['NA_Sales','EU_Sales','JP_Sales','Critic_Score','Critic_Count','User_Score','User_Count']
sales_columns = ['NA_Sales','EU_Sales','JP_Sales']
score_count_columns = ['Critic_Score','Critic_Count','User_Score','User_Count']

# Define the mapping from class labels to numerical values
class_mapping = {'high': 0, 'medium': 1, 'low': 2}

# Create a new column 'GS_Category_Num' with numerical values
df['GS_Category_Num'] = df['GS_Category'].map(class_mapping)

# Now, you can use 'GS_Category_Num' as the class variable
class_variable = 'GS_Category_Num'

#Sales column tree
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[sales_columns], df[class_variable], test_size=0.2, random_state=42)

# Create a Decision Tree Classifier with a maximum of 20 nodes
tree_model = DecisionTreeClassifier(max_leaf_nodes=10)

# Fit the model on the training data
tree_model.fit(X_train, y_train)

# Predict on the test data
y_pred = tree_model.predict(X_test)

# Calculate accuracy on the test data
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy and the number of nodes in the tree
print(f"Sales Accuracy: {accuracy:.4f}")
print(f"Number of nodes in the tree: {tree_model.tree_.node_count}")

plt.figure(figsize=(15, 5))  # Adjust the figure size as needed
plot_tree(tree_model, filled=True, feature_names=sales_columns, class_names=['high', 'medium', 'low'])
plt.title("Decision Tree Sales")
plt.show()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[score_count_columns], df[class_variable], test_size=0.2, random_state=42)

# Create a Decision Tree Classifier with a maximum of 20 nodes
tree_model = DecisionTreeClassifier(max_leaf_nodes=10)

# Fit the model on the training data
tree_model.fit(X_train, y_train)

# Predict on the test data
y_pred = tree_model.predict(X_test)

# Calculate accuracy on the test data
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy and the number of nodes in the tree
print(f"Score and Count Accuracy: {accuracy:.4f}")
print(f"Number of nodes in the tree: {tree_model.tree_.node_count}")

plt.figure(figsize=(15, 5))  # Adjust the figure size as needed
plot_tree(tree_model, filled=True, feature_names=score_count_columns, class_names=['high', 'medium', 'low'])
plt.title("Decision Tree Score and Count")
plt.show()



# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[whole_tree_columns], df[class_variable], test_size=0.2, random_state=42)

# Create a Decision Tree Classifier with a maximum of 20 nodes
tree_model = DecisionTreeClassifier(max_leaf_nodes=10)

# Fit the model on the training data
tree_model.fit(X_train, y_train)

# Predict on the test data
y_pred = tree_model.predict(X_test)

# Calculate accuracy on the test data
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy and the number of nodes in the tree
print(f"All columns Accuracy: {accuracy:.4f}")
print(f"Number of nodes in the tree: {tree_model.tree_.node_count}")

plt.figure(figsize=(15, 5))  # Adjust the figure size as needed
plot_tree(tree_model, filled=True, feature_names=whole_tree_columns, class_names=['high', 'medium', 'low'])
plt.title("Decision Tree all Variables")
plt.show()
