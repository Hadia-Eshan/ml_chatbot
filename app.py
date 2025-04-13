# app.py
import streamlit as st
import joblib
from utils import preprocess, responses

# Load model and vectorizer
model = joblib.load("chatbot_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Page setup
st.set_page_config(page_title="Restaurant Chatbot", page_icon="🍽️")
st.title("🍽️ Restaurant Chatbot")

# Initialize chat history as list of (user, bot) pairs
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # each item = (user_msg, bot_reply)

# Input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("👤 Ask something:", placeholder="Type your message...")
    submitted = st.form_submit_button("Send")

# Handle input
if submitted and user_input:
    processed = preprocess(user_input)
    intent = model.predict(vectorizer.transform([processed]))[0]
    bot_reply = responses.get(intent, f"(Intent: {intent}) Sorry, I didn’t understand.")

    # Save (user, bot) as a pair
    st.session_state.chat_history.insert(0, (user_input, bot_reply))

# Display all chat history
for user_msg, bot_msg in st.session_state.chat_history:
    st.markdown(f"**🧑 You:** {user_msg}")
    st.markdown(f"**🤖 Bot:** {bot_msg}")
    st.markdown("---")
