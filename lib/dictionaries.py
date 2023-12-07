import string

def word_frequency(sentence):
    word_count = {}
    translator = str.maketrans("", "", string.punctuation)

    for word in sentence.lower().translate(translator).split():
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


# Test the function
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
