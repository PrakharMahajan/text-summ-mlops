import pandas as pd

# Load each CSV file into a DataFrame
csv_file1 = "cnn_dailymail/test.csv"
csv_file2 = "cnn_dailymail/train.csv"
csv_file3 = "cnn_dailymail/validation.csv"

df1 = pd.read_csv(csv_file1)
df2 = pd.read_csv(csv_file2)
df3 = pd.read_csv(csv_file3)

# Combine the DataFrames into a single dataset
combined_dataset = pd.concat([df1, df2, df3], ignore_index=True)

# Display the combined dataset
print("Combined Dataset:")
print(combined_dataset.head())

# Perform any additional preprocessing steps here

# Save the combined dataset to a new CSV file
combined_dataset.to_csv("combined_dataset.csv", index=False)
