
from keras.models import Sequential
from keras.layers import LSTM, Dense, RepeatVector, TimeDistributed, Input

# Define input sequence
seq_in = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

# Convert characters to integers
char_to_int = dict((c, i) for i, c in enumerate(seq_in))
int_to_char = dict((i, c) for i, c in enumerate(seq_in))

# Convert input sequence to integers
seq_in_int = np.array([char_to_int[char] for char in seq_in])

# Reshape input into [samples, timesteps, features]
n_in = len(seq_in_int)
seq_in_int = seq_in_int.reshape((1, n_in, 1))

# Prepare output sequence
seq_out = seq_in_int[:, 1:, :]
n_out = n_in - 1

# Define model
model = Sequential([
    Input(shape=(n_in, 1)),
    LSTM(100, activation='relu'),
    RepeatVector(n_out),
    LSTM(100, activation='relu', return_sequences=True),
    TimeDistributed(Dense(1))
])

model.compile(optimizer='adam', loss='mse')

# Fit model
model.fit(seq_in_int, seq_out, epochs=300, verbose=0)

# Make prediction
yhat = model.predict(seq_in_int, verbose=0)

# Convert predictions back to characters
predicted_chars = [int_to_char[int(round(x[0]))] for x in yhat[0]]
print("Predicted next characters:")
print(predicted_chars)
