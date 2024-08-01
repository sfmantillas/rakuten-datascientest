import streamlit as st
import pandas as pd
from PIL import Image

st.title("🎈 The first page is here. )
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("Hello world.")

#Load images
img_NBC = Images\3_Machile_Learning\1st iter Naive-Bayes.png
img_SVC = Image.open("Images\3_Machile_Learning\1st iter SVM.png")
img_RFC = Image.open("Images\3_Machile_Learning\1st iter Random forest.png")
img_KNN = Image.open("Images\3_Machile_Learning\1st iter KNN.png")

with st.container():
    st.write("---")
    st.header("Title of the header")
    st.write("")
    image_column_1, image_column_2, image_column_3, image_column_4 = st.columns((1,1,1,1))
    with image_column_1:
        st.image(img_NBC)
    with image_column_2:
        st.image(img_SVC)
    with image_column_3:
        st.image(img_RFC)
    with image_column_4:
        st.image(img_KNN)