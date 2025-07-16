import streamlit as st

세션=st.session_state

if "채팅" not in st.session_state:
    세션.채팅 = []

with st.form("채팅_폼", clear_on_submit=True):
    입력 = st.text_input("채팅을 입력하세요.")
    if st.form_submit_button("입력") and 입력:
        세션.채팅.append(입력)




if st.button("🗑️ 전체 삭제"):
    세션.채팅.clear()

st.markdown("### 💬 채팅 내역")
for 메시지 in 세션.채팅:
    st.write(메시지)
