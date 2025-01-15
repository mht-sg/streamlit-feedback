from streamlit_feedback import chatbot_thumbs_app
from streamlit_feedback import streamlit_feedback


chatbot_thumbs_app(
    streamlit_feedback=streamlit_feedback(
        feedback_type="thumbs",
        optional_text_label="Kommentar til feedback her",
    ),
    debug=True,
)
