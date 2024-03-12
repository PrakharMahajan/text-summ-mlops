# Combining the CNN/Daily Mail dataset
import pandas as pd

# Load each CSV file into a DataFrame
csv_file1 = "cnn_dailymail/test.csv"
csv_file2 = "cnn_dailymail/train.csv"
csv_file3 = "cnn_dailymail/validation.csv"

df_test = pd.read_csv(csv_file1)
df_train = pd.read_csv(csv_file2)
df_validation = pd.read_csv(csv_file3)

# Save each dataset to a separate Excel file
xlsx_file_path_test = "dataset/cnn_dataset_test.xlsx"
xlsx_file_path_train = "dataset/cnn_dataset_train.xlsx"
xlsx_file_path_validation = "dataset/cnn_dataset_validation.xlsx"

df_test.to_excel(xlsx_file_path_test, index=False, engine='openpyxl')
df_train.to_excel(xlsx_file_path_train, index=False, engine='openpyxl')
df_validation.to_excel(xlsx_file_path_validation, index=False, engine='openpyxl')
