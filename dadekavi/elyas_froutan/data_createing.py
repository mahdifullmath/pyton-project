import pandas as pd
import random

# Define a list of different names
names = ['Alice', 'Bob', 'Eva', 'David', 'Lily', 'Tom', 'Sophie', 'Chris', 'Anna', 'Peter']

# Define an empty dataframe
data = pd.DataFrame()

# Create 100 samples with 10 different attributes
for i in range(100):
    sample = {
        'Name': random.choice(names),
        'Age': random.randint(20, 70),
        'Gender': random.choice(['Male', 'Female']),
        'City': random.choice(['London', 'Paris', 'Berlin', 'Tokyo', 'Sydney']),
        'Education': random.choice(['High School', 'Bachelor', 'Master', 'PhD']),
        'Income': random.randint(25000, 120000),
        'Marital Status': random.choice(['Single', 'Married', 'Divorced', 'Widowed']),
        'Employment Status': random.choice(['Employed', 'Unemployed', 'Self-employed']),
        'Hobby': random.choice(['Music', 'Painting', 'Photography', 'Dancing', 'Hiking']),
        'Favorite Color': random.choice(['Black', 'White', 'Gray', 'Brown', 'Orange'])
    }
    data = data.append(sample, ignore_index=True)

# Save the data to an Excel file
data.to_excel('modified_sample_data.xlsx', index=False)

