# AI-Chatbot
# Overview:
Groq AI Chatbot is an advanced, interactive AI assistant built using Streamlit and powered by Groq's cutting-edge LLM models. Designed to deliver intelligent and dynamic conversations, this chatbot leverages the power of Groq's API to generate human-like responses efficiently. Users can engage with the chatbot seamlessly, choosing between state-of-the-art models like llama3-8b-8192 and mixtral-8x7b-32768 to tailor their experience. With a sleek and intuitive interface, Groq AI Chatbot ensures an effortless and engaging interaction while offering customizable settings, including model selection and response length. Whether for personal use, AI experimentation, or productivity enhancement, this chatbot provides an effective solution for real-time AI-assisted conversations.

# Features:
1) Supports Groq LLM API for generating AI responses
2) Secure API key input via .env file
3) Model selection (llama3-8b-8192, mixtral-8x7b-32768)
4) Adjustable response length (max_tokens)
5) Maintains chat history during a session
6) Sidebar settings for easy configuration

# Installation:
1) Create Environment
   a) conda create -p venv python==3.11 -y b) conda activate venv/
3) Install Dependencies
   a) pip install -r requirements.txt
5) Set Up API Keys
   a) GROQ_API_KEY="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"
7) Running the Application:
streamlit run app.py

# Usage:
1) Enter your Groq API key in the sidebar(already fatched from .env file).
2) Select an AI model (llama3-8b-8192 or mixtral-8x7b-32768).
3) Adjust the word limit (max_tokens).
4) Type a message and press Enter.
5) View AI responses and continue the conversation.
6) Click Start New Conversation to start new conversation

# Folder Structure:
1) ├── app.py # Main Streamlit application
2) ├── requirements.txt # Dependencies
3) ├── .env # API keys (excluded in .gitignore)
4) ├── README.md # Documentation

## The Chatbot Application is Deployed on Streamlit Clouds, can be accessed via link 
https://ai-chatbot-fbqpzprwh6yhmyg98rnqeu.streamlit.app/
