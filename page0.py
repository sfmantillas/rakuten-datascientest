import streamlit as st
import pandas as pd
from PIL import Image

#"🎈 My new app"

def app():
    st.title("🎈 My new app")
    st.write(
        "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    )
    st.write("Hello world.")

    with st.container():
        st.write("---")
        st.header("Description of the project:")
        st.write(
            """
            Cataloging products according to different data (texts and images) 
            is important for e-commerce since it allows for various applications 
            such as product recommendation and personalized research. It is then 
            a question of predicting the type code of the products knowing textual 
            data (designation and description of the products) as well as image data 
            (image of the product).
            """
        )
    
    with st.container():
        st.write("---")
        st.header("Resources to refer to:")
        st.write(
            """
            This project is part of the Rakuten France Multimodal Product Data Classification challenge, the data and their description are available at: https://challengedata.ens.fr/challenges/35 
            
            Text data: ~60 mb
            
            Image data: ~2.2 gb
            
            99k data with over 1000 classes.
            """
        )

    with st.container():
        st.write("---")
        st.header("Members")
        st.write("Here is a list of items:")
        st.write(
            """
            - Lakshmi Narasimha Priyatham Kumanduri
            - Sajad Bairampour
            - Vitalij Merenics
            - Noel Nickel
            - Sebastián Felipe Mantilla-Serrano
            """
            )

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

#End")
