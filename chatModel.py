import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
hf_token = os.environ.get("HF_TOKEN")

# Initialize model only once (caching)
@st.cache_resource
def get_model():
    llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-R1-0528",
        task="text-generation",
        huggingface_api_key=hf_token,
        max_new_tokens=1024,
        temperature=0.7
    )
    return ChatHuggingFace(llm=llm)

model = get_model()

# Streamlit UI
st.title("DH-Chatbot")
st.markdown("Chat with your DeepSeek-powered assistant!")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]
if "display_history" not in st.session_state:
    st.session_state.display_history = []

# Chat input box
user_input = st.chat_input("Type your message and press Enter...")

if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.spinner("DeepSeek is thinking..."):
        result = model.invoke(st.session_state.chat_history)
    st.session_state.chat_history.append(AIMessage(content=result.content.split("</think>\n")[-1]))
    st.session_state.display_history.append(("user", user_input))
    st.session_state.display_history.append(("ai", result.content.split("</think>\n")[-1]))

# Display chat history
for speaker, message in st.session_state.display_history:
    if speaker == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("ai").write(message)
