"あなた：", key="user_input")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        with st.spinner("考え中..."):
            import openai

# ここを追加！
client = openai.OpenAI()

# 書き方を新しくする！
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=chat_history,
    temperature=0.9,
    max_tokens=1000
)
        reply = response.choices[0].message.content
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.experimental_rerun()

    for message in st.session_state.chat_history:
        if message["role"] != "system":
            st.markdown(f"**{message['role']}**：{message['content']}")
