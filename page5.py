import streamlit as st
import pandas as pd
from PIL import Image

#"🎈 My new app"
Img_cover = Image.open("Images/0_FrontCover/FotoJet.jpg")
img_1_Classif_NBC_confmat = Image.open("Images/4_Machile_Learning/1_Classif_NBC_confmat.png")
img_1_Classif_NBC_report = Image.open("Images/4_Machile_Learning/1_Classif_NBC_report.png")

img_model = Image.open("Images/5_DNN_Model/model.png")

def app():
    
    st.title("Convolutional Neural Network classifier using text and images")

#############################################
    st.write("---")

    with st.container():
            st.header("Multinomial Naïve-Bayes Classifier:")
    with st.container():
        st.write("")
        image_column, text_column = st.columns((1,1))
        with image_column:
            st.image(img_model)
        with text_column:
            st.markdown(
                """
            <p style="font-size: 25px;">
            We immediately find that we are facing a classification problem with strongly
            unbalanced 27 categories, where the most abundant labelled as '2583' 
            represents itself 12% of the dataset, while the least abundant labelled as
            '1180' We immediately find that we are facing a classification problem with strongly
            unbalanced 27 categories, where the most abundant labelled as '2583' 
            represents itself 12% of the dataset, while the least abundant labelled as
            '1180' 
            </p>

            <p style="font-size: 25px;">
            We immediately find that we are facing a classification problem with strongly
            unbalanced 27 categories, where the most abundant labelled as '2583' 
            represents itself 12% of the dataset, while the least abundant labelled as
            '1180' 
            </p>
            """
            ,
            unsafe_allow_html=True
            )
        st.markdown(
            """
            <p style="font-size: 25px;">
            represents less than 1% of our dataset. 
            </p>
            """
            ,
            unsafe_allow_html=True
        )

        st.image(img_1_Classif_NBC_report)