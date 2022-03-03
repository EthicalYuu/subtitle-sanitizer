import pysubs2

def get_dict():
    word_replacement = {}
    with open("word_alt.txt", encoding='utf-8') as f:
        for line in f:
            (word, alt) = line.split()
            word_replacement[word] = alt
    return word_replacement

def purify(sub_line):
    pure_dict = get_dict()
    for word, initial in pure_dict.items():
        sub_line = sub_line.replace(word, initial)
    return sub_line

def replace_with_alt(filepath):
    subs = pysubs2.load(filepath, encoding="utf-8")
    for line in subs:
        line.text = purify(line.text)
    subs.save(filepath)
    print(filepath + "  successfuly purified")



