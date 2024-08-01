import streamlit as st
from PIL import Image

Img_portrait_a = Image.open("Images/0_FrontCover/collage_padding_1160.png")
Img_portrait_b = Image.open("Images/0_FrontCover/collage_padding_1920.png")
Img_portrait_c   = Image.open("Images/0_FrontCover/collage_padding_1560.png")

# Define a function to handle page navigation
def main():
    st.image(Img_portrait_c)
#    with st.container():
#        st.write("")
#        image_column_a, image_column_b, image_column_c = st.columns((1,2,1))
#        with image_column_a:
#            st.image(Img_portrait_a)
#        with image_column_a:
#            st.image(Img_portrait_b)
#        with image_column_a:
#            st.image(Img_portrait_c)

    st.title("Classification of Rakuten e-commerce products")

    # Create a selectbox for page selection
    page = st.sidebar.selectbox("Select a page", ["Home", "Page 1", "Page 2"])

    if page == "Home":
        import page0
        page0.app()
        # st.write("Welcome to the Home Page!")
        # You can add more content here for the Home page
    elif page == "Page 1":
        import page1
        page1.app()
    elif page == "Page 2":
        import page2
        page2.app()

if __name__ == "__main__":
    main()
