import streamlit as st
from streamlit_chat import message as st_message
import time

# Initialize session state variables
if 'history' not in st.session_state:
    st.session_state.history = []
if 'user_input' not in st.session_state:
    st.session_state.user_input = ''
if 'bot_response' not in st.session_state:
    st.session_state.bot_response = ''
if 'loading' not in st.session_state:
    st.session_state.loading = False

# Function to simulate bot response
def get_bot_response(query):
    # time.sleep(2)  # Simulate a delay for loading indicator
    return "This is a placeholder response."

# Function to handle user input
def handle_input():
    st.session_state.loading = True
    user_query = st.session_state.user_input
    st.session_state.history.append(("User", user_query))
    st.session_state.bot_response = get_bot_response(user_query)
    st.session_state.history.append(("Bot", st.session_state.bot_response))
    st.session_state.user_input = ''  # Clear the input box
    st.session_state.loading = False

# Sidebar to display chat history
st.sidebar.title("Chat History")
for index, (role, msg) in enumerate(st.session_state.history):
    if role == "User":
        st.sidebar.write(f"**{role}**: {msg}")
    else:
        st.sidebar.write(f"**{role}**: {msg}")

# Main area for chat input and display
st.title("Guidepad Agent")
st.write("Hi, How can I assist you?")

# Display chat history in the main area
for index, (role, msg) in enumerate(st.session_state.history):
    if role == "User":
        st_message(msg, is_user=True, key=f"user_{index}")
    else:
        st_message(msg, key=f"bot_{index}")

# Input area for user query
user_input = st.text_input("You:", value=st.session_state.user_input, key="user_input", on_change=handle_input)

# Display loading indicator
if st.session_state.loading:
    with st.spinner("Loading Response..."):
        time.sleep(2)  # Simulate loading time

# Run the handle_input function when user hits enter
if user_input and not st.session_state.loading:
    handle_input()
