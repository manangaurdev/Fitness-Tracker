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


# Task-3:- Exploring the data (Lets start exploring our data by calculating summary statistics and confirming that our columns are of the correct data type)

# What are the summary statistics?
summary_statistics = fitness_data.describe()
summary_statistics

# Check the data types of each column
fitness_data['date'] = pd.to_datetime(fitness_data['date']) 

# Convert the data column to a datetime format
fitness_data.dtypes



# Task-4:- Create useful new columns (Sometimes we might want to rename columns with more descriptive names to be easier to interpret, or create new columns to measure things we are interested in)

# Rename 'weight' and 'workout_duration' to have more descriptive names
fitness_data.rename(columns={'weight': 'weight_kg', 'workout_duration': 'workout_duration_minutes'}, inplace=True)

# Add a new column 'weight_lbs' converting weight from kilograms to pounds (1 kg = 2.20462 lbs)
fitness_data['weight_lbs'] = fitness_data['weight_kg'] * 2.20462

# Add a column to indicate the day of the week
fitness_data['day_of_week'] = fitness_data['date'].dt.day_name()

# Add a column to indicate weekends
fitness_data['is_weekend'] = fitness_data['day_of_week'].isin(['Saturday', 'Sunday'])

# Display the data
fitness_data 


# Add a new column 'sleep_debt' that calculates the difference between sleep_hours and a target of 7.5 hours
fitness_data['sleep_debt'] = fitness_data['sleep_hours'] - 7.5

# Create a new column that calculates the cumulative sleep debt
fitness_data['cumulative_sleep_debt'] = fitness_data['sleep_debt'].cumsum()

fitness_data


# Task-5:- Visualizing trends across single variables (Lets visualize the distributions and trends of different columns in data)
import plotly.express as px

# Create a plotly histogram of the number of steps
fig = px.histogram(fitness_data, x='steps', nbins=30, title='Histogram of Steps')
fig.update_layout(
    xaxis_title='Number of Steps',
    yaxis_title='Frequency',
    bargap=0.1
)
fig.show()


# Create a line chart for the number of steps over time
fig = px.line(fitness_data, x='date', y='steps', title='Number of Steps Over Time')
fig.update_layout(
    xaxis_title = 'Date',
    yaxis_title = 'Number of Steps'
)

# Display the line chart
fig.show()

# Visualize weight trend over time
fig = px.line(fitness_data, x='date', y='weight_kg', title='Weight Trend Over Time')

fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Weight (kg)'
)

# Display the line chart
fig.show()


# Task-6:- Visualizing trends across multiple variables

# Create a box plot for sleep hours comparing weekdays and weekends
fig = px.box(fitness_data, x='is_weekend', y='sleep_hours',
             title='Sleep Hours: Weekdays vs Weekends',
             labels={'is_weekend': 'Is Weekend', 'sleep_hours': 'Sleep Hours'})

# Display the box plot
fig.show()

# Visualize average sleep by day of week
fig = px.bar(fitness_data.groupby('day_of_week')['sleep_hours'].mean().reset_index(),
             x='day_of_week', y='sleep_hours',
             title='Average Sleep Hours by Day of Week',
             labels={'day_of_week': 'Day of Week', 'sleep_hours': 'Average Sleep Hours'})

# Display the bar chart
fig.show() 