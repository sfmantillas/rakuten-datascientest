import streamlit as st

st.write("Hello :D")

# #Import the necessary modules
from time import time
import joblib
import numpy as np
import pandas as pd
from re import findall
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
# import tensorflow as tf
from tensorflow import float32
from tensorflow import expand_dims
from tensorflow import convert_to_tensor
#from tensorflow.keras import mixed_precision
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications import EfficientNetB0
#from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.efficientnet import preprocess_input
#from sklearn.feature_extraction.text import TfidfVectorizer

# st.write(f'tensorflow: {tf.__version__}')
# st.write(f'streamlit: {st.__version__}')

#"🎈 My new app"
#Img_cover = Image.open("Images/0_FrontCover/FotoJet.jpg")
options = ["Random product", "Classify your product"]

number_to_cat = {
     0: "10: Specialized Literature: music, physics",
     1: "40: Videogames, PS, XBox, Nintendo, cables",
     2: "50: Tech, controllers, fans, cables, cameras",
     3: "60: Console videogames, vintage and modern",
     4: "1140: Figurines, funkos, collectionable mugs",
     5: "1160: Collection cards: Pokemon, FIFA, Yu-Gi-Oh",
     6: "1180: Figurines, table games, miscelaneous",
     7: "1280: Kids: Toys, dolls, puff bears",
     8: "1281: Toys, cards (Yu-Gi-Oh), babys",
     9: "1300: Drones",
    10: "1301: Kids and babys toys, clothes, shoes",
    11: "1302: Outdoor toys, trampolines, gym, sports",
    12: "1320: Babys: deco, carts, backpacks, diappers",
    13: "1560: Home deco and furniture",
    14: "1920: Cussions. ",
    15: "1940: Food, coffee, gums, chiclets, mermalade",
    16: "2060: Photography, Christmas, deco, illumination",
    17: "2220: Pet toys, collars, cussions, pots, brushes",
    18: "2280: Magazines, science, art, historical journals",
    19: "2403: Books, comics, mangas",
    20: "2462: Console Videogames, consoles and games",
    21: "2522: Papershop, A5 size, pencils, notebooks",
    22: "2582: Outdoor furniture: tables, deco, plants",
    23: "2583: Pools, pumps, water cleaning",
    24: "2585: Bricolage, house repair, cleaning",
    25: "2705: Books, novels",
    26: "2905: PC Videogames"
}

## Image pre-processing

# Function for image displaying
def show_image(image_array):
    plt.imshow(image_array)
    plt.axis('off')  # Hide axis
    plt.show()
    return None

# Function for square padding
def pad_to_square(image):
    height, width, channels = image.shape
    max_dim = max(height, width)

    pad_height = max_dim - height
    pad_width = max_dim - width

    pad_top = pad_height // 2
    pad_bottom = pad_height - pad_top
    pad_left = pad_width // 2
    pad_right = pad_width - pad_left

    padded_image = np.full((max_dim, max_dim, channels), 255, dtype=np.uint8)
    padded_image[pad_top:pad_top+height, pad_left:pad_left+width, :] = image

    return padded_image

# Function for preprocessing an image using PIL
def preprocess_image(image, target_size=(224, 224)):
    image = np.array(image)
    image = pad_to_square(image)
    image = Image.fromarray(image)
    image = ImageOps.fit(image, target_size, Image.LANCZOS)
    image = np.array(image) / 255.0
    return image

# Function for preprocessing an image using TensorFlow
def load_and_preprocess_image(image):
    image = preprocess_image(image)
    image = convert_to_tensor(image, dtype=float32)

    # Apply preprocessing input required by EfficientNet
    image = preprocess_input(image)
    return image

# Function for extracting features from a single image
def extract_features_from_image(image, model):
    # Load and preprocess the image
    image = load_and_preprocess_image(image)

    # Add a batch dimension since the model expects input shape (batch_size, height, width, channels)
    image = expand_dims(image, axis=0)

    # Extract features using the model
    features = model.predict(image)

    return features

######## Function for building and compiling the EfficientNetB0 model
def build_image_model(input_size=(224, 224, 3)):
    base_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=input_size)
    x = GlobalAveragePooling2D()(base_model.output)
    model = Model(inputs=base_model.input, outputs=x)

    # Compile
    optimizer = 'adam'

    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    return model

image_model = build_image_model(input_size=(224, 224, 3))

## Text preprocessing

# Manually define a set of stopwords
# These stopwords are common words in English and French that do not add significant meaning to the text
manual_stopwords = set("""
a about above after again against all am an and any are aren't as at be because been before being below between both but by can't cannot could couldn't did didn't do does doesn't doing don't down during each few for from further had hadn't has hasn't have haven't having he he'd he'll he's her here here's hers herself him himself his how how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most mustn't my myself no nor
un une des du le la les et à en dans par pour au aux avec ce cette ces comme il elle ils elles que qui sur son sa ses leur leurs où donc ne pas ni non plus on nous vous votre vos c'est ce sont car même si mais ou où or ni soit ni puis
""".split())

# Define a function to preprocess text without using NLTK
# This function tokenizes the text into words, converts to lowercase, removes stopwords, and filters out short words
def simple_preprocess_text(text):
    # Tokenize the text into words and convert to lowercase
    tokens = findall(r'\b\w\w+\b', text.lower())
    # Filter out stopwords and short words (length <= 2)
    filtered_tokens = [word for word in tokens if word not in manual_stopwords and len(word) > 2]
    return ' '.join(filtered_tokens)

# Function to merge text columns and preprocess them
def preprocess_text_data(designation, description):
    # Combining 'designation' and 'description' columns into one 'text' column
    text = designation + ' ' + description

    # Applying the text preprocessing function to the 'text' column and creating a new column 'processed_text'
    text = simple_preprocess_text(text)

    # Returning the updated DataFrames with added columns
    return text

## Model and vectorizer import
model = load_model('Models/dnn_classifier.h5')#PATH/DEINES/LETZTEN/MODELLS
vectorizer = joblib.load('Models/Tfidf_Vectorizer.joblib')













def app():

    st.title("Proof of concept: Try the model yourself :smile:")

    with st.container():
        st.markdown(
            """
            <p style="font-size: 20px;">
            Choose an option from the drop-down menu below. You can either:
            </p>

             - <p style="font-size: 20px;">Classify a random product from our samples.
            </p>

             - <p style="font-size: 20px;">Upload your own product's name, description, and image.
            </p>
            """
            ,
            unsafe_allow_html=True
        )

        # st.markdown(
        #     """
        #     <p style="font-size: 20px;">
        #     Below you find a drop menu where you can select between
        #     proving the classifier with a random product from our
        #     samples, or you can load yourself the designation, description
        #     and the image of a product of your preference.
        #     </p>
        #     """
        #     ,
        #     unsafe_allow_html=True
        #     )
    selected_option = st.selectbox("Select an option:", options)

    if selected_option == options[0]:
        with st.container():
            st.header("Try with a random product:")

            st.markdown(
            """
            <p style="font-size: 20px;">
            Press the button to randomly select a product already charged in your
            database to display its designation, description, image and category
            predicted using our model.
            </p>
            """
            ,
            unsafe_allow_html=True
            )

            # Load dataset containing samples
            products = pd.read_csv("./Datasets/POC_products.csv", encoding='cp1252').fillna("")

            # Set new random seed.
            np.random.seed(int(time()))

            #Button to generate a random product id
            if st.button("Select a random product"):

                random_id = np.random.randint(19)
                #st.write(f"Random Integer: {random_int}")

                ## Extract
                product_designation = products.designation[random_id]
                product_description = products.description[random_id]

                ## Importing and transforming the image
                path_product_img = "Images/Images_for_POC/POC_image_{}.jpg".format(random_id)
                product_image = Image.open(path_product_img).convert('RGB')

                st.subheader("**Designation:** {}".format(product_designation))
                image_column, text_column = st.columns((1,1))
                with image_column:
                    st.image(product_image)
                with text_column:
                    st.markdown("**Description:** {}".format(product_description))

                product_text = preprocess_text_data(product_designation, product_description)
                product_text_tfidf = vectorizer.transform([product_text]).toarray()
                product_img_features = extract_features_from_image(product_image, image_model)

                product_cat = model.predict([product_text_tfidf, product_img_features], batch_size=32)
                product_cat = number_to_cat[product_cat.argmax()]
                st.success("**Product category:** {}".format(product_cat))

#############################################
    elif selected_option == options[1]:
        #st.write("---")
        with st.container():
            st.header("Upload your own product:")

            st.markdown(
            """
            <p style="font-size: 20px;">
            In the next boxes you can upload the designation, the description and
            the image of your product. It is strongly recommended you translate
            your texts to French:
            </p>
            """
            ,
            unsafe_allow_html=True
            )

            product_designation = st.text_input("Enter the designation of your product (mandatory): ")
            product_description = st.text_area("Enter the description of your product (optional): ")
            product_image = st.file_uploader("Upload the image of your produc (mandatory)t: ")
            if product_designation and product_image is not None:
                st.success("Your product was uploaded successfully. Here is your input:")
                st.subheader("**Designation:** {}".format(product_designation))
                image_column, text_column = st.columns((1,1))
                with image_column:
                    st.image(product_image)
                with text_column:
                    st.markdown("**Description:** {}".format(product_description))

                product_image = Image.open(product_image).convert('RGB')

                product_text = preprocess_text_data(product_designation, product_description)
                product_text_tfidf = vectorizer.transform([product_text]).toarray()
                product_img_features = extract_features_from_image(product_image, image_model)

                product_cat = model.predict([product_text_tfidf, product_img_features], batch_size=32)
                product_cat = number_to_cat[product_cat.argmax()]
                st.success("**Product category:** {}".format(product_cat))
                # print(product_cat.argmax())
                # print(number_to_cat[product_cat.argmax()])





#############################################