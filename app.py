import streamlit as st
from PIL import Image

# Define a function to handle page navigation
def main():

    # Create a selectbox for page selection
    page = st.sidebar.selectbox("Select a page", ["Welcome", 
    "Project description", "Data Exploration", 
    "Preprocessing", "ML algorithms", 
    "CNN model", "Conclusions"])

    if page == "Welcome":
        import page0
        page0.app()
        # st.write("Welcome to the Home Page!")
        # You can add more content here for the Home page
    elif page == "Project description":
        import page1
        page1.app()
    elif page == "Data Exploration":
        import page2
        page2.app()
    elif page == "Preprocessing":
        import page3
        page3.app()
    elif page == "ML algorithms":
        import page4
        page4.app()
    elif page == "CNN model":
        import page5
        page5.app()
    elif page == "Conclusions":
        import page6
        page6.app()

if __name__ == "__main__":
    main()
