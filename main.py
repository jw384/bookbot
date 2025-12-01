import sys

from stats import get_num_words , get_dict , get_list_of_dicts

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    s = get_book_text(sys.argv[1])
    w = get_num_words(s)
    print(f"Found {w} total words")
    d = (get_dict(s))
    #print(d)
    ld = get_list_of_dicts(d)

    for d in ld:
        if d["name"].isalpha():
            print(f"{d["name"]}: {d["num"]}")
        



main()


