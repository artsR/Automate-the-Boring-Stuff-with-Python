def make_string(words):
    name =''
    length = len(words)
    for i in range(length) :
        if i == length - 1 :
            name += 'and ' + words[i]
        else:
            name += words[i] + ', '
    return name

spam = ['apples', 'bananas', 'tofu', 'cats']

sentence = make_string(spam)
print(sentence)
