import streamlit as st
import pandas as pd
from PIL import Image

#"🎈 My new app" This version tries to include a dropdown menu to change between text and image preprocessing
img_Distr_product_type_codes = Image.open("Images/2_Data_Exploration/Distr_product_type_codes.png")
img_Distr_product_type_codes_pie = Image.open("Images/2_Data_Exploration/Distr_product_type_codes_pie.png")
img_Distr_product_title_length = Image.open("Images/2_Data_Exploration/Distr_product_title_length.png")

img_word_cloud_1300 = Image.open("Images/3_Preprocessing/word_cloud_1300.png")
img_example_word_cloud_1940_stopwords = Image.open("Images/3_Preprocessing/example_word_cloud_1940_stopwords.png")
img_example_word_cloud_1940_no_stopwords = Image.open("Images/3_Preprocessing/example_word_cloud_1940_no_stopwords.png")

img_example_0 = Image.open("Images/3_Preprocessing/example_0.jpg")
img_example_1 = Image.open("Images/3_Preprocessing/example_1.jpg")
img_example_2 = Image.open("Images/3_Preprocessing/example_2.jpg")
img_example_3 = Image.open("Images/3_Preprocessing/example_3.jpg")
img_example_4 = Image.open("Images/3_Preprocessing/example_4.jpg")

img_example_5 = Image.open("Images/3_Preprocessing/example_5.jpg")
img_example_6 = Image.open("Images/3_Preprocessing/example_6.jpg")
img_example_7 = Image.open("Images/3_Preprocessing/example_7.jpg")
img_example_8 = Image.open("Images/3_Preprocessing/example_8.jpg")
img_example_9 = Image.open("Images/3_Preprocessing/example_9.jpg")



options = ["Text preprocessing", "Image preprocessing"]

def app():
    
    st.title("3. Preprocessing of data")
    #st.image(Img_cover)

    with st.container(): 
            st.markdown(
            """
            <p style="font-size: 20px;">
            Before feeding any of the machine-learning or deep-neural-network algorithms
            we present later, we separate our data in text and image subsets such that
            they are expressed numerically so as they can be read by our models. Below
            you find a drop menu where you can select between the preprocessing of text variables, 
            i.e., 'designation' and 'description', or the preprocessing we followed with
            the images. 
            </p>
            """
            ,
            unsafe_allow_html=True
            )
    selected_option = st.selectbox("Select an option:", options)

    if selected_option == "Text preprocessing":
        with st.container():
            st.header("Text preprocessing:")

        st.image(img_word_cloud_1300)
        st.markdown(
            """
            <p style="font-size: 20px;">
            The preparation of the text consists of the following steps: 
            </p>
            
            - <p style="font-size: 20px;"> Concatenation: We start by concatenating the 'designation' and 'description' variables in order to have only one text variable. </p>
            - <p style="font-size: 20px;"> Tokenization: Then we "tokenize" our text variable, that is, using the method 'word_tokenize' from the library 'nltk' we create an array with every word found in the whole corpus of the dataset, obtaining a list of 10'697,098 character clusters, including symbols such as ':', '%', '<', etc. . This is also the longest stage of the text processing. </p>
            - <p style="font-size: 20px;"> Count: Using the token array and the method 'Counter' from the library 'collections' we count the number of times a specific word or special character appears in the corpus. As a sample, the first ten most frequent "words" are [('>', 391273), ('<', 391237), ('de', 374144), (':', 311939), (';', 233885), ('&', 222630), ('.', 207131), ('#', 192313), ('39', 168706), ('et', 145732)], where each number is the number of times that character or word is found. </p>
            - <p style="font-size: 20px;"> First word clouds: At this point we generate our first word clouds for each of the product categories, finding that they are full of stopwords that do not contribute to the characterization of the text. Below it is displayed the word cloud for the product type code 1940. 
            """
            ,  
            unsafe_allow_html=True
        )
        st.image(img_example_word_cloud_1940_stopwords)
        st.markdown(
            """
            - <p style="font-size: 20px;"> Stopwords: We solve this problem using 'stopwords' from the submodule 'nltk.corpus' to download the stopwords of the French language assuming that the huge majority of the corpus is in French . </p>
            - <p style="font-size: 20px;"> Re-tokenization: We re-tokenize our text ignoring the stopwords, not only making the running time shorter but also yielding a clean array with only meaninful words. </p>
            - <p style="font-size: 20px;"> Second word clouds: To confirm that the stopwords were correctly ignored and that the words remaining are characterizing the corpus for each category, we generate new word clouds. As an example, below you find the word cloud of the same product category above, 1094. Please notice the difference between them. </p>
            """
            ,
            unsafe_allow_html=True
        )
        st.image(img_example_word_cloud_1940_no_stopwords)
        st.markdown(
            """
            - <p style="font-size: 20px;"> Last cleaning: Lastly, we withdraw HTML tags, numbers, and any special character from our processed corpus . </p>

            <p style="font-size: 20px;">
            The result of this process is an array containg the frequency of each word that 
            has passed the filters discussed above. This is the format that we use to feed
            our machine learning and deep neural network models. 
            </p> 
            </p>
            """
            ,
            unsafe_allow_html=True
        )
    
    elif selected_option == "Image preprocessing":
        with st.container():
            st.header("Image preprocessing:")
            st.markdown(
                """
            <p style="font-size: 20px;">
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
            <p style="font-size: 20px;">
            The image preprocessing then goes as follows: 
            </p>
            
            - <p style="font-size: 20px;"> Load image set: We start by 
              all the direction to the images contained in the image_train 
              folder using the productid and imageid columns from the X_train.csv. 
              Below we show five images as examples before the preprocessing. </p>
            """
            ,
            unsafe_allow_html=True
            )

            image_column_0, image_column_1, image_column_2, image_column_3, image_column_4 = st.columns((1,1,1,1,1))
            with image_column_0:
                st.image(img_example_0)
            with image_column_1:
                st.image(img_example_1)
            with image_column_2:
                st.image(img_example_2)
            with image_column_3:
                st.image(img_example_3)
            with image_column_4:
                st.image(img_example_4)

            
            st.markdown(
                """
            - <p style="font-size: 20px;"> Border cropping: We crop the images from all sides with one pixel width using the method ImageOps.crop(image, border=1). This can help to remove any unwanted edges that may have appeared after resizing. </p>
            - <p style="font-size: 20px;"> Numpy conversion: We convert all the images to a NumPy array, the format accepted for the majority of Machine learning and Deep learning models. </p>
            - <p style="font-size: 20px;"> Normalization: We finish by normalizing the pixel values from the range [0, 255] to [0, 1] to standardize the input values, important to increase quality when working with neural networks. </p>

            
            <p style="font-size: 20px;">
            The resulting images after the process describe above are shown below: 
            </p>
            """
            ,
            unsafe_allow_html=True
            )

            image_column_0, image_column_1, image_column_2, image_column_3, image_column_4 = st.columns((1,1,1,1,1))
            with image_column_0:
                st.image(img_example_5)
            with image_column_1:
                st.image(img_example_6)
            with image_column_2:
                st.image(img_example_7)
            with image_column_3:
                st.image(img_example_8)
            with image_column_4:
                st.image(img_example_9)

            
            st.markdown(
                """
            <p style="font-size: 20px;">
            For completeness and also as part of the proof-of-concept 
            demonstration we have designed, we included a step just after 
            loading the user image consisting on padding it with white
            spaces so as it transforms into a square image, the geometry required
            for our preprocessing stage because feeding the model with user image: 
            </p>
            """
            ,
            unsafe_allow_html=True
            )

            
    with st.container():
        st.write("")
        

    
            
    
    
    
            
