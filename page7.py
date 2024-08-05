import streamlit as st
import pandas as pd
from PIL import Image

#"🎈 My new app"
Img_cover = Image.open("Images/0_FrontCover/FotoJet.jpg")

def app():
    
    st.title("Business and scientific conclusions")
    
    with st.container():
            st.header("Third approach: ")
    with st.container():
        st.write("")
        
        st.write(
                """
             - High Accuracy Achieved: Models, particularly Deep Learning Approach #3, show excellent results in classifying e-commerce products, demonstrating effective learning from data.

             - Simple vs. Complex Models: Simple Machine Learning models offer satisfactory results, but more complex deep learning models yield superior performance.

             - Multi-modal Input Advantage: Combining text and image data enhances classification accuracy, underscoring the benefit of using multi-modal inputs.
            """
            ,
            unsafe_allow_html=True
            )

        img_Layers_Vitmer_Neu = Image.open("Images/5_DNN_Model/Layers_Vitmer_Neu.png")
        st.image(img_Layers_Vitmer_Neu)

        st.write(
                """
            Combined Branch:
            - Layers: Concatenation → Dense (64 neurons, ReLU) → Batch Normalization → Dropout (50%) → Output (softmax activation).

            Training:
             - Compile: Nadam optimizer, sparse categorical cross-entropy loss.
             - Callbacks: Early stopping, learning rate reduction.
             - Performance: Achieves over 90% accuracy on both training and test sets.
            
            Key Metrics:
             - Detailed classification report and confusion matrix: Shows high precision across all product types.
            """
            ,
            unsafe_allow_html=True
            )
        img_Vitaly_Acc_Loss = Image.open("Images/5_DNN_Model/Vitaly_Acc_Loss.jpg")
        st.image(img_Vitaly_Acc_Loss)

        img_Vitaly_Classification_report = Image.open("Images/5_DNN_Model/Vitaly_Classification_report.jpg")
        st.image(img_Vitaly_Classification_report)

        img_Vitaly_CM = Image.open("Images/5_DNN_Model/Vitaly_CM.jpg")
        st.image(img_Vitaly_CM)