import streamlit as st
import pandas as pd
from PIL import Image

#"🎈 My new app"
Img_cover = Image.open("Images/0_FrontCover/FotoJet.jpg")

def app():
    
    st.title("Business and scientific conclusions")
    st.image(Img_cover)

    with st.container():
        #st.write("---")
        st.header("Members")
        st.subheader(
            """
            - Sajad Bairampour  
            """
        )
        st.subheader(
            """
            - Lakshmi Narasimha Priyatham Kumanduri
            """
        )
        st.subheader(
            """
            - Sebastián Felipe Mantilla-Serrano
            """
        )
        st.subheader(
            """
            - Vitalij Merenics
            """
        )
        st.subheader(
            """
            - Noel Nickel
            """
        )
#        st.write(
 #           """
 #           - Sajad Bairampour
 #           - Lakshmi Narasimha Priyatham Kumanduri
 #           - Sebastián Felipe Mantilla-Serrano
 #           - Vitalij Merenics
  #          - Noel Nickel
   #         """
    #        )

 
#End")
