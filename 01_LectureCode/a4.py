import pandas as pd

# Getting Info
movies = pd.read_csv('Data/movies.csv')
print(movies.info())
print(movies.shape)
