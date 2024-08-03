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

def app():
    
    st.title("3. Preprocessing of data")
    #st.image(Img_cover)

    with st.container(): 
            st.markdown(
            """
            <p style="font-size: 25px;">
            Before feeding any of the machine-learning or deep-neural-network algorithms
            we present later, we separate our data in text and image subsets such that
            they are expressed numerically so as they can be read by our models. Below
            you find first the process we implemented with the text variables, 
            'designation' and 'description', and then the procedure we followed with
            the images. 
            </p>
            """
            ,
            unsafe_allow_html=True
            )

    with st.container():
        st.header("Text preprocessing:")

        st.image(img_word_cloud_1300)
        st.markdown(
            """
            <p style="font-size: 25px;">
            The preparation of the text consists of the following steps: 
            </p>
            
            - <p style="font-size: 25px;"> Concatenation: We start by concatenating the 'designation' and 'description' variables in order to have only one text variable. </p>
            - <p style="font-size: 25px;"> Tokenization: Then we "tokenize" our text variable, that is, using the method 'word_tokenize' from the library 'nltk' we create an array with every word found in the whole corpus of the dataset, obtaining a list of 10'697,098 character clusters, including symbols such as ':', '%', '<', etc. . This is also the longest stage of the text processing. </p>
            - <p style="font-size: 25px;"> Count: Using the token array and the method 'Counter' from the library 'collections' we count the number of times a specific word or special character appears in the corpus. As a sample, the first ten most frequent "words" are [('>', 391273), ('<', 391237), ('de', 374144), (':', 311939), (';', 233885), ('&', 222630), ('.', 207131), ('#', 192313), ('39', 168706), ('et', 145732)], where each number is the number of times that character or word is found. </p>
            - <p style="font-size: 25px;"> First word clouds: At this point we generate our first word clouds for each of the product categories, finding that they are full of stopwords that do not contribute to the characterization of the text. Below it is displayed the word cloud for the product type code 1940. 
            """
            ,  
            unsafe_allow_html=True
        )
        st.image(img_example_word_cloud_1940_stopwords)
        st.markdown(
            """
            - <p style="font-size: 25px;"> Stopwords: We solve this problem using 'stopwords' from the submodule 'nltk.corpus' to download the stopwords of the French language assuming that the huge majority of the corpus is in French . </p>
            - <p style="font-size: 25px;"> Re-tokenization: We re-tokenize our text ignoring the stopwords, not only making the running time shorter but also yielding a clean array with only meaninful words. </p>
            - <p style="font-size: 25px;"> Second word clouds: To confirm that the stopwords were correctly ignored and that the words remaining are characterizing the corpus for each category, we generate new word clouds. As an example, below you find the word cloud of the same product category above, 1094. Please notice the difference between them. </p>
            """
            ,
            unsafe_allow_html=True
        )
        st.image(img_example_word_cloud_1940_no_stopwords)
        st.markdown(
            """
            - <p style="font-size: 25px;"> Last cleaning: Lastly, we withdraw HTML tags, numbers, and any special character from our processed corpus . </p>

            <p style="font-size: 25px;">
            The result of this process is an array containg the frequency of each word that 
            has passed the filters discussed above. This is the format that we use to feed
            our machine learning and deep neural network models. 
            </p> 
            </p>
            """
            ,
            unsafe_allow_html=True
        )
            
    
    
    st.write("---")
    
    with st.container():
            st.header("Image preprocessing:")

            st.image(img_Distr_product_title_length)
    with st.container():
        st.write("")
        image_column, text_column = st.columns((1,1))
        with image_column:
            st.image(img_Distr_product_type_codes_pie)
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
            
