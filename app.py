import streamlit as st
import pickle
import numpy as np
import sklearn
import nltk
nltk.download('punkt')
import nltk.tokenize

doc = open('model.pickle', 'r')
model = pickle.load('model.pickle')

st.title('Text app')
text = st.input_text('Ingrese el texto')
text = np.array([text])
if st.button('Identificar'):
  prediction = model.predict(text)[0]
  if prediction == 1:
    prediction = 'positive'
    st.write(prediction)
  else:
    prediction = 'negative'
    st.write(prediction)
  
