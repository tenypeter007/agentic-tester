import streamlit as st
from agent import generate_test_for_url

st.title("Agentic Web Tester")
url = st.text_input("Enter website URL to test")

if st.button("Generate and Run Test"):
    with st.spinner("Running agent..."):
        result = generate_test_for_url(url)
    st.subheader("Agent Output")
    st.code(result)