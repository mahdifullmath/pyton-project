import pandas as pd
import random

# تعریف یک لیست از نام‌های مختلف
names = ['John', 'Emma', 'Michael', 'Sophia', 'William', 'Olivia', 'James', 'Ava', 'Daniel', 'Isabella']

# تعریف یک دیتافریم خالی
data = pd.DataFrame()

# ایجاد ۵۰ نمونه با ۱۰ صفت مختلف
for i in range(50):
    sample = {
        'Name': random.choice(names),
        'Age': random.randint(18, 60),
        'Gender': random.choice(['Male', 'Female']),
        'City': random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']),
        'Education': random.choice(['High School', 'Bachelor', 'Master', 'PhD']),
        'Income': random.randint(20000, 100000),
        'Marital Status': random.choice(['Single', 'Married', 'Divorced', 'Widowed']),
        'Employment Status': random.choice(['Employed', 'Unemployed', 'Self-employed']),
        'Hobby': random.choice(['Reading', 'Sports', 'Traveling', 'Cooking', 'Gardening']),
        'Favorite Color': random.choice(['Red', 'Blue', 'Green', 'Yellow', 'Purple'])
    }
    data = data.append(sample, ignore_index=True)

# ذخیره داده‌ها در یک فایل اکسل
data.to_excel('sample_data.xlsx', index=False)

import random
from scipy.spatial.distance import pdist, squareform
data_numeric = data.copy()
for column in data.columns:
    if data[column].dtype == object:
        data_numeric[column] = pd.Categorical(data[column]).codes

# محاسبه ماتریس فاصله
distances = pdist(data_numeric, metric='cosine')

dissimilarity_matrix=  squareform(distances)
similarity_matrix  = 1 - dissimilarity_matrix
# نمایش ماتریس عدم تشابه
print(dissimilarity_matrix)

# محاسبه ماتریس فاصله
distance_matrixx = pd.DataFrame(dissimilarity_matrix)
distance_matrixx.to_excel('matris_adamtashaboh.xlsx')

