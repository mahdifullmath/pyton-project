import pandas as pd
import numpy as np

num_samples = 50


data = {
    'سن': np.random.randint(20, 60, num_samples),
    'جنسیت': np.random.choice(['مرد', 'زن'], num_samples),
    'شغل': np.random.choice(['مهندس', 'پزشک', 'معلم', 'بازیگر'], num_samples),
    'وضعیت_تاهل': np.random.choice(['مجرد', 'متاهل'], num_samples),
    'امتیاز': np.random.rand(num_samples),
    'محل_زندگی': np.random.choice(['شهر', 'روستا'], num_samples),
    'سلامتی': np.random.choice(['خوب', 'متوسط', 'ضعیف'], num_samples),
    'تحصیلات': np.random.choice(['لیسانس', 'فوق لیسانس', 'دکتری'], num_samples),
    'وزن': np.random.randint(50, 100, num_samples),
    'قد': np.random.randint(150, 190, num_samples),
}

df = pd.DataFrame(data)


df.to_excel('dataset.xlsx', index=False)


dissimilarity_matrix = np.zeros((num_samples, num_samples))
for i in range(num_samples):
    for j in range(num_samples):
        if i != j:
            dissimilarity_matrix[i, j] = np.sum(df.iloc[i] != df.iloc[j])/11


df_dissimilarity = pd.DataFrame(dissimilarity_matrix)
df_dissimilarity.to_excel('dissimilarity_matrix.xlsx', index=False)



