import glob
import time
import ngram
import functions


# extracts all the sentences from the MLRS Corpus
def convert():
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


if __name__ == '__main__':
    st = time.time()

    sentences = convert()
    unk_sentences = []

    unigram = ngram.NGram()
    unigram.populate(sentences)

    for sentence in sentences:
        unk_sentence = ""
        for word in sentence.split():
            # if a word only occurs once in our data set replace it with an unk token
            # in our corpus of sentences
            if unigram.LM[word] == 1:
                unk_sentence += "<UNK> "
            else:
                unk_sentence += word + " "

        unk_sentences.append(unk_sentence)

    unk_unigram = ngram.NGram()
    unk_unigram.populate(unk_sentences)
    functions.save("./Models/unigram.pickle", unk_unigram)

    unk_bigram = ngram.NGram(n=2)
    unk_bigram.populate(unk_sentences)
    functions.save("./Models/bigram.pickle", unk_bigram)

    unk_trigram = ngram.NGram(n=3)
    unk_trigram.populate(unk_sentences)
    functions.save("./Models/trigram.pickle", unk_trigram)
