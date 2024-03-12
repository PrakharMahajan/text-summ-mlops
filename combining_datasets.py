import pandas as pd

# Combining testing data

cnn_test = pd.read_excel('dataset/cnn_dataset_test.xlsx')
xsum_test = pd.read_excel('dataset/xsum_dataset_test.xlsx')

cnn_test = cnn_test.rename(columns={'highlights': 'summary'})
xsum_test = xsum_test.rename(columns={'document': 'article'})

cnn_test['id'] = cnn_test['id'].astype(str)
xsum_test['id'] = xsum_test['id'].astype(str)

test_data = pd.concat([cnn_test, xsum_test])
test_data.to_excel('dataset/test_dataset.xlsx')

# Combining training data

cnn_train = pd.read_excel('dataset/cnn_dataset_train.xlsx')
xsum_train = pd.read_excel('dataset/xsum_dataset_train.xlsx')

cnn_train = cnn_train.rename(columns={'highlights': 'summary'})
xsum_train = xsum_train.rename(columns={'document': 'article'})

cnn_train['id'] = cnn_train['id'].astype(str)
xsum_train['id'] = xsum_train['id'].astype(str)

train_data = pd.concat([cnn_train, xsum_train])
train_data.to_excel('dataset/train_dataset.xlsx')

# Combining validation data

cnn_val = pd.read_excel('dataset/cnn_dataset_validation.xlsx')
xsum_val = pd.read_excel('dataset/xsum_dataset_validation.xlsx')

cnn_val = cnn_val.rename(columns={'highlights': 'summary'})
xsum_val = xsum_val.rename(columns={'document': 'article'})

cnn_val['id'] = cnn_val['id'].astype(str)
xsum_val['id'] = xsum_val['id'].astype(str)

val_data = pd.concat([cnn_val, xsum_val])
val_data.to_excel('dataset/validation_dataset.xlsx')
