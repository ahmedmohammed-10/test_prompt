import streamlit as st
from controller.ask_controller import ask


st.title("Chat With DMS")

st.markdown("""
<style>
    .stTextInput > div > input {
        width: 100%;
        font-size: 24px; /* Font size for better readability */
    }
    .user-textarea {
        height: 100px; /* Height for the User text area */
    }
    .system-textarea {
        height: 800px; /* Height for the System text area */
    }
    .stButton button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-size: 24px; /* Font size for better readability */
    }
</style>
""", unsafe_allow_html=True)

# Input for the query
cohere_key = st.text_area("Cohere_Key:", "", key="cohere_key")
user = st.text_area("User:", "", height=50, key="user")
system = st.text_area("System:", "", height=200, key="system")

# Create a button for sending the messages
if st.button("Send"):
    if user and system and cohere_key:
        response = ask(user, system, cohere_key)
        st.write(f"Response: {response}")
    else:
        st.write("Please enter both messages.")
