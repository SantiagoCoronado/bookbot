def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def word_count(file):
    return len(get_book_text(file).split())

def char_count(book):
    dict = {}
    for word in book.split():
        for char in word.lower():
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
    return dict

def sort_on(item):
    return item["num"]

def sorting(dict):
    list = []
    for key in dict:
        list.append({"char": key, "num": dict[key]})
    list.sort(reverse=True, key=sort_on)
    for item in list:
        print(f"{item['char']}: {item['num']}")
    return list