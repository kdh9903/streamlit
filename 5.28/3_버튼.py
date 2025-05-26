import streamlit as st

버튼 = st.button("버튼")
if 버튼 :
    print("버튼이 눌림!")
    st.success("버튼이 눌림!")

if st.button("버튼2"):
    print("버튼2가 눌림!")

# ----------------------------------------

제목 = st.title("제목")
if st.button("바꾸기"):
    제목.title("1234")

if st.button("원레대로"):
    제목.title("제목")
