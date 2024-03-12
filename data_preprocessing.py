import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker

train = pd.read_excel('untouched_dataset/train_dataset.xlsx')
test = pd.read_excel('untouched_dataset/test_dataset.xlsx')
validation = pd.read_excel('untouched_dataset/validation_dataset.xlsx')


# Function for text cleaning
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


# Function for Spelling correction
def correct_spelling_in_dataset(dataset):
    # Create a SpellChecker instance
    spell = SpellChecker()

    # Iterate over each sample in the dataset
    for sample in dataset:
        # Correct spelling in 'article' text
        article = sample['article']
        # Tokenize the article into words
        words = article.split()
        # Identify misspelled words
        misspelled = spell.unknown(words)
        # Correct misspelled words
        corrected_article = [spell.correction(word) if word in misspelled else word for word in words]
        # Join the corrected words back into a string
        sample['article'] = ' '.join(corrected_article)

        # Correct spelling in 'summary' text
        summary = sample['summary']
        # Tokenize the summary into words
        words = summary.split()
        # Identify misspelled words
        misspelled = spell.unknown(words)
        # Correct misspelled words
        corrected_summary = [spell.correction(word) if word in misspelled else word for word in words]
        # Join the corrected words back into a string
        sample['summary'] = ' '.join(corrected_summary)

    return dataset


print("Starting to pre-process training dataset\n")

train['article'] = train['article'].apply(clean_text)
train['summary'] = train['summary'].apply(clean_text)
pre_processed_train = correct_spelling_in_dataset(train)
pre_processed_train.to_excel('Clean Dataset/train.xlsx')
print("Cleaned Dataset:", pre_processed_train, "\n=========")

test['article'] = test['article'].apply(clean_text)
test['summary'] = test['summary'].apply(clean_text)
pre_processed_test = correct_spelling_in_dataset(test)
pre_processed_test.to_excel('Clean Dataset/test.xlsx')

validation['cleaned_article'] = validation['article'].apply(clean_text)
validation['cleaned_summary'] = validation['summary'].apply(clean_text)
pre_processed_validation = correct_spelling_in_dataset(validation)
pre_processed_validation.to_excel('Clean Dataset/validation.xlsx')

print("DONE!!")
