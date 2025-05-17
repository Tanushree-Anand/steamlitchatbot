import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os
os.environ["GOOGLE_API_KEY"]=st.secrets["GOOGLE_API_KEY"]

# Initialize the chatbot model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Set up the page
st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("💬 Gemini AI Chatbot")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant.")
    ]

# Chat interface
user_input = st.text_input("You:", key="user_input")

if user_input:
    if user_input.lower() == "quit":
        st.write("🔚 Chat ended.")
        st.stop()

    # Append human message
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    # Get model response
    result = llm.invoke(st.session_state.chat_history)

    # Append AI response
    st.session_state.chat_history.append(AIMessage(content=result.content))

# Display chat history
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        st.markdown(f"**You:** {message.content}")
    elif isinstance(message, AIMessage):
        st.markdown(f"**AI:** {message.content}")
