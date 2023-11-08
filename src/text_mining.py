from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter

def analyze_text(text_data, target_word, context_window=20):
    # Tokenize the text data into words
    tokens = word_tokenize(text_data)

    # Remove stop words and apply stemming
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    filtered_words = [stemmer.stem(word.lower()) for word in tokens if word.lower() not in stop_words and word.isalpha()]

    print(filtered_words)

    # Find words used often with the target word within the specified context window
    target_word = stemmer.stem(target_word.lower())
    context_words = []
    for i, word in enumerate(filtered_words):
        if word == target_word:
            start_index = max(0, i - context_window)
            end_index = min(len(filtered_words), i + context_window + 1)
            context_words.extend(filtered_words[start_index:i] + filtered_words[i + 1:end_index])

    # print(context_words)

    # Count the frequency of context words
    word_counts = Counter(context_words).most_common(20)

    # Filter words frequently used with the target word
    # frequent_context_words = {word: count for word, count in word_counts.items() if count > 1}

    return word_counts

# Example usage
if __name__ == "__main__":
    text_data = "Your text data containing descriptions of houses, cozy and family-friendly environments, etc."
    target_word = "house"
    context_window = 5  # Specify the context window size

    frequent_context_words = analyze_text(text_data, target_word, context_window)

    # Print words frequently used with the target word
    print(f"Words frequently used with '{target_word}':")
    print(frequent_context_words)
