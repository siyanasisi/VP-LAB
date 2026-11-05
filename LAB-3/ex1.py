import string 
from collections import Counter

def clean_text(text):
    text = text.lower()

    for i in string.punctuation:
        text = text.replace(i, "")

    return text

def analyze_text(text):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    total_words = len(words)
    unique_words = len(set(words))

    if total_words == 0:
        av_len = 0
        most_common_word = None
    else:
        av_len = int(sum(len(word) for word in words) / total_words)
        most_common_word = Counter(words).most_common(3)

    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "average_word_length": av_len,
        "most_common_words": most_common_word
    }

text = "This is a very very long and boring text. Its very long and boring. It is very boring."
print(analyze_text(text))