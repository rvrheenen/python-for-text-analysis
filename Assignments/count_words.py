from utils_3a import preprocess

def count(text):
    words = preprocess(text)
    return {word:words.count(word) for word in set(words)}
