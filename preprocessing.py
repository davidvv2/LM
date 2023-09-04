import glob
import random
import time
import ngram

# extracts all the sentences from the MLRS Corpus
def convert():
    path = "./Corpus"
    sentence = "<s>"
    sentences = []
    text_files = glob.glob(path + "/*.txt")
    if len(text_files) == 0:
        print("ERROR NO CORPUS FOUND!!!\nEXITING...")
        return
    print("loading corpus...")

    for file in text_files:
        for line in open(file, 'rt', encoding='utf8'):
            if line[:3] == '</s':
                sentence += " </s>"
                sentences.append(sentence)
                sentence = "<s>"
            elif line[:1] == '<':
                continue
            else:
                list = line.split('\t')
                sentence += " " + list[0].lower()

        print("finished scanning file: " + file)
    print("Finished loading Corpus")
    return sentences


if __name__ == '__main__':
    st = time.time()
    sentences = convert()

    # separates the dictionary of sentences into a training and testing set, using
    # a simple shuffle of sentences and segmentation of list with 80% being used for the
    # training set and 20% for the testing set.
    random.shuffle(sentences)
    training_sentences = sentences[:round(len(sentences) * 0.8)]
    testing_sentences = sentences[round(len(sentences) * 0.8):]

    # saves the training and testing set as separate text files, where each line is a sentence
    print("Saving data sets...")
    f1 = open("training_sentences.txt", "w", encoding='utf8')
    for s in training_sentences:
        f1.write(s + " \n")
    f1.close()
    print("Finished saving training set")
    f2 = open("testing_sentences.txt", "w", encoding='utf8')
    for s in testing_sentences:
        f2.write(s + " \n")
    f2.close()
    print("Finished saving test set")
    print("%.2f" % (time.time() - st))

