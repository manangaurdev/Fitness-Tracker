# Task-0:- Setup (We're going to use pandas for data analysis and plotly.express for interactive data visualization)

# Importing necessary packages
import pandas as pd
import plotly.express as px 


# Task-1:- Reading in the data (Let's read in and display the fitness_data.csv file using pandas.)

# Reading in the dataset "fitness.csv"
fitness_data = pd.read_csv("fitness_data.csv")

# Display the data
fitness_data