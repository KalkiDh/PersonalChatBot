# DeepSeek Chatbot

A conversational AI chatbot powered by [DeepSeek R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528), built with [LangChain](https://www.langchain.com/) and a modern [Streamlit](https://streamlit.io/) frontend. The bot maintains chat context and leverages Hugging Face’s API for robust, context-aware conversations.

---

## 📸 Project Screenshots

<!-- 
Add your project screenshots or GIFs below. 
For example:
(images/Sample.png)
![Conversation Example](images/conversation.gif)
-->

---

## 🚀 Features

- 🤖 **Conversational AI**: Chat with a powerful LLM via a friendly web interface  
- 🧠 **Contextual Memory**: Maintains chat history for contextual responses  
- ⚡ **Streamlit Frontend**: Clean, interactive chat UI  
- 🔒 **Secure API Key Management**: Uses `.env` for Hugging Face secrets  
- 🛠️ **Easy Customization**: Swap LLMs or tweak parameters as needed

---

## 🛠️ Getting Started

### 1. Clone the Repository

git clone https://github.com/yourusername/deepseek-chatbot.git
cd deepseek-chatbot

### 2. Set Up Environment

Create a `.env` file in the project root:

HF_TOKEN=your_huggingface_api_key_here


Get your Hugging Face API key from [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).

### 3. Install Requirements

pip install -r requirements.txt

### 4. Run the Streamlit App

streamlit run app.py

---

## 💡 Usage

- Type your message in the chat input box and press Enter.
- The chatbot will respond, maintaining context throughout the session.
- To end the session, simply close the browser tab or stop the Streamlit server.

---

## 📂 Project Structure

deepseek-chatbot/
│
├── app.py # Streamlit frontend
├── chatModel.py # (Optional) CLI backend script
├── requirements.txt # Python dependencies
├── .env # Hugging Face API key (not committed)
└── README.md # This file


---

## 📋 Requirements

- Python 3.8+
- See `requirements.txt` for package details:
    - langchain >= 0.3.0
    - langchain-core >= 0.3.0
    - langchain-huggingface >= 0.0.1
    - huggingface_hub >= 0.23.0
    - python-dotenv >= 1.0.0
    - streamlit >= 1.32.0

---

## ⚙️ Customization

- **Change the LLM**: Swap the `repo_id` in `app.py` to use a different Hugging Face model.
- **Adjust Model Parameters**: Edit `temperature`, `max_new_tokens`, etc., in the model initialization.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- [DeepSeek-AI](https://huggingface.co/deepseek-ai) for the LLM
- [LangChain](https://www.langchain.com/) for orchestration
- [Streamlit](https://streamlit.io/) for the frontend
- [Hugging Face](https://huggingface.co/) for model hosting

---

**Enjoy chatting with your DeepSeek-powered assistant! 🚀**
