import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# Load the dataset from a CSV file into a DataFrame
df = pd.read_csv("heart_disease_uci.csv")

# Print the shape of the DataFrame (number of rows and columns)
print(df.shape)

# Display the first 5 rows of the DataFrame 
print(df.head())

# Print the column names of the DataFrame
print(df.columns)

# Display information about the DataFrame
print(df.info())

# Check missing values 
null_values = df.isnull().sum()
print(null_values)

# Check the minimum and maximum values in the column 
print(df['age'].min(), df['age'].max())

# Plot a distribution to see the distribution of ages in the dataset  
sns.histplot(df['age'])

# Showing the distribution of age with colours distinguishing between different values in the 'sex' column
fig = px.histogram(data_frame=df, x='age', color='sex')
fig.show()

### Check for duplicate rows [?]

# Count the occurrences of each value in the 'sex' column
sex_counts = df['sex'].value_counts()
print(sex_counts)

# Plot a pie chart
fig = px.pie(df, names = 'sex', color = 'sex')
fig.show()

# x-axis represents the 'dataset' column values
# bars colored by the values in the 'sex' column 
fig = px.bar(df, x='dataset', color='sex')
fig.show()
print(df.groupby('sex')['dataset'].value_counts())

# Create a count plot to show the frequency of each 'cp' value, colored by 'num'
plt.figure(figsize=(10, 6))
sns.countplot(x='cp', hue='num', data=df)

# Set title and labels for better readability
plt.xlabel('Chest Pain Type')
plt.ylabel('Amount')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# Create a count plot to show the distribution of the 'num' column
plt.figure(figsize=(8, 6))
sns.countplot(x='num', data=df)
plt.title('Distribution of num')
plt.xlabel('num')
plt.ylabel('Amount')
plt.show()

# Box plot to visually check for outliers in the 'trestbps' column 
plt.figure(figsize=(8, 6))
sns.boxplot(y=df['trestbps'])  
plt.title('Box Plot for trestbps (Resting Blood Pressure)')
plt.ylabel('trestbps (Resting Blood Pressure)')
plt.show()
