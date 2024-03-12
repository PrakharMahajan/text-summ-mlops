import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# train = pd.read_excel('D:/Capstone_Project/dataset/train_dataset.xlsx')
test = pd.read_excel('D:/Capstone_Project/dataset/test_dataset.xlsx')
# validation = pd.read_excel('D:/Capstone_Project/dataset/validation_dataset.xlsx')

# STEP 1 - TEXT CLEANING
print("text cleanin\n\n")
def clean_text(text):
    # Check if the text is not empty
    if pd.isnull(text):
        return ''

    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9]', ' ', str(text))

    # Convert to lowercase
    text = text.lower()

    # Tokenize and remove stop words
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [word for word in words if word.isalnum() and word not in stop_words]

    # Join the cleaned words
    cleaned_text = ' '.join(words)

    return cleaned_text


test['cleaned_article'] = test['article'].apply(clean_text)
test['cleaned_summary'] = test['summary'].apply(clean_text)

# test['cleaned_article'] = test['article'].apply(clean_text)
# test['cleaned_summary'] = test['summary'].apply(clean_text)
#
# validation['cleaned_article'] = validation['article'].apply(clean_text)
# validation['cleaned_summary'] = validation['summary'].apply(clean_text)

print(test[['cleaned_article', 'cleaned_summary']])

# STEP 2 - TOKENIZATION
print("tokenization \n\n")

from nltk.tokenize import word_tokenize

def tokenize_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    return tokens

test['tokenized_article'] = test['cleaned_article'].apply(tokenize_text)
test['tokenized_summary'] = test['cleaned_summary'].apply(tokenize_text)

# test['tokenized_article'] = test['cleaned_article'].apply(clean_text)
# test['tokenized_summary'] = test['cleaned_summary'].apply(clean_text)
#
# validation['tokenized_article'] = validation['cleaned_article'].apply(clean_text)
# validation['tokenized_summary'] = validation['cleaned_summary'].apply(clean_text)

print(test[['tokenized_article', 'tokenized_summary']])

# STEP 3 - STOPWORDS REMOVAl
print("stopping removal \n\n")

from nltk.corpus import stopwords

def remove_stopwords(tokens):
    # Remove stopwords from the list of tokens
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens

# Apply stopword removal to 'tokenized_article' and 'tokenized_summary' columns
test['filtered_article'] = test['tokenized_article'].apply(remove_stopwords)
test['filtered_summary'] = test['tokenized_summary'].apply(remove_stopwords)

# Display the data with stopwords removed
print(test[['filtered_article', 'filtered_summary']])

# # STEP 4- PADDING / TRUNCATION
# print("padding/truncation \n\n")
#
# from tensorflow.keras.preprocessing.sequence import pad_sequences
#
# def pad_sequences_data(sequences, max_length):
#     # Pad sequences to a specified maximum length
#     padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post', truncating='post')
#     return padded_sequences
#
# # Set the maximum length for padding
# max_length = 50  # Adjust as needed
#
# # Apply padding to 'filtered_article' and 'filtered_summary' columns
# test['padded_article'] = test['filtered_article'].apply(lambda x: pad_sequences_data([x], max_length)[0])
# test['padded_summary'] = test['filtered_summary'].apply(lambda x: pad_sequences_data([x], max_length)[0])
#
# # Display the data with padding applied
# print(test[['padded_article', 'padded_summary']])

# STEP 5 - VOCAB CReation
print("vocab \n\n")

def create_vocabulary(data_column):
    # Flatten the list of lists and extract unique tokens
    flat_tokens = [token for tokens_list in data_column for token in tokens_list]
    vocabulary = set(flat_tokens)
    return vocabulary

# Extract vocabulary from 'filtered_article' and 'filtered_summary' columns
article_vocabulary = create_vocabulary(test['filtered_article'])
summary_vocabulary = create_vocabulary(test['filtered_summary'])

# Display the vocabularies
print("Article Vocabulary:", article_vocabulary)
print("Summary Vocabulary:", summary_vocabulary)
