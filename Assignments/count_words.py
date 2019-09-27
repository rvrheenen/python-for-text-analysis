from utils_3a import preprocess

def count(text):
    words = preprocess(text)
    return {word:words.count(word) for word in set(words)}

print(count("this is a (tricky) test, is this?"))
