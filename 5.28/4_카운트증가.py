import streamlit as st

숫자 = 0
st.title(숫자)

if st.button("바꾸기"):
    숫자 = 99999
    print(숫자)

if st.button("원레대로"):
    숫자 = 0
    print(숫자)

# ----------------------------------------
if '숫자' not in st.session_state:
    st.session_state.숫자 = 0

st.title(st.session_state.숫자)

if st.button("바꾸기"):
    st.session_state.숫자 = 99999
    print(st.session_state.숫자)
    st.rerun()

if st.button("원래대로"):
    st.session_state.숫자 = 0
    print(st.session_state.숫자)
    st.rerun()

# ----------------------------------------
변수 = st.session_state

if '숫자' not in 변수:
    변수.숫자 = 0

st.title(변수.숫자)

if st.button("바꾸기"):
    변수.숫자 = 99999
    st.rerun()

if st.button("원래대로"):
    변수.숫자 = 0
    st.rerun()


# ----------------------------------------

변수 = st.session_state

if '숫자' not in 변수:
    변수.숫자 = 0

st.title(변수.숫자)

if st.button("바꾸기"):
    변수.숫자 = 변수.숫자 + 1
    st.rerun()
