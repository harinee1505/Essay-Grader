from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
import re

nltk.download('punkt')
nltk.download('stopwords')

def grade_essay(essay):
    blob = TextBlob(essay)
    sentences = blob.sentences
    words = blob.words

    grammar_score = 1 - (len(blob.correct().words) - len(words)) / len(words)
    grammar_score = max(min(grammar_score, 1), 0)

    length_score = min(len(words) / 250, 1)

    stop_words = set(stopwords.words('english'))
    unique_words = len(set([word.lower() for word in words if word.lower() not in stop_words]))
    vocab_score = min(unique_words / 100, 1)

    total_score = (grammar_score * 0.4 + length_score * 0.3 + vocab_score * 0.3) * 100
    return round(total_score, 2)
