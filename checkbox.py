# Query: checkbox.py
# ContextLines: 1

No Resultsimport streamlit as st

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
