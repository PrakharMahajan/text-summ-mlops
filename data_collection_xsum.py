from datasets import load_dataset
import pandas as pd

xsum_dataset = load_dataset('xsum')

# Convert dataset to DataFrame
df_train = pd.DataFrame(xsum_dataset['train'])
df_test = pd.DataFrame(xsum_dataset['test'])
df_validation = pd.DataFrame(xsum_dataset['validation'])

# Specify the Excel file path
train_file_path = 'dataset/xsum_dataset_train.xlsx'
test_file_path = 'dataset/xsum_dataset_test.xlsx'
validation_file_path = 'dataset/xsum_dataset_validation.xlsx'

# Save DataFrame to Excel
df_train.to_excel(train_file_path, index=False, engine='openpyxl')
df_test.to_excel(test_file_path, index=False, engine='openpyxl')
df_validation.to_excel(validation_file_path, index=False, engine='openpyxl')
