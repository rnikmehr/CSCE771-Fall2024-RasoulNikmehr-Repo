
# Based on https://machinelearningmastery.com/develop-word-embeddings-python-gensim/
# Import
from gensim.models import Word2Vec

corpus = [
['An', 'alpha', 'document', '.'],
['A', 'beta', 'document', '.'],
['Guten', 'Morgen', '!'],
['Gamma', 'manuscript', 'is', 'old', '.'],
['Whither', 'my', 'document', '?']
]

# train model
# Setting min_count to 1 to ensure all words are considered, even if they appear only once.
model = Word2Vec(corpus, min_count=1)
# summarize the loaded model
print("INFO: Model - \n" + str(model))

# summarize vocabulary
# Use model.wv.key_to_index to get the vocabulary
words = list(model.wv.key_to_index)
print("INFO: Words found - \n" + str(words))

# access vector for one word - specified by myword
myword = 'document'
# Use model.wv to access word vectors
# Checking if the word exists in the vocabulary before accessing its vector
if myword in model.wv:
    print("INFO: Model of '" + myword + "' - \n" + str(model.wv[myword]))
else:
    print(f"INFO: The word '{myword}' is not present in the model's vocabulary.")

import os

# ... your existing code ...

# Create the 'data' directory if it doesn't exist
os.makedirs('../data', exist_ok=True)

# save model
model.save('../data/model.bin')
model.wv.save_word2vec_format('../data/model.txt', binary=False)

# load model
new_model = Word2Vec.load('../data/model.bin')
print("INFO: Reloaded Model - \n" + str(new_model))
