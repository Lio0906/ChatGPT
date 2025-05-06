

    for message in st.session_state.chat_history:
        if message["role"] != "system":
            st.markdown(f"**{message['role']}**：{message['content']}")
