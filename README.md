# NLP - Stopword Removal
### App Link
- https://nlp-stopword-removal.streamlit.app/
---
### What is Stopword Removal?
- **Stopwords** are common words like "**is**", "**the**", "**and**", "**in**", "**at**", etc.
- These words **don't carry important meaning** in most text analysis tasks.
- **Stopword removal** means removing such words from text before analysis.
- **Real-Life Example:-**

  If someone says:
  > "The product is very good and useful."

  After removing stopwords, the result becomes:
  > "product good useful"

  This helps focus on the **important words** for machine understanding.
---
### Why Remove Stopwords?
- To **reduce noise** in text data
- To **speed up** NLP models
- To **focus on keywords** only
- Used in **sentiment analysis**, **classification**, **topic modeling**, etc.
---
### Required Python Packages
- **`nltk`**
- **`streamlit`**
---
### Output of the Code
`Filtered: ['basic', 'example', 'understand', 'stopword', 'removal', '.']`
- The common words like "**this**", "**is**", "**a**", "**to**" are removed.
---
### Some Curious Points
- Stopwords vary **based on language**.
- We can customize **our own stopword list**.
- Some NLP tasks (like translation) **prefer keeping stopwords**.
---
