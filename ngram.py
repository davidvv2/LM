import functions
from collections import OrderedDict
UNK = "<UNK>"


class NGram:
    def __init__(self, n=1):
        self.LM = {}  # a dictionary used to save the language model
        self.LM_1 = {}  # a dictionary used to store a language model using n-1 grams
        self.count = 0  # stores the total amount of grams in the Language Model
        self.n = n  # use to store the size of the grams

    def populate(self, sentences):
        for sentence in sentences:
            grams = functions.generate_gram(sentence, self.n)
            self.count += len(grams)
            for gram in grams:
                functions.add(gram, self.LM)

            # populates the n-1_gram model to be used in the probability method
            if self.n-1 > 0:
                for gram in functions.generate_gram(sentence, self.n-1):
                    functions.add(gram, self.LM_1)

    def sentence_probability(self, sentence):
        grams = functions.generate_gram(sentence, self.n)
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

                        if word in current_path:
                            current_path = current_path[word]

                        elif UNK in current_path:
                            current_path = current_path[UNK]
                        else:
                            return 0

                    p *= current_path / self.count

        return p

    def predict_next_word(self, sentence):
        words = sentence.split()
        if len(words) < self.n-1:
            return None

        last_words = words[len(words)-self.n+1:]
        current_pos = self.LM

        for word in last_words:
            if word in current_pos:
                current_pos = current_pos[word]
            elif UNK in current_pos:
                current_pos = current_pos[UNK]
            else:
                return None

        sorted_values = OrderedDict(sorted(current_pos, reverse=True))

        for key, _ in sorted_values:
            if key == "<s>" or key == "</s>" or key == UNK:
                continue
            return key
