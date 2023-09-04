import glob
import random
import time
import ngram


# extracts all the sentences from the MLRS Corpus
def convert():
    path = "./Corpus"
    sentence = "<s>"
    _sentences = []
    text_files = glob.glob(path + "/*.txt")
    if len(text_files) == 0:
        print("ERROR NO CORPUS FOUND!!!\nEXITING...")
        return
    print("loading corpus...")

    for file in text_files:
        for line in open(file, 'rt', encoding='utf8'):
            if line[:3] == '</s':
                sentence += " </s>"
                _sentences.append(sentence)
                sentence = "<s>"
            elif line[:1] == '<':
                continue
            else:
                list = line.split('\t')
                sentence += " " + list[0].lower()

        print("finished scanning file: " + file)
    print("Finished loading Corpus")
    return _sentences


if __name__ == '__main__':
    st = time.time()

    sentences = convert()
    unk_sentences = []

    unigram = ngram.NGram()
    unigram.populate(sentences, 1)

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
