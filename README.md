![AIEduBot UI](assets/aiedubot_ui.png)


# 🤖 AIEduBot: Multimodal AI ChatBot for YouTube Video QA

Welcome to **AIEduBot** — a multimodal, interactive chatbot designed to answer user questions about **educational YouTube videos** related to Artificial Intelligence. The system extracts insights from video content using automatic speech recognition, chunking, embedding, and a LangChain-powered QA pipeline.

🔗 **Live Demo**: [aiedubot-fzt4db9283sdiryyap6cxz.streamlit.app](https://aiedubot-fzt4db9283sdiryyap6cxz.streamlit.app)

---

## 🎯 Project Goal

The aim of AIEduBot is to improve **accessibility** and **interactivity** with educational content by enabling users to:
- Ask natural language questions about YouTube videos
- Receive accurate, contextual answers
- Interact using **text and voice** input/output

---

## 🧱 Architecture Overview

```
+----------------+       +----------------+       +----------------------+
|  YouTube URL   |  -->  |  Whisper ASR   |  -->  |  Text Chunking       |
+----------------+       +----------------+       +----------------------+
                                                        |
                                                        v
                                               +----------------------+
                                               | Sentence Embeddings  |
                                               | (HuggingFace + SBERT)|
                                               +----------------------+
                                                        |
                                                        v
                                               +----------------------+
                                               |  ChromaDB Vector DB  |
                                               +----------------------+
                                                        |
                                                        v
    +---------+   +-------------+   +--------------------+   +-----------------+
    | Text/   |   | Streamlit   |-->| LangChain QA Agent |-->| OpenAI LLM      |
    | Voice   |   | Frontend UI |   +--------------------+   +-----------------+
    | Input   |   +-------------+   | LangSmith Tracing  |
    +---------+                   +------------------------+
```

---

## 🧪 Methodology

### 1. Data Ingestion:
- YouTube audio extracted and transcribed using **OpenAI Whisper**.

### 2. Preprocessing:
- Transcripts are chunked into overlapping text windows.
- Sentence embeddings generated using **`all-MiniLM-L6-v2`** (via SentenceTransformers).

### 3. Vector Store:
- Embeddings stored in **ChromaDB** for semantic search and retrieval.

### 4. QA Pipeline:
- **LangChain Retriever-Reader agent** fetches relevant chunks and generates answers via OpenAI's `gpt-3.5-turbo`.

### 5. Evaluation:
- System behavior traced and evaluated using **LangSmith**.

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/aiedubot.git
cd aiedubot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Ensure **FFmpeg** is installed for audio handling:

```bash
# Ubuntu
sudo apt install ffmpeg

# MacOS (using Homebrew)
brew install ffmpeg
```

### 3. Run the app

```bash
streamlit run app.py
```

---


## ⚙️ Configuration

Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key
```

Make sure `requirements.txt` is installed. Key libraries include:

- `openai`
- `streamlit`
- `whisper`
- `sentence-transformers`
- `chromadb`
- `langchain`
- `pydub`


---

## 💡 Usage Guide

1. Launch the Streamlit app
2. Paste a YouTube video URL (educational content only)
3. Ask questions via **text or voice**
4. Receive answers and hear them read aloud

Example Questions:
- "What is supervised learning?"
- "How does backpropagation work?"
- "What was the key takeaway of this lecture?"

---

## 🚀 Future Improvements

- Summarization per section
- Multilingual support
- Integration with other LLMs
- Chat memory for multi-turn interactions

---

## 📄 Report

A companion **PDF report** is available for download, summarizing all methodology and design decisions. *(You can generate this automatically or contact the developer for a copy.)*

---

## 🧑‍💻 Author

Developed by EchoLogic Grop 
 [Abrar Alanazi
 Albandari Altalh] as part of the Ironhack Final Project — 2025 AI Engineer Bootcamp.  
Feel free to contribute, fork, or reach out for collaborations.

