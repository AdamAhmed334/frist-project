import streamlit as st
from groq import Groq
st.title("Adamh_app")
cilent = Groq(api_key=st.secrets["qroc_api-key"])

text = st.text_area("تلخيص ما كتبت",hight = 2000)
if st.button("لخص"):
  if len(text.splite()) < 10:
    st.wraning("النص قصير اكتب نص اكبر")
