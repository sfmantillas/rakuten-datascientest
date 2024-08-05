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
            The Naive Bayes Classifier, based on Bayes Theorem, 
            is a probabilistic algorithm often used for text 
            classification. Despite its assumption of feature 
            independence (hence "naive"), it performs well in 
            various applications. Performance metrics, a 
            classification report bar plot, and a confusion matrix 
            reveal significant variance across product types. 
            Achieving a 70% overall accuracy, the model is 
            satisfactory given its simplicity and exclusive 
            use of text data.
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
            The Random Forest Classifier is an ensemble 
            method that enhances accuracy and robustness
            by combining multiple decision trees. In this 
            model, decisions flow from the root to leaf 
            nodes, with each leaf representing a class 
            label. Performance metrics, the plot of its 
            classification report, and confusion matrix 
            indicate an accuracy of 75%, positioning it 
            between the Naive Bayes and Support Vector Machine 
            models in terms of accuracy.
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
                The Logistic Regression Classifier is a linear 
                model used for binary and multiclass classification. 
                It predicts probabilities by applying the logistic 
                function to a linear combination of features. 
                Performance metrics, the plot of classification report  
                and confusion matrix show an 
                accuracy of 77%, positioning it between the Random 
                Forest and Support Vector Machine models in terms of 
                accuracy. 
                This model is valued for its simplicity and 
                effectiveness, especially in text classification tasks. 
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
                The Support Vector Machine Classifier (SVC) 
                optimally separates classes by finding a 
                hyperplane in a multi-dimensional space, 
                using support vectors to define this separation. 
                With a regularization parameter (C) set to 1, 
                the model allows more misclassifications in favor 
                of a larger margin. A linear kernel is used. 
                Performance metrics, classification report, 
                and confusion matrix show an overall accuracy 
                of 83%, significantly higher than the rest of 
                the models.
                """
                ,
                unsafe_allow_html=True
                )
        