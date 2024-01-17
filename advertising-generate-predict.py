import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.naive_bayes import GaussianNB
import pickle 

st.write("# Advertising Model Prediction")
st.write("This app predicts the **Ads Model** type!")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 0.7, 296.4, 148.5) 
    Radio = st.sidebar.slider('Radio', 0.0, 49.6,24.8 )
    Newspaper = st.sidebar.slider('Newspaper', 0.3, 114.0, 57.2)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

advertising_model = pickle.load(open("Advertising.h5", "rb")) 

prediction = advertising_model.predict(df)

st.subheader('Class labels and their corresponding index number')
st.write(pickle.load.unique())

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
