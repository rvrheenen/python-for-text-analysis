import glob
import os
from nltk import sent_tokenize, word_tokenize

def get_paths(input_folder):
    return glob.glob(os.path.join(input_folder, '*.txt'))


def get_basic_stats(txt_path):
    with open(txt_path, 'r') as f:
        text = f.read()

    chapter_act_keyword = {
        "HuckFinn": "CHAPTER",
        "AnnaKarenina": "Chapter ",
        "Macbeth": "ACT"
    }

    tokens = word_tokenize(text)
    word_count = {token:tokens.count(token) for token in set(tokens)}

    return {
        "num_sents": len(sent_tokenize(text)),
        "num_tokens": len(tokens),
        "vocab_size": len(set(tokens)), # It says nowhere to remove punctuation..
        "num_chapters_or_acts": text.count(chapter_act_keyword[os.path.basename(txt_path).strip(".txt")]),
        "top_20_tokens": sorted(word_count, key=word_count.get, reverse=True)[:20]
    }
