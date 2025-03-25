import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Default API Key from .env (if available)
default_api_key = os.getenv("GROQ_API_KEY")

# Initialize session state for chat history & input control
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "last_input" not in st.session_state:
    st.session_state.last_input = ""

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Please respond to user queries."),
    ("user", "Question: {question}")
])

def generate_response(question, api_key, model, max_tokens):
    if not api_key:
        return "⚠️ Please enter a valid Groq API key in the sidebar."

    try:
        # Initialize Groq LLM
        llm = ChatGroq(
            model=model,
            groq_api_key=api_key,
            max_tokens=max_tokens
        )

        # Chain the prompt with LLM and output parser
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser
        answer = chain.invoke({'question': question})
        return answer

    except Exception as e:
        return f"🚨 API Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="Groq AI Chatbot", page_icon="🤖")

st.title("🤖 Groq AI Chatbot")

# Sidebar Settings
with st.sidebar:
    st.title("⚙️ Settings")
    api_key = st.text_input("🔑 Groq API Key:", type="password", value=default_api_key or "")
    model = st.selectbox("🧠 Choose Model", ["llama3-8b-8192", "mixtral-8x7b-32768"])
    max_tokens = st.slider("📝 Set Word Limit", min_value=50, max_value=4096, value=150)

    if st.button("🆕 Start New Conversation"):
        st.session_state.chat_history = []
        st.session_state.last_input = ""  # Reset last input
        st.rerun()  # Refresh the app to clear chat history

# Display Chat History
st.write("### 💬 Chat Below:")

for role, text in st.session_state.chat_history:
    st.write(f"**{role}:** {text}")

# User Input Field (Always Below Chat)
user_input = st.text_input("🗨️ Type your message and press Enter:", value="", key="user_input")

# Process input only if it's different from the last one
if user_input and user_input != st.session_state.last_input:
    if not api_key.strip():
        st.warning("⚠️ Please enter a Groq API key in the sidebar.")
    else:
        with st.spinner("⏳ Generating response..."):
            response = generate_response(user_input, api_key, model, max_tokens)

            # Save conversation to history
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("AI", response))

            # Store last input to prevent duplicate execution
            st.session_state.last_input = user_input

            # Refresh to update chat display
            st.rerun()