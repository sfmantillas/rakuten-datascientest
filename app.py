import streamlit as st
from PIL import Image

# Define a function to handle page navigation
def main():

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
