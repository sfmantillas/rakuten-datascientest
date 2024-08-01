import streamlit as st
import pandas as pd
from PIL import Image

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("Hello world.")

#Load images
img_SVC = Image.open("Images/3_Machile_Learning/2st iter SVM C = 10k.png")

with st.container():
    st.write("---")
    st.header("Title of the header")
    st.write("")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_SVC)
    with text_column:
        st.subheader("Tithe of the subheader")
        st.write(
            """
            with the actual path to your image file. 
            This code will open the image using the default image viewer on your system.
            with the actual path to your image file. This code will open the image using 
            the default image viewer on your system.
            """
        )

#End