## Based on
# - [1] https://medium.com/analytics-vidhya/basics-of-using-pre-trained-glove-vectors-in-python-d38905f356db
# - [2] https://machinelearningmastery.com/develop-word-embeddings-python-gensim/
# - [3] Glove site: https://nlp.stanford.edu/projects/glove/

# Install as necessary
# !pip install numpy
# !pip install scipy
# !pip install matplotlib
# !pip install sklearn

# Necessary imports
import numpy as np
from sklearn.manifold import TSNE

# Copy data from: https://nlp.stanford.edu/data/glove.6B.zip
# Unzip and use file glove.6B.50d.txt; set the data path accordingly
# Replace 'path/to/glove.6B.50d.txt' with the actual path to your file
glove_input_file = '/content/glove.6B.50d.txt'

# Path 1
embeddings_dict = {}
with open(glove_input_file, 'r') as f:
    for line in f:
        values = line.split()
        word = values[0]
        # Wrap vector creation in a try-except to handle invalid lines
        try:
            vector = np.asarray(values[1:], "float32")
            # Check if the vector has the correct dimension (50 in this case)
            if vector.shape[0] == 50:
                embeddings_dict[word] = vector
            else:
                print(f"Skipping word '{word}' due to incorrect vector dimension: {vector.shape}")
        except ValueError:
            print(f"Skipping word '{word}' due to invalid vector values")

# A function defined for similarity
# - See description of euclidean use in [1]
def find_closest_embeddings(embedding):
    return sorted(embeddings_dict.keys(), key=lambda word: spatial.distance.euclidean(embeddings_dict[word], embedding))

# Find closest word
find_closest_embeddings(embeddings_dict["king"])[:5]

# Vector operation
print(find_closest_embeddings(
    embeddings_dict["twig"] - embeddings_dict["branch"] + embeddings_dict["hand"]
)[:5])

# For visualizing
tsne = TSNE(n_components=2, random_state=0)

# Organizing data structures
words = list(embeddings_dict.keys())
vectors = [embeddings_dict[word] for word in words]

# Convert the list of arrays to a 2D NumPy array
vectors_array = np.array(vectors)  # Convert 'vectors' to a NumPy array

Y = tsne.fit_transform(vectors_array[:50]) # Use the NumPy array for fit_transform

plt.scatter(Y[:, 0], Y[:, 1])

for label, x, y in zip(words, Y[:, 0], Y[:, 1]):
    plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords="offset points")
plt.show()

import os

# We can work with Glove or convert it to word2vec

# Path 2
from gensim.scripts.glove2word2vec import glove2word2vec
word2vec_output_file = '/content/data/word2vec.txt'
os.makedirs(os.path.dirname(word2vec_output_file), exist_ok=True)

glove2word2vec(glove_input_file, word2vec_output_file)
print("INFO: file converted and saved to - " + word2vec_output_file)

from gensim.models import KeyedVectors

# load the Stanford GloVe model
filename = 'data/word2vec.txt'
model = KeyedVectors.load_word2vec_format(filename, binary=False)

# calculate: (king - man) + woman = ?
result = model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
print(result)

# Vector operation on glove
print(find_closest_embeddings(
    embeddings_dict["woman"] - embeddings_dict["man"] + embeddings_dict["king"]
)[:5])
