import string

def preprocess(text):
    text = ''.join(char for char in text.lower().strip().replace("\t", "") if char not in string.punctuation)
    return text.split(" ")
