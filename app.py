import streamlit as st
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')   # Downloads list of stopwords

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is a basic example to understand stopword removal."

# Tokenize
words = word_tokenize(text)

# Remove stopwords
filtered_words = [w for w in words if w.lower() not in stopwords.words('english')]

st.write("Filtered:", filtered_words)