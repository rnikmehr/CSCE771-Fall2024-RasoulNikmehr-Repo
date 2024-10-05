
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, RepeatVector, TimeDistributed

# Define input sequence
seq_in = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Reshape input into [samples, timesteps, features]
n_in = len(seq_in)
seq_in = seq_in.reshape((1, n_in, 1))

# Prepare output sequence
seq_out = seq_in[:, 1:, :]
n_out = n_in - 1

# Define model
model = Sequential()
model.add(LSTM(100, activation='relu', input_shape=(n_in,1)))
model.add(RepeatVector(n_out))
model.add(LSTM(100, activation='relu', return_sequences=True))
model.add(TimeDistributed(Dense(1)))
model.compile(optimizer='adam', loss='mse')

# Fit model
model.fit(seq_in, seq_out, epochs=300, verbose=0)

# Make prediction
yhat = model.predict(seq_in, verbose=0)
print("Predicted next numbers:")
print(yhat[0,:,0])
