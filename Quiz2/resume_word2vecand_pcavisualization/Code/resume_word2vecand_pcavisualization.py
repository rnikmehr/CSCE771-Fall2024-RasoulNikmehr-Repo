# Import necessary libraries
from gensim.models import Word2Vec
import PyPDF2
import re
from gensim.utils import simple_preprocess
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
plt.scatter(result[:, 0], result[:, 1])
for i, word in enumerate(words):
    plt.annotate(word, xy=(result[i, 0], result[i, 1]))
plt.title("Word Embeddings Visualization")

# Save the figure before showing it
plt.savefig('word_embeddings.png')  # Specify the desired filename and format

plt.show()

# Function to read PDF
def read_pdf(pdf_path='/content/Rasoul_Nikmehr_Resume.pdf'):
    with open('/content/Rasoul_Nikmehr_Resume.pdf', 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
    return text

# Preprocess the text
def preprocess(text):
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokenize and lowercase
    return simple_preprocess(text, deacc=True)

# Read and preprocess the resume
resume_text = read_pdf('/content/Rasoul_Nikmehr_Resume.pdf')
corpus = [preprocess(resume_text)]

# Train model
model = Word2Vec(corpus, min_count=1)

# Summarize the loaded model
print("INFO: Model - \n" + str(model))

# Summarize vocabulary
words = list(model.wv.key_to_index.keys())
print("INFO: Words found - \n" + str(words))

# Access vector for one word
myword = 'experience'  # Change this to a word you expect to be in your resume
if myword in model.wv:
    print(f"INFO: Model of '{myword}' - \n" + str(model.wv[myword]))
else:
    print(f"INFO: '{myword}' not found in the model vocabulary.")

# Load model
new_model = Word2Vec.load('resume_model.bin')
print("INFO: Reloaded Model - \n" + str(new_model))

# Visualize the embedding using PCA
words = list(model.wv.key_to_index.keys())
vectors = [model.wv[word] for word in words]

pca = PCA(n_components=2)
result = pca.fit_transform(vectors)

plt.figure(figsize=(12, 8))
plt.scatter(result[:, 0], result[:, 1])
for i, word in enumerate(words):
    plt.annotate(word, xy=(result[i, 0], result[i, 1]))
plt.title("Word Embeddings Visualization")
plt.show()
plt.savefig('word_embeddings.png').
