
def add_prefix_un(word):
    return "un"+word
def make_word_groups(vocab_words):
    pre = vocab_words[0]
    return f" :: {pre}".join(vocab_words)
def remove_suffix_ness(word):
    s = word[:-4]
    if s[-1].lower()=="i":
        return s[:-1]+"y"
    else:
        return s
def adjective_to_verb(sentence, index):
    s = sentence.split()[index]
    return s.strip(".")+"en"