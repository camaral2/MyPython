import pandas as pd
import numpy as np

def read_clean_data(df, field, max_scores3 = 2):
  # Handle missing values
  df.fillna(df.mean(), inplace=True)
  
  # Remove duplicate records
  df.drop_duplicates(subset=field, inplace=True)
  
  # Standardize data formats
  df[field] = df[field].astype(int)
  
  # Detect and handle outliers
  z_scores = np.abs((df[field] - df[field].mean()) / df[field].std())
  outliers = df[z_scores > max_scores]
  df = df[~df.index.isin(outliers.index)]
  
  return df

# Create a sample dataframe with multiple records
data = {'A': [1, 2, 3, 1, 2, 3, 8, 7, 6, 9, 30, 4, 3, 2, 5, 6, 7, 70], 'B': [2,9,6,4,3,5]}

df = pd.DataFrame(data)
df = read_clean_data(df, 'A', 1.5)

print(df)

# Save the cleaned dataset
df.to_csv('cleaned_data.csv', index=False)




