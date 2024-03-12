import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

# Load datasets
train = pd.read_excel('D:/Capstone_Project/dataset/train_dataset.xlsx')
test = pd.read_excel('D:/Capstone_Project/dataset/test_dataset.xlsx')
validation = pd.read_excel('D:/Capstone_Project/dataset/validation_dataset.xlsx')

# Text cleaning function
def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text.lower())
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [word for word in words if word.isalnum() and word not in stop_words]
    return ' '.join(words)

# Apply text cleaning to 'article' and 'summary' columns
train['cleaned_article'] = train['article'].apply(clean_text)
train['cleaned_summary'] = train['summary'].apply(clean_text)

test['cleaned_article'] = test['article'].apply(clean_text)
test['cleaned_summary'] = test['summary'].apply(clean_text)

validation['cleaned_article'] = validation['article'].apply(clean_text)
validation['cleaned_summary'] = validation['summary'].apply(clean_text)

# Combine 'cleaned_article' and 'cleaned_summary' for creating a common vocabulary
all_text = test['cleaned_article'].tolist() + test['cleaned_summary'].tolist()

# Tokenize and create a vocabulary with a limit on the number of words
vocab_size = 10000
tokenizer = Tokenizer(num_words=vocab_size, oov_token="<OOV>")
tokenizer.fit_on_texts(all_text)

# Tokenize and pad sequences for 'cleaned_article'
train_article_sequences = tokenizer.texts_to_sequences(train['cleaned_article'])
train_padded_article_sequences = pad_sequences(train_article_sequences, padding='post')

# Tokenize and pad sequences for 'cleaned_summary'
train_summary_sequences = tokenizer.texts_to_sequences(train['cleaned_summary'])
train_padded_summary_sequences = pad_sequences(train_summary_sequences, padding='post')

# Repeat similar steps for test and validation datasets

# Displaying the tokenized and padded sequences
print(train_padded_article_sequences[:5])
print(train_padded_summary_sequences[:5])
