import glob
from lxml import etree

def get_tokens(path_to_doc):
    return etree.parse(path_to_doc).findall("xdrs/taggedtokens/tagtoken")

def get_token_pos(token_element):
    tags = token_element.find('tags')
    tag_dict = {}
    for tag in tags:
        tag_dict[tag.get("type")] = tag.text
    return tag_dict['tok'], tag_dict['pos']

def get_doc_text(path_to_doc):
    etree.parse(path_to_doc)
    taggedtokens = etree.parse(path_to_doc).findall("xdrs/taggedtokens/tagtoken")
    tokens = []
    for tagtoken in taggedtokens:
        for tag in tagtoken.find("tags"):
            if tag.get("type") == "tok":
                tokens.append(tag.text)
    return " ".join(tokens)


def sort_docs(path_pmb):
    files = glob.glob(path_pmb + "/**/*.xml", recursive=True)
    language_doc_dict = {}
    for file in files:
        lang = file.split("/")[-1].split(".")[0]
        doc = "/".join(file.split("/")[:-1])
        if lang not in language_doc_dict:
            language_doc_dict[lang] = set()
        language_doc_dict[lang].add(doc)
    return language_doc_dict


def get_pairs(language_list):
    """Given a list, return a list of tuples of all element pairs."""
    pairs = []
    for l1 in language_list:
        for l2 in language_list:
            if l1 != l2:
                if (l1, l2) not in pairs and (l2, l1) not in pairs:
                    pairs.append((l1, l2))
    return pairs
