import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"
st.title("Check English grammar Correct and Simple! 😄")


name = st.text_area("Sentence", disabled=False)

check = st.button("🤖 Check my grammar", type="primary", disabled=False)

if check:
    with st.spinner('Wait for it...'):
        result = requests.get(url=BACKEND_URL + "/correct-sentence?q="+name)
    st.success(str(result.content, 'utf-8'))
