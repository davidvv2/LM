# Maltese Language Model
This program creates a language model for the Maltese language. The Maltese Language is the native language of Malta, a european country. It is the only Semitic language that uses the lating alphabet.


The pre-processing section of this project is tailor made to extracts sentences from the MLRS Corpus (https://mlrs.research.um.edu.mt/).
These sentences are then converted into ngrams.

This language model has the functionality to predict the probability of a given sentence to occur, as well as being able to predict the next word given a string of text. It is also able to deal with unknown words as words that occur only once are replaced with a unk_token, which is meant to represent an unknown word. The size of the ngrams can be adjusted when declaring an object of class ngram.
