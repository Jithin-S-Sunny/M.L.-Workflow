import pandas as pd
dataframe1 = pd.read_csv("example2.txt", header=None)
dataframe1.to_csv('example2.csv', index = None)
