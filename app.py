import streamlit as st
import pickle
import numpy as np
import sklearn
import nltk
nltk.download('punkt')
import nltk.tokenize

def tokenizer(text):
  return text.split()

doc = open('model.pickle', 'rb')
model = pickle.load(doc)

st.title('Text app')
text = st.text_input('Ingrese el texto')
text = np.array([text])
if st.button('Identificar'):
  prediction = model.predict(text)[0]
  if prediction == 1:
    prediction = 'positive'
    st.write(prediction)
  else:
    prediction = 'negative'
    st.write(prediction)
  
