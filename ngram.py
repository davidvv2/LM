class NGram:
    def __init__(self):
        self.LM = {}
        self.count = 0
        self.n = 1

    def populate(self, sentences, n=1):
        count = 0
        for sentence in sentences:
            words = sentence.split()
            sentence_length = len(words)
            self.count += sentence_length  # -2 to negate the end and start of sentence tags




