import streamlit as st
import pandas as pd
from PIL import Image

#"🎈 My new app"

def app():
    
    st.title("Convolutional Neural Network classifier using text and images")

#############################################
    st.write("---")

    with st.container():
            st.header("First approach: ")
    with st.container():
        st.write("")
        
        st.markdown(
                """
                <p style="font-size: 20px;">
            This model integrates NLP for text and CNNs for image processing. Text data is vectorized using TF-IDF, while images undergo augmentation using Keras' ImageDataGenerator. Key steps include rescaling, shearing, and zooming to enhance robustness and prevent overfitting.
            Model Architecture:
            
            - <p style="font-size: 20px;"> Image Branch: Uses MobileNetV2 for feature extraction, followed by GlobalAveragePooling2D, a dense layer with 512 neurons, and a dropout layer.
            
            - <p style="font-size: 20px;"> Text Branch: Processes TF-IDF vectors with a dense layer of 512 neurons and a dropout layer.
            """
            ,
            unsafe_allow_html=True
            )

        img_Layers_Sajjad_Neu = Image.open("Images/5_DNN_Model/Layers_Sajjad_Neu.jpg")
        st.image(img_Layers_Sajjad_Neu)

        st.markdown(
                """
           <p style="font-size: 20px;"> Both branches are concatenated, and a final dense layer with softmax activation classifies into 27 categories.

           <p style="font-size: 20px;"> Training Setup:
           
            - <p style="font-size: 20px;"> Compile: Optimizer, sparse categorical cross-entropy loss, and accuracy metric.
            
            - <p style="font-size: 20px;"> Data Generators: Batches of 32 for training and validation, with augmentation.
            
            - <p style="font-size: 20px;"> Callbacks: EarlyStopping and ReduceLROnPlateau for monitoring and adjusting training.

            <p style="font-size: 20px;"> Results: Achieved performance over 75% accuracy after 20 epochs, with similar training and validation accuracy, indicating no overfitting or underfitting.
            """
            ,
            unsafe_allow_html=True
            )
        img_Performance_Sajjad = Image.open("Images/5_DNN_Model/Performance_Sajjad.jpg")
        st.image(img_Performance_Sajjad)

    with st.container():
            st.header("Second approach: ")
    with st.container():
        st.write("")
        
        st.write(
                """
            <p style="font-size: 20px;">  Overview:
             
             - <p style="font-size: 20px;"> Combines: Text and image data using TensorFlow and Keras.
             - <p style="font-size: 20px;"> Text Preprocessing: Tokenization, stop word removal, and TF-IDF vectorization (up to 10,000 features).
             - <p style="font-size: 20px;"> Text Model: Dense layers with 128 and 64 neurons, ReLU activation.
             - <p style="font-size: 20px;"> Image Model: Input layer (128x128 RGB), three Conv2D layers (32, 64, 128 filters) with ReLU, MaxPooling, and Flatten.

            <p style="font-size: 20px;"> Integration:
            
            - <p style="font-size: 20px;"> Combined Branch: Concatenates text and image features, processes with dense layers (128 and 64 neurons).
            - <p style="font-size: 20px;"> Output Layer: Softmax activation for classification into 27 categories.
            """
            ,
            unsafe_allow_html=True
            )

        img_Pry_layer_neu = Image.open("Images/5_DNN_Model/Pry_layer_neu.jpg")
        st.image(img_Pry_layer_neu)

        st.write(
                """
           <p style="font-size: 20px;"> Training:
            
            - <p style="font-size: 20px;"> Data Generators: Augmented text and image data (batch size: 32).
            
            - <p style="font-size: 20px;"> Compile: Adam optimizer, categorical cross-entropy loss, accuracy metric.
            
            - <p style="font-size: 20px;"> Train/Validation Split: 80/20.

            <p style="font-size: 20px;"> Results: Achieved performance over 80% on training set, 80% on validation set over 10 epochs.
            """
            ,
            unsafe_allow_html=True
            )
        img_performance_pry_NEU = Image.open("Images/5_DNN_Model/performance_pry_NEU.jpg")
        st.image(img_performance_pry_NEU)

    with st.container():
            st.header("Third approach: ")
    with st.container():
        st.write("")
        
        st.write(
                """
            <p style="font-size: 20px;"> Overview:
             
             - <p style="font-size: 20px;"> Combines: Text and image features for product classification.
             
             - <p style="font-size: 20px;"> Text Preprocessing: Tokenization, stop word removal, synonym augmentation, TF-IDF vectorization (5,000 features).
             
             - <p style="font-size: 20px;"> Image Processing: EfficientNetB0 for feature extraction, resizing, normalization, augmentation.

            <p style="font-size: 20px;"> Text Branch:
             
             - <p style="font-size: 20px;"> Layers: Dense (512 neurons, ReLU) → Batch Normalization → Dropout (25%) → Dense (256 neurons, ReLU) → Batch Normalization → Dropout (50%).

            <p style="font-size: 20px;"> Image Branch:
             
             - <p style="font-size: 20px;"> Layers: Dense (256 neurons, ReLU) → Batch Normalization → Dropout (50%) → Dense (128 neurons, ReLU) → Batch Normalization → Dropout (50%).
            """
            ,
            unsafe_allow_html=True
            )

        img_Layers_Vitmer_Neu = Image.open("Images/5_DNN_Model/Layers_Vitmer_Neu.jpg")
        st.image(img_Layers_Vitmer_Neu)

        st.write(
                """
            <p style="font-size: 20px;"> Combined Branch:
            
            - <p style="font-size: 20px;"> Layers: Concatenation → Dense (64 neurons, ReLU) → Batch Normalization → Dropout (50%) → Output (softmax activation).

            <p style="font-size: 20px;"> Training:
             
             - <p style="font-size: 20px;"> Compile: Nadam optimizer, sparse categorical cross-entropy loss.
             
             - <p style="font-size: 20px;"> Callbacks: Early stopping, learning rate reduction.
             
             - <p style="font-size: 20px;"> Performance: Achieves over 93% accuracy on both training and test sets.
            
            <p style="font-size: 20px;"> Key Metrics:
             
             - <p style="font-size: 20px;"> Detailed classification report and confusion matrix: Shows high precision across all product types.
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
    
