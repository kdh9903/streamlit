import streamlit as st

if 'count' not in st.session_state:
    st.session_state.count = 0

st.title(st.session_state.count)
if st.button("카운트asd 증가"):
    st.session_state.count += 1