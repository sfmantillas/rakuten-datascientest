import streamlit as st
import pandas as pd
from PIL import Image
from io import StringIO

img_Distr_product_type_codes = Image.open("Images/2_Data_Exploration/Distr_product_type_codes.png")
img_Distr_product_type_codes_pie = Image.open("Images/2_Data_Exploration/Distr_product_type_codes_pie.png")
img_Distr_product_title_length = Image.open("Images/2_Data_Exploration/Distr_product_title_length.png")
img_Distr_product_descript_length = Image.open("Images/2_Data_Exploration/Distr_product_descript_length.png")
img_Corr_mat = Image.open("Images/2_Data_Exploration/Corr_mat.png")

# List of image paths
list_categories = [2583, 1560, 1300, 2060, 2522, 1280, 2403, 2280, 1920, 1160, 1320, 10, 2705, 1140, 2582, 40, 2585, 1302, 1281, 50, 2462, 2905, 60, 2220, 1301, 1940, 1180]
image_paths = [f'Images/2_Data_Exploration/collage_padding_{i}.png' for i in list_categories]  # Replace with your actual image paths

# List of image captions for dropdown menu
image_names = [f'Product type code {i}' for i in list_categories]

X_train = pd.read_csv('./Datasets/X_train.csv',index_col=0)
Y_train = pd.read_csv('./Datasets/Y_train.csv',index_col=0)
X_test = pd.read_csv('./Datasets/X_test.csv',index_col=0)

img_example_0 = Image.open("Images/2_Data_Exploration/image_1008141237_product_436067568a.jpg")
img_example_1 = Image.open("Images/2_Data_Exploration/image_938777978_product_201115110a.jpg")
img_example_2 = Image.open("Images/2_Data_Exploration/image_457047496_product_50418756a.jpg")
img_example_3 = Image.open("Images/2_Data_Exploration/image_1077757786_product_278535884a.jpg")
img_example_4 = Image.open("Images/2_Data_Exploration/image_393356830_product_5862738a.jpg")

img_example_5 = Image.open("Images/2_Data_Exploration/image_1274228667_product_133389013.jpg")
img_example_6 = Image.open("Images/2_Data_Exploration/image_1295960357_product_4128438366.jpg")
img_example_7 = Image.open("Images/2_Data_Exploration/image_1265224052_product_3929899732.jpg")
img_example_8 = Image.open("Images/2_Data_Exploration/image_940543690_product_152993898.jpg")
img_example_9 = Image.open("Images/2_Data_Exploration/image_1310030687_product_4181949876.jpg")

def capture_df_info(df):
    info_buffer = StringIO()
    df.info(buf=info_buffer)
    info_buffer.seek(0)
    return info_buffer.getvalue()


# Initialize session state
if 'selected_image_index' not in st.session_state:
    st.session_state.selected_image_index = 0


def app():

    st.title("2. Data Exploration")

    with st.container(): 
            st.markdown(
            """
            <p style="font-size: 20px;">
            The dataset consists of three CSV files: X_train.csv, 
            y_train.csv and X_test.csv. 
            X_train.csv contains information of 84,916 items,
            divided in the columns 'designation' (character array), 
            'description' (character array), 
            'productid' (integer), and 'imageid'  (integer). A
            sample of the file is shown below:
            </p>
            """
            ,
            unsafe_allow_html=True
        )
    
    st.write(X_train[1:6])
    with st.container():
        with st.container():
            st.markdown(
            """
            <p style="font-size: 20px;">
            Attached to the CSV files shared by Rakuten, 
            there is also a ZIP file containing two folders, 
            'image_train' and 'image_test', and inside them the 
            photographs of the products as JPG files, one 
            image per entry in the CSV files. 
            The corresponding JPG images of the products displayed
            above and contained in the folder 'image_train'
            are shown below:
            </p>
            """
            ,
            unsafe_allow_html=True
        )

        image_column_0, image_column_1, image_column_2, image_column_3, image_column_4 = st.columns((1,1,1,1,1))
        with image_column_0:
            st.image(img_example_0)
            st.text("productid: \n436067568")
        with image_column_1:
            st.image(img_example_1)
            st.text("productid: \n201115110")
        with image_column_2:
            st.image(img_example_2)
            st.text("productid: \n50418756")
        with image_column_3:
            st.image(img_example_3)
            st.text("productid: \n278535884")
        with image_column_4:
            st.image(img_example_4)
            st.text("productid: \n5862738")

    with st.container(): 
            st.markdown(
            """
            <p style="font-size: 20px;">
            Then, the y_train.csv with with 84,916 
            items and the column 'prdtypecode'  (integer) contains
            the target labels of the items described in 
            file X_train.csv:
            </p>
            """
            ,
            unsafe_allow_html=True
        )
    
    st.write(Y_train[1:6])

    with st.container(): 
            st.markdown(
            """
            <p style="font-size: 20px;">
            Lastly,  
            X_train.csv contains 13,812 items and the same 
            features of X_train.csv, except that there is
            no Y_test.csv file with the 'prdtypecode' labels, 
            leaving them unknown. The challenge then 
            consists of predicting the Y_test labels and
            submit the classification to Rakuten challenge
            website where a score is given depending on the
            success on matching with the real hidden labels. 
            A sample of the X_test.csv file is shown below: 
            </p>
            """
            ,
            unsafe_allow_html=True
        )
    
    st.write(X_test[1:6])
    with st.container():
        with st.container(): 
            st.markdown(
            """
            <p style="font-size: 20px;">
            The corresponding JPG images of the products displayed
            above and contained in the folder 'image_test'
            are shown below:
            </p>
            """
            ,
            unsafe_allow_html=True
        )

        image_column_0, image_column_1, image_column_2, image_column_3, image_column_4 = st.columns((1,1,1,1,1))
        with image_column_0:
            st.image(img_example_5)
            st.text("productid: \n133389013")
        with image_column_1:
            st.image(img_example_6)
            st.text("productid: \n4128438366")
        with image_column_2:
            st.image(img_example_7)
            st.text("productid: \n3929899732")
        with image_column_3:
            st.image(img_example_8)
            st.text("productid: \n152993898")
        with image_column_4:
            st.image(img_example_9)
            st.text("productid: \n4181949876")

    with st.container():
        st.write("---")
        st.header("Characterization of the X-train DataFrame:")

        st.write("### Info report of DataFrame X_train:")
        X_train_info = capture_df_info(X_train)
        st.text(X_train_info)
        st.markdown(
            """
            <p style="font-size: 20px;">
            We find that there are 29,800 products with missing descriptions. Instead of
            eliminating these items or deleting the 'description' column, we choose to 
            concatenate the 'designation' and 'description' columns into a unique column 
            containing the text information for each item. 
            </p>
            """
            ,
            unsafe_allow_html=True
        )
        
        st.write("### Info report of DataFrame Y_train:")
        X_train_info = capture_df_info(Y_train)
        st.text(X_train_info)
        st.markdown(
            """
            <p style="font-size: 20px;">
            Y_train has no missing values. 
            </p>
            """
            ,
            unsafe_allow_html=True
        )
        
        st.write("### Info report of DataFrame X_test:")
        X_test_info = capture_df_info(X_test)
        st.text(X_test_info)
        st.markdown(
            """
            <p style="font-size: 20px;">
            Lastly, X_test has 4,886 items with missing descriptions. Similarly to the
            X_train DataFrame, we will concatenate the columns 'designation' and 
            'description' to create a unique text column. 
            </p>
            """
            ,
            unsafe_allow_html=True
        )
    st.write("---")

    with st.container(): 
            st.markdown(
            """
            <p style="font-size: 20px;">
            Below you will find the results of a first exploration done on the dataset. 
            </p>
            """
            ,
            unsafe_allow_html=True
        )
    
    with st.container():
            st.header("Distribution of the product type codes 'prdtypecode':")

            st.image(img_Distr_product_type_codes)

            
    with st.container():
        st.write("")
        image_column, text_column = st.columns((1,1))
        with image_column:
            st.image(img_Distr_product_type_codes_pie)
        with text_column:
            st.markdown(
                """
            <p style="font-size: 20px;">
            We immediately find that we are facing a classification problem with strongly
            unbalanced 27 categories, where the most abundant labelled as '2583' 
            represents itself 12% of the dataset, while the least abundant labelled as
            '1180' represents less than 1% of our dataset. 
            """
            ,
            unsafe_allow_html=True
            )
        #st.markdown(
        #    """
        #    <p style="font-size: 20px;">
        #    represents less than 1% of our dataset. 
        #    </p>
        #    """
        #    ,
        #    unsafe_allow_html=True
        #)
    
    st.write("---")
    
    with st.container():
            st.header("Distribution of Product Titles Length ('designation' of X_train):")

            st.image(img_Distr_product_title_length)

            
    with st.container():
        st.write("")
        st.markdown(
                """
            <p style="font-size: 20px;">
            In this histogram we see the number of words employed for the title of the products 
            contained in the 'designation' variable. We can characterize this
            distribution using the median and the first moments of the distribution: 
            the mean (first moment), the standard deviation (squared root
            of the second moment), the skewness (third moment), and the kurtosis 
            (fourth moment). From our distribution we obtain: 
            </p>
            
            - <p style="font-size: 20px;"> Median: 11. The median of 11 informs us that the 50% of the products have designations shorter than 11 words, and similarly for titles with more than 11 words. </p>
            - <p style="font-size: 20px;"> Mean: 11.56. The mean is slighly displaced to the right respect to the median due to the long tail for long titles, that is, the distribution is skewed to the right and rare long titles pull the mean to that direction. </p>
            - <p style="font-size: 20px;"> Standard deviation: 6.21. The standard deviation of 6.21 tells us about the dispersion around the mean, and closely around the median, suggesting that the majority of the titles are approximately between 6 and 18 words.   </p>
            - <p style="font-size: 20px;"> Skewness: 2.10. The positive skewness of 2.10 is consistent to the conclusions we extracted from the median and the mean, the distribution is skewed to the right, it means, there are rare titles with very long titles, some of them with four times more words than the median of 11. 
            - <p style="font-size: 20px;"> Kurtosis: 7.60. Finally, the kurtosis of 7.60 is informing that the distribution is leptokurtic, that is, it has longer tails and is more peaked close to the mean compared to a normal distribution. In particular, this value larger than 3, reaffirms the existence of outliers and extreme values, it means, the very rare and long titles.  </p>

            <p style="font-size: 20px;">
            The median of 11 informs us that the 50% of the products have designations
            shorter than 11 words, and similarly for titles with more than 11 words. 
            </p>
            """
            ,
            unsafe_allow_html=True
            )
    
    st.write("---")
    
    with st.container():
            st.header("Distribution of Product Descriptions Length ('description' of X_train):")

            st.image(img_Distr_product_descript_length)
# # 80.16663526308352 115.41128398754836 3.1069389792798465 18.023798852941773
            
    with st.container():
        st.write("")
        image_column, text_column = st.columns((1,1))
        
        st.markdown(
                """
            <p style="font-size: 20px;">
            The histogram above displays the number of words employed to describe the products 
            contained in the 'description' variable. Similarly, we use the 
            the median and the first moments of the distribution to characterize it: 
            </p>
            
            - <p style="font-size: 20px;"> Median: 35. 50% of the descriptions are shorter than 35 words. </p>
            - <p style="font-size: 20px;"> Mean: 80.17. There are extremely long descriptions that pull the mean to the left more than the size of the median of 35 words. </p>
            - <p style="font-size: 20px;"> Standard deviation: 115.4. The number of words of the descriptions is considerably spread aroud the median, with the left side of the interval, that is, the mean minus one standard deviation, reaches negative values, suggesting that many products have descriptions with no words, that is, description is missing.   </p>
            - <p style="font-size: 20px;"> Skewness: 3.11. The skewness reconfirms the conclusions when we observe the mean minus the median, that it is strongly right-skewed with rare very long descriptions. 
            - <p style="font-size: 20px;"> Kurtosis: 18.02. Lastly, the kurtosis of 18.02 shows that the distribution is more peaked and has much longer tails than a normal distribution.  </p>

            <p style="font-size: 20px;">
            Theses observations are at the end consistent to the fact that 4886 products
            have no description. These observations led us to concatenate the designation
            and the description variables to obtain only one text variable that we will
            classify using machine-learning techniques, and lastly with deep neural 
            networks when images are included in the classification.
            </p>
            """
            ,
            unsafe_allow_html=True
            )
    
    st.write("---")
    
    with st.container():
        st.header("Correlation matrix of the 'productid', 'imageid', and the word length of 'designation' and 'description' variables of X_train:")

        
        st.markdown(
                """
            <p style="font-size: 20px;">
            Each product is associated with a numerical 'productid' and 'imageid'. 
            These identifiers link the CSV files to a database of images named 
            image_imageid_product_productid.jpg, where each 'productid' corresponds 
            to a unique 'imageid'. This setup allows us to examine correlations between 
            'imageid' and 'productid', as well as their relationships with the word 
            lengths of product titles and descriptions.

 
            </p>
            """
            ,
            unsafe_allow_html=True
            )
            
    with st.container():
        st.write("")
        image_column, text_column = st.columns((2,1))
        with image_column:
            st.image(img_Corr_mat)
        with text_column:
            st.markdown(
                """
            <p style="font-size: 20px;">
            On the left-hand side, we see the correlation matrix for the numerical 
            variables: 'productid', 'imageid', and the word lengths of titles and 
            descriptions. The matrix reveals a strong correlation between 'productid' 
            </p>
            """
            ,
            unsafe_allow_html=True
            )
        st.markdown(
            """
            <p style="font-size: 20px;">
            and 'imageid', suggesting that higher 'productid' codes are likely 
            associated with higher 'imageid' codes. There is also a weak correlation 
            between these codes and the description length, indicating that products 
            with higher codes tend to have longer descriptions.
            Finally, the correlation coefficients for title word length are almost 
            negligible with respect to the other variables, suggesting that title 
            length is largely unrelated to the other metrics.
            </p>
            """
            ,
            unsafe_allow_html=True
        )
    
    st.write("---")
    
