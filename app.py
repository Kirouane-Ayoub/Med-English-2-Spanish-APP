import streamlit as st 
from lib.utils import * 
st.set_page_config(page_title='Medical-en2es-Translate', layout="wide")

st.header(":hand: Welcome To Medical-en2es medical Machine Translation system: ")
st.info("""**Medical_en2es_Translate** is a specialized neural machine translation model designed for translating medical 
content from English to Spanish. It has been fine-tuned to cater specifically to the medical 
domain, ensuring accurate and contextually relevant translations for healthcare professionals and 
researchers.""")


col1 , col2 = st.columns(2)
with col1 :  
    st.header("Input your Sentence here:")
    prompt = st.text_input(" ")
    st.info("Press Enter To apply")
with col2 : 
    st.header("The translation of your Sentence is :")
    if prompt: 
        result= run(prompt=prompt)
        st.text_area(" ", value=result)
