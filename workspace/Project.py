# Task-0:- Setup (We're going to use pandas for data analysis and plotly.express for interactive data visualization)

# Importing necessary packages
import pandas as pd
import plotly.express as px 


# Task-1:- Reading in the data (Let's read in and display the fitness_data.csv file using pandas.)

# Reading in the dataset "fitness.csv"
fitness_data = pd.read_csv("fitness_data.csv")

# Display the data
fitness_data


# Task-2:- Checking for missing values (Now that we've read in the data, let's check whether it has any missing values.)

# Does the data have any missing values?
missing_values = fitness_data.isnull().sum()
missing_values

# Which rows have missing values?
rows_with_missing_values = fitness_data[fitness_data.isnull().any(axis=1)]
rows_with_missing_values