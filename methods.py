import pickle


def add(gram, dictionary):
    counter = 0
    current_dictionary = dictionary
    in_dictionary = True

    for word in gram:
        if word in current_dictionary:
            if counter + 1 < len(gram):
                current_dictionary = current_dictionary[word]
            counter += 1
        else:
            in_dictionary = False

    # if gram is in our dictionary increment value
    if in_dictionary:
        current_dictionary[gram[-1]] += 1
    # if gram is not in dictionary then add it to our dictionary and increment it by 1
    else:
        for i in range(counter, len(gram)):
            # if we are not at the end of our gram, then add a new dimension in our
            # dictionary to the current point we are at in our dictionary traversal
            if i + 1 < len(gram):
                current_dictionary[gram[i]] = {}
                current_dictionary = current_dictionary[gram[i]]
            # if we reached the end of our gram, then add the last value of our gram
            # as a key and initialize the value to 1
            else:
                current_dictionary[gram[i]] = 1


def generate_gram(sentence, n):

    words = sentence.split()
    pos = 0
    ngrams = []

    while pos + n <= len(words):
        ngram = []

        for i in range(pos, pos+n):
            ngram.append(words[i])

        ngrams.append(ngram)
        pos += 1
    return ngrams


def save(path, model):
    f
