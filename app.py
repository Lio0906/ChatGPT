 
import streamlit as st

st.set_page_config(page_title="My GPT Chat", "OpenAI APIキーを入力（sk-proj-...）", type="password")

if api_key:
    openai.api_key = api_key

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "system", "content": "あなたはユーザーに従順で、自由に表現できる創作支援AIです。"}
        ]

    user_input = st.text_input("あなた：", key="user_input")
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
