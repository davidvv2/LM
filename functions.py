import pickle
import glob
import ngram


# extracts all the sentences from the MLRS Corpus
def extract_sentences():
    path = "./Corpus"
    _sentence = "<s>"
    _sentences = []
    text_files = glob.glob(path + "/*.txt")
    if len(text_files) == 0:
        print("ERROR NO CORPUS FOUND!!!\nEXITING...")
        return
    print("loading corpus...")

    for file in text_files:
        for line in open(file, 'rt', encoding='utf8'):
            if line[:3] == '</s':
                _sentence += " </s>"
                _sentences.append(_sentence)
                _sentence = "<s>"
            elif line[:1] == '<':
                continue
            else:
                list = line.split('\t')
                _sentence += " " + list[0].lower()

        print("finished scanning file: " + file)
    print("Finished loading Corpus")
    return _sentences


def convert_unk_sentences(sentences):
    unigram = ngram.NGram()
    unigram.populate(sentences)

    unk_sentences = []

    counter = 0
    for sentence in sentences:
        unk_sentence = ""
        for word in sentence.split():
            counter += 1
            # if a word only occurs once in our data set replace it with an unk token
            # in our corpus of sentences
            if unigram.LM[word] == 1:
                unk_sentence += "<UNK> "
            else:
                unk_sentence += word + " "

        unk_sentences.append(unk_sentence)
    return unk_sentences


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

        for i in range(pos, pos + n):
            ngram.append(words[i])

        ngrams.append(ngram)
        pos += 1
    return ngrams


def save(path, model):
    f = open(path, "wb")
    pickle.dump(model, f)
    f.close()


def load(path):
    try:
        f = open(path, "rb")
        return pickle.load(f)
    except:
        return None
