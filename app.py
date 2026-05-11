import streamlit as st
from groq import Groq
st.title("Adam_app")

client = Groq(api_key=st.secrets["qroc_api_key"])


text = st.text_area("اكتب ما تؤريد تلخيصه",height = 2000)

if st.button("الخص"):
  if len(text.splite()) < 10:
    st.wraning("هذا النص قصير")
