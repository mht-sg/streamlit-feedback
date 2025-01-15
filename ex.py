import streamlit as st
from streamlit_feedback import streamlit_feedback


st.title("💬 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

messages = st.session_state.messages


_submit_feedback = lambda user_response, emoji=None: st.toast(
    f"Feedback submitted: {user_response}", icon=emoji
)


for n, msg in enumerate(messages):
    st.chat_message(msg["role"]).write(msg["content"])

    if msg["role"] == "assistant" and n > 1:
        feedback_key = f"feedback_{int(n/2)}"

        if feedback_key not in st.session_state:
            st.session_state[feedback_key] = None

        streamlit_feedback(
            feedback_type="thumbs",
            optional_text_label="Please provide extra information",
            review_on_positive=False,
            on_submit=_submit_feedback,
            key=feedback_key,
        )

if prompt := st.chat_input():
    messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = prompt
    st.session_state["response"] = response.choices[0].message.content
    with st.chat_message("assistant"):
        messages.append({"role": "assistant", "content": st.session_state["response"]})
        st.write(st.session_state["response"])
        st.rerun()
