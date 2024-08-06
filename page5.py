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
            st.header("First approach: ")
    with st.container():
        st.write("")
        
        st.write(
                """
            This model integrates NLP for text and CNNs for image processing. Text data is vectorized using TF-IDF, while images undergo augmentation using Keras' ImageDataGenerator. Key steps include rescaling, shearing, and zooming to enhance robustness and prevent overfitting.
            Model Architecture:
             - Image Branch: Uses MobileNetV2 for feature extraction, followed by GlobalAveragePooling2D, a dense layer with 512 neurons, and a dropout layer.
             - Text Branch: Processes TF-IDF vectors with a dense layer of 512 neurons and a dropout layer.
            """
            ,
            unsafe_allow_html=True
            )

        img_Layers_Sajjad_Neu = Image.open("Images/5_DNN_Model/Layers_Sajjad_Neu.png")
        st.image(img_Layers_Sajjad_Neu)

        st.write(
                """
           Both branches are concatenated, and a final dense layer with softmax activation classifies into 27 categories.

           Training Setup:
            - Compile: Optimizer, sparse categorical cross-entropy loss, and accuracy metric.
            - Data Generators: Batches of 32 for training and validation, with augmentation.
            - Callbacks: EarlyStopping and ReduceLROnPlateau for monitoring and adjusting training.

            Results: Achieved performance with 78% accuracy after 20 epochs, with similar training and validation accuracy, indicating no overfitting or underfitting.
            """
            ,
            unsafe_allow_html=True
            )
        img_Performance_Sajjad = Image.open("Images/5_DNN_Model/Performance_Sajjad.png")
        st.image(img_Performance_Sajjad)

    with st.container():
            st.header("Second approach: ")
    with st.container():
        st.write("")
        
        st.write(
                """
            Overview:
             - Combines: Text and image data using TensorFlow and Keras.
             - Text Preprocessing: Tokenization, stop word removal, and TF-IDF vectorization (up to 10,000 features).
             - Text Model: Dense layers with 128 and 64 neurons, ReLU activation.
             - Image Model: Input layer (128x128 RGB), three Conv2D layers (32, 64, 128 filters) with ReLU, MaxPooling, and Flatten.

            Integration:
             - Combined Branch: Concatenates text and image features, processes with dense layers (128 and 64 neurons).
             - Output Layer: Softmax activation for classification into 27 categories.
            """
            ,
            unsafe_allow_html=True
            )

        img_Pry_layer_neu = Image.open("Images/5_DNN_Model/Pry_layer_neu.png")
        st.image(img_Pry_layer_neu)

        st.write(
                """
           Training:
            - Data Generators: Augmented text and image data (batch size: 32).
            - Compile: Adam optimizer, categorical cross-entropy loss, accuracy metric.
            - Train/Validation Split: 80/20.

            Results: Achieved performance with  87% on training set, 80% on validation set over 10 epochs.
            """
            ,
            unsafe_allow_html=True
            )
        img_performance_pry_NEU = Image.open("Images/5_DNN_Model/performance_pry_NEU.png")
        st.image(img_performance_pry_NEU)

    with st.container():
            st.header("Third approach: ")
    with st.container():
        st.write("")
        
        st.write(
                """
            Overview:
             - Combines: Text and image features for product classification.
             - Text Preprocessing: Tokenization, stop word removal, synonym augmentation, TF-IDF vectorization (5,000 features).
             - Image Processing: EfficientNetB0 for feature extraction, resizing, normalization, augmentation.

            Text Branch:
             - Layers: Dense (512 neurons, ReLU) → Batch Normalization → Dropout (25%) → Dense (256 neurons, ReLU) → Batch Normalization → Dropout (50%).

            Image Branch:
             - Layers: Dense (256 neurons, ReLU) → Batch Normalization → Dropout (50%) → Dense (128 neurons, ReLU) → Batch Normalization → Dropout (50%).
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
        img_Vitaly_Acc_Loss = Image.open("Images/5_DNN_Model/Vitaly_Acc_Loss.png")
        st.image(img_Vitaly_Acc_Loss)

        img_Vitaly_Classification_report = Image.open("Images/5_DNN_Model/Vitaly_Classification_report.png")
        st.image(img_Vitaly_Classification_report)

        img_Vitaly_CM = Image.open("Images/5_DNN_Model/Vitaly_CM.png")
        st.image(img_Vitaly_CM)
    
