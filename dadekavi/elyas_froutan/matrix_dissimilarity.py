
from scipy.spatial.distance import pdist, squareform
import pandas as pd
data = pd.read_excel('sample_data.xlsx')
data_numeric = data.copy()
for column in data.columns:
    if data[column].dtype == object:
        data_numeric[column] = pd.Categorical(data[column]).codes


distances = pdist(data_numeric, metric='hamming')

dissimilarity_matrix=  squareform(distances)


print(dissimilarity_matrix)


distance_matrixx = pd.DataFrame(dissimilarity_matrix)
distance_matrixx.to_excel('dissimilarity_matrix.xlsx')

