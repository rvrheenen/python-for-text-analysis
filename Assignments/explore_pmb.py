from utils import *

path_pmb = 'PMB/pmb-2.1.0/data/gold'
language_doc_dict = sort_docs(path_pmb)
languages = list(language_doc_dict.keys())

for language in languages:
    n_docs = len(language_doc_dict[language])
    docs = language_doc_dict[language]
    n_tokens = sum( [len(get_tokens(f'{doc}/{language}.drs.xml')) for doc in list(docs)] )
    print(f'{language}: num docs: {len(docs)}, num tokens: {n_tokens}')


for language_1, language_2 in get_pairs(languages):
    print(f"Coverage for parallel data in {language_1} and {language_2}: {len(language_doc_dict[language_1].intersection(language_doc_dict[language_2]))}")

# Unsure what was intended with "print the documents in both lanugages" so I went for the path
# If the intention was the document text, see the commented line.
langs = input("Please enter two languages by their abbreviations. EG: en it ").strip().split()
for doc in language_doc_dict[langs[0]].intersection(language_doc_dict[langs[1]]):
    for lang in langs:
        print(f"[{lang}]: {f'{doc}/{lang}.drs.xml'}")
        # print(f"[{lang}]: {get_doc_text(f'{doc}/{lang}.drs.xml')}")
    if input("Do you want to continue? [yes(or anything else)/no]: ") == "no" :
        break


uniq_docs = set()
shared_docs = set()
total_docs = list()
for language in languages:
    new_docs = language_doc_dict[language]
    uniq_docs = uniq_docs.union(new_docs)
    if len(shared_docs) == 0:
        shared_docs = new_docs
    else:
        shared_docs = shared_docs.intersection(new_docs)
    total_docs += list(new_docs)
print(f'''There are {len(uniq_docs)} different documents across all the languages,
there are {len(shared_docs)} documents that occur in all languages and there are {len(total_docs)} total documents.''')
