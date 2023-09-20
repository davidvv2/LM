import ngram
import functions

sentences = functions.extract_sentences()
unk_sentences = functions.convert_unk_sentences(sentences)

unk_unigram = ngram.NGram()
unk_unigram.populate(unk_sentences)
functions.save("./Models/unigram.pickle", unk_unigram)

unk_bigram = ngram.NGram(n=2)
unk_bigram.populate(unk_sentences)
functions.save("./Models/bigram.pickle", unk_bigram)

unk_trigram = ngram.NGram(n=3)
unk_trigram.populate(unk_sentences)
functions.save("./Models/trigram.pickle", unk_trigram)

unigram = functions.load("./Models/unigram.pickle")
bigram = functions.load("./Models/bigram.pickle")
trigram = functions.load("./Models/trigram.pickle")

sentence = "li nidħlu fl- ewro"
print(unigram.predict_next_word(sentence))
print(bigram.predict_next_word(sentence))
print(trigram.predict_next_word(sentence))
