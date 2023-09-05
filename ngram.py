import methods
UNK = "<UNK>"

class NGram:
    def __init__(self, n=1):
        self.LM = {}  # a dictionary used to save the language model
        self.LM_1 = {}  # a dictionary used to store a language model using n-1 grams
        self.count = 0  # stores the total amount of grams in the Language Model
        self.n = n  # use to store the size of the grams

    def populate(self, sentences):
        for sentence in sentences:
            grams = methods.generate_gram(sentence, self.n)
            self.count += len(grams)
            for gram in grams:
                methods.add(gram, self.LM)

            # populates the n-1_gram model to be used in the probability method
            if self.n-1 > 0:
                for gram in methods.generate_gram(sentence, self.n-1):
                    methods.add(gram, self.LM_1)

    def sentence_probability(self, sentence):
        grams = methods.generate_gram(sentence, self.n)
        p = 0

        if grams:
            for gram in grams:
                current_path = self.LM
                if self.n != 1:
                    second_current_path = self.LM_1

                    for i in range(0, len(gram)):
                        word = gram[i]
                        pre_word = gram[i-1] if i > 0 else None

                        if word in current_path:
                            current_path = current_path[word]

                            if pre_word and pre_word in second_current_path:
                                second_current_path = second_current_path[pre_word]
                            elif pre_word and UNK in second_current_path:
                                second_current_path = second_current_path[UNK]

                        elif UNK in current_path:
                            current_path = current_path[UNK]

                            if pre_word and pre_word in second_current_path:
                                second_current_path = second_current_path[pre_word]
                            elif pre_word and UNK in second_current_path:
                                second_current_path = second_current_path[UNK]

                        else:
                            return 0

                    p *= current_path/second_current_path
                # unigram probability
                else:
                    for i in range(0, len(gram)):
                        word = gram[i]
                        pre_word = gram[i - 1] if i > 0 else None

                        if word in current_path:
                            current_path = current_path[word]

                        elif UNK in current_path:
                            current_path = current_path[UNK]
                        else:
                            return 0

                    p *= current_path / self.count

        return p
