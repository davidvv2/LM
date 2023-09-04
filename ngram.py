import methods


class NGram:
    def __init__(self):
        self.LM = {}  # a dictionary used to save the language model
        self.count = 0  # stores the total amount of words in the Language Model
        self.n = 1  # use to store the size of the grams

    def populate(self, sentences, n=1):
        self.n = n
        for sentence in sentences:
            words = sentence.split()
            sentence_length = len(words)
            self.count += sentence_length
            methods.add(methods.generate_gram(sentence, n), self.LM)
