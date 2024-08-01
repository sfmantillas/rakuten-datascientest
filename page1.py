import streamlit as st
import pandas as pd
from PIL import Image

def app():

    img_SVC = Image.open("Images/3_Machile_Learning/2st iter SVM C = 10k.png")

    st.title("Page 1")
    st.write("This is the content of Page 1.")

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
#END