# 🤖 Multimodal AI ChatBot for YouTube Video QA

A multimodal conversational AI chatbot built with Streamlit and LangChain to answer questions about educational YouTube videos. It combines speech recognition, semantic search, and natural language understanding in a sleek, modern UI.

![AI Chatbot Interface](A_2D_digital_image_of_an_AI_chatbot_interface_for_.png)

## 🚀 Live Demo

👉 Try it here: [aiedubot-fzt4db9283sdiryyap6cxz.streamlit.app](https://aiedubot-fzt4db9283sdiryyap6cxz.streamlit.app)

## 🔍 Features

- 🎥 **YouTube Video Transcription**: Automatically transcribes educational videos using OpenAI Whisper.
- 🧠 **Vector Search**: Stores text chunks in ChromaDB with HuggingFace SentenceTransformers.
- 🗨️ **Conversational Agent**: Uses LangChain and OpenAI/GPT to answer user questions contextually.
- 🎤 **Voice Input**: Users can speak their questions using a microphone button.
- 💬 **Chat-style Interface**: Clean, professional chat interface inspired by modern messaging apps.
- 🔁 **Multimodal Interaction**: Text and voice input, text and audio output.
- 📊 **Evaluation Support**: Integrates with LangSmith for agent tracing and performance evaluation.

## 📦 Tech Stack

- Python, Streamlit
- OpenAI Whisper (speech-to-text)
- LangChain Agents
- HuggingFace Transformers & SentenceTransformers
- ChromaDB (vector store)
- LangSmith (for tracing and eval)
- FFmpeg (for video/audio processing)

## 🛠️ Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/ai-chatbot-video-qa.git
   cd ai-chatbot-video-qa
