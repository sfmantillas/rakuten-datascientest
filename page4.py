import streamlit as st
import pandas as pd
from PIL import Image

#"🎈 My new app"
Img_cover = Image.open("Images/0_FrontCover/FotoJet.jpg")

img_Distr_product_type_codes = Image.open("Images/2_Data_Exploration/Distr_product_type_codes.png")
img_Distr_product_type_codes_pie = Image.open("Images/2_Data_Exploration/Distr_product_type_codes_pie.png")
img_Distr_product_title_length = Image.open("Images/2_Data_Exploration/Distr_product_title_length.png")


img_1_Sample = Image.open("Images/4_Machile_Learning/1_Sample.png")
img_1_Classif_LRC_confmat = Image.open("Images/4_Machile_Learning/1_Classif_LRC_confmat.png")
img_1_Classif_LRC_report = Image.open("Images/4_Machile_Learning/1_Classif_LRC_report.png")
img_1_Classif_RFC_confmat = Image.open("Images/4_Machile_Learning/1_Classif_RFC_confmat.png")
img_1_Classif_RFC_report = Image.open("Images/4_Machile_Learning/1_Classif_RFC_report.png")
img_1_Classif_SVC_confmat = Image.open("Images/4_Machile_Learning/1_Classif_SVC_confmat.png")
img_1_Classif_SVC_report = Image.open("Images/4_Machile_Learning/1_Classif_SVC_report.png")
img_1_Classif_NBC_confmat = Image.open("Images/4_Machile_Learning/1_Classif_NBC_confmat.png")
img_1_Classif_NBC_report = Image.open("Images/4_Machile_Learning/1_Classif_NBC_report.png")

options = ["Multinomial Naïve-Bayes Classifier", "Random Forest Classifier", "Logistic Regression Classifier", "Support Vector Classifier"]

def app():
    
    st.title("Machine learning classifiers using text variable")

#############################################
    #st.write("---")

    with st.container(): 
        st.markdown(
            """
            <p style="font-size: 20px;">
            The machine learning stage of the project consisted on classifying
            the different text samples from the corpus into the 27 categories 
            of 'prdtypecode' column in Y_train.csv file. 
            </p>
            """
            ,
            unsafe_allow_html=True
        )

        st.image(img_1_Sample)

        st.markdown(
            """
            <p style="font-size: 20px;">
            Below you find a drop menu where you can select among the 
            four models we have explored: Multinomial Naïve-Bayes, 
            Random Forest, Logistic Regression and Support Vector Machine.
            </p>
            """
            ,
            unsafe_allow_html=True
            )
    selected_option = st.selectbox("Select an option:", options)
    
    if selected_option == "Multinomial Naïve-Bayes Classifier":
        with st.container():
            st.header("Multinomial Naïve-Bayes Classifier:")

            st.image(img_1_Classif_NBC_report)
        with st.container():
            st.write("")
            image_column, text_column = st.columns((1,1))
            with image_column:
                st.image(img_1_Classif_NBC_confmat)
            with text_column:
                st.markdown(
                """
            <p style="font-size: 25px;">
            We immediately find that we are facing a classification problem with strongly
            unbalanced 27 categories, where the most abundant labelled as '2583' 
            represents itself 12% of the dataset, while the least abundant labelled as
            '1180' 
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

#############################################
    elif selected_option == "Random Forest Classifier":
        #st.write("---")
        with st.container():
            st.header("Random Forest Classifier:")

            st.image(img_1_Classif_RFC_report)
        with st.container():
            st.write("")
            image_column, text_column = st.columns((1,1))
            with image_column:
                st.image(img_1_Classif_RFC_confmat)
            with text_column:
                st.markdown(
                """
            <p style="font-size: 25px;">
            We immediately find that we are facing a classification problem with strongly
            unbalanced 27 categories, where the most abundant labelled as '2583' 
            represents itself 12% of the dataset, while the least abundant labelled as
            '1180' 
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

#############################################
    elif selected_option == "Logistic Regression Classifier":
        #st.write("---")
        with st.container():
            st.header("Logistic Regression Classifier:")

            st.image(img_1_Classif_LRC_report)
        with st.container():
            st.write("")
            image_column, text_column = st.columns((1,1))
            with image_column:
                st.image(img_1_Classif_LRC_confmat)
            with text_column:
                st.markdown(
                """
                <p style="font-size: 25px;">
                We immediately find that we are facing a classification problem with strongly
                unbalanced 27 categories, where the most abundant labelled as '2583' 
                represents itself 12% of the dataset, while the least abundant labelled as
                '1180' 
                """
                ,
                unsafe_allow_html=True
                )
            

#############################################
    elif selected_option == "Support Vector Classifier":
        #st.write("---")
        with st.container():
            st.header("Support Vector Classifier:")

            st.image(img_1_Classif_SVC_report)
        with st.container():
            st.write("")
            image_column, text_column = st.columns((1,1))
            with image_column:
                st.image(img_1_Classif_SVC_confmat)
            with text_column:
                st.markdown(
                """
                <p style="font-size: 25px;">
                We immediately find that we are facing a classification problem with strongly
                unbalanced 27 categories, where the most abundant labelled as '2583' 
                represents itself 12% of the dataset, while the least abundant labelled as
                '1180' 
                """
                ,
                unsafe_allow_html=True
                )
        