from utils import get_paths, get_basic_stats
import os

def main():
    book_paths = get_paths('../Data/books')
    book2stats = {}
    for book_path in book_paths:
        stats = get_basic_stats(book_path)
        book = os.path.basename(book_path).strip('.txt')
        print(book, stats)
        book2stats[book] = stats
        with open(f'top_20_{book}.txt', 'w') as f:
            f.write("\n".join(stats['top_20_tokens']))

    stats2book_with_highest_value = {
        "num_sents": max(book2stats, key=lambda book: book2stats[book]["num_sents"]),
        "num_tokens": max(book2stats, key=lambda book: book2stats[book]["num_tokens"]),
        "vocab_size": max(book2stats, key=lambda book: book2stats[book]["vocab_size"]),
        "num_chapters_or_acts": max(book2stats, key=lambda book: book2stats[book]["num_chapters_or_acts"]),
    }
    print(stats2book_with_highest_value)


if __name__ == '__main__':
    main()
