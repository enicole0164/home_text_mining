import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# Tokenize the text data into words
tokens = word_tokenize(website_text)

# Filter words related to 'house'
house_related_words = [word.lower() for word in tokens if 'house' in word.lower()]

# Count the frequency of each word
word_counts = Counter(house_related_words)

# Print the most common words related to 'house'
print("Most common words related to 'house':")
print(word_counts.most_common(10))  # Change the number to display more or fewer words
