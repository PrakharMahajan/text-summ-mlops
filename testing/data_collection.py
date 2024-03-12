# Combining the CNN/Daily Mail dataset

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
combined_dataset.to_csv("combined_dataset_cnn.csv", index=False)

# Downloading and saving the XSum dataset

from datasets import load_dataset

xsum_dataset = load_dataset('xsum')

# Access train, validation, and test splits
train_data = xsum_dataset['train']
validation_data = xsum_dataset['validation']
test_data = xsum_dataset['test']

# Access individual examples
example = train_data[0]
document = example['document']
summary = example['summary']

# Print the first document and summary
print("Document:", document)
print("\nSummary:", summary)

# Downloading the NYT dataset

import ir_datasets
dataset = ir_datasets.load("nyt")
