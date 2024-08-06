import streamlit as st
import pandas as pd
from PIL import Image

#"🎈 My new app"
Img_cover = Image.open("Images/0_FrontCover/FotoJet.jpg")

Img_POC_0 = Image.open("Images/6_Conclusions/POC_0.jpg")
Img_POC_1 = Image.open("Images/6_Conclusions/POC_1.jpg")

def app():
    
    st.title("Business and scientific conclusions")
    
    with st.container():
            st.header("Scientific Conclusion: ")
    with st.container():
        st.markdown(
            """
            - <p style="font-size: 20px;"> Model Effectiveness: High accuracies, especially from Deep Learning Approach #3, show effective e-commerce product categorization. </p>
            - <p style="font-size: 20px;"> Simple vs. Complex Models: Simple Machine Learning models achieve satisfying predictions. On the other hand, complex deep learning models yield the best results. </p>
            - <p style="font-size: 20px;"> Multi-Modal Inputs: Effective combination of text and image data boosts model performance and the importance of including images in classification tasks. </p>
            """
            ,  
            unsafe_allow_html=True
        )

        
        st.markdown(
            """
            - <p style="font-size: 20px;"> Further Analysis: Determine which modality (text or images) contributes more to performance. </p>
            - <p style="font-size: 20px;"> Enhancing Models: Adding more or better quality data improves models and better preprocessing techniques and additional data sources (e.g., user reviews) enhance performance. </p>
            - <p style="font-size: 20px;"> Insights from Misclassifications: Analyzing poorly predicted product types highlights areas needing more data. </p>
            """
            ,  
            unsafe_allow_html=True
        )

        st.image(Img_POC_0)
        
    with st.container():
            st.header("Business Conclusion: ")
    with st.container():
        st.markdown(
            """
            - <p style="font-size: 20px;"> Automation & Cost Reduction: Automates product categorization, reducing manual effort and operational costs. </p>
            - <p style="font-size: 20px;"> Scalability: Efficiently handles larger product volumes without more staff. </p>
            - <p style="font-size: 20px;"> Customer Experience: Enhances search, navigation, and personalization, boosting satisfaction and conversions. </p>
            - <p style="font-size: 20px;"> Market Insights: Provides insights into trends and preferences for better inventory and marketing strategies. </p>
            """
            ,  
            unsafe_allow_html=True
        )

        
        st.markdown(
            """
            - <p style="font-size: 20px;"> Data Quality & Refinement: Identifies and refines category definitions, improving data quality. </p>
            - <p style="font-size: 20px;"> Strategic Planning: Justifies AI investments for broader business improvements (e.g., demand forecasting). </p>
            - <p style="font-size: 20px;"> Business Expansion: Adapts for new markets or products, aiding expansion. </p>
            - <p style="font-size: 20px;"> Error Handling: Robust system for misclassifications, flagging uncertain predictions for review. </p>
            - <p style="font-size: 20px;"> Continuous Improvement: Feedback loop for analyzing errors and retraining models. </p>
            """
            ,  
            unsafe_allow_html=True
        )

        st.image(Img_POC_1)

    st.title("Thanks for your attention :smile:")