import streamlit as st
from groq import Groq
import PyPDF2
import io
st.title("app")
cilent = Groq(api_key=st.secrets["qroq_key"]) 
uploaded_files = st.file_uploader("Uplode",type =["pdf"])
if uploaded_files is not None:
  pdfReader = PyPDF2.PdfReader(io.BytesIO(uploaded_files.read()))
  page_text = ""
  for pages in pdf_reder.pages:
    page_text += page.extract_text() or ""
else:
  page_text = ""
text = st.text_area("تلخيص ما كتبت",height = 200,value = page_text)
if st.button("لخص"):
  if len(text.split()) < 10:
    st.warning("النص قصير اكتب نص اكبر")
  else:
    with st.spinner("جار تلخيص"):
      arcbic_letter = 0
      for c in text:
        if '\u0600' <= c <= '\u06FF':
          arcbic_letter+= 1
      if arcbic_letter > 12:
        language = "العربية"
      else:
        language = "English"
      chatbot = cilent.chat.completions.create(
        model = "llama-3.3-70b-versatile",  
        messages = [{"role":"system","content":f"You are a helpful assistant for kid. Summarize the text in 3-4 sentences. You MUST respond in {language} only"},
                   {"role":"user","content":text}]
      )
      st.success(chatbot.choices[0].message.content)
