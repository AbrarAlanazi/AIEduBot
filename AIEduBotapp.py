import streamlit as st
from streamlit_chat import message
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

# Manually set API key here
OPENAI_API_KEY = "OPENAI_API_KEY"

# Set page configuration
st.set_page_config(page_title="AIEduBot", layout="wide")

# Sidebar branding
with st.sidebar:
    st.image("https://i.pinimg.com/736x/f2/ee/25/f2ee25161a920fe0cbbbefdda8c0f934.jpg", width=200)
    st.markdown("## AIEduBot", unsafe_allow_html=True)
    st.markdown("Ask me about the AI video content!", unsafe_allow_html=True)
    st.markdown("---")
   

# Initialize the language model
llm = ChatOpenAI(temperature=0.2, model="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)

# --- Define video_qa_tool logic ---
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory="db", embedding_function=embedding_model)

retriever = vectordb.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0.2, openai_api_key=OPENAI_API_KEY),
    retriever=retriever,
    return_source_documents=False
)

def video_qa_tool(query: str) -> str:
    return qa_chain.run(query)

# Define LangChain Tool
tools = [
    Tool(
        name="video_qa_tool",
        func=video_qa_tool,
        description="Use this tool to answer questions about video content on AI."
    )
]

# Initialize memory and agent
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent = initialize_agent(tools, llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, memory=memory)

# Session state initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
st.markdown("### Ask AIEduBot about AI Concepts in the Videos:")
for i, chat in enumerate(st.session_state.messages):
    message(chat["content"], is_user=chat["role"] == "user", key=str(i), avatar_style="bottts")

# User input
user_query = st.chat_input("Type your question here...")

if user_query:
    # Show user's message
    st.session_state.messages.append({"role": "user", "content": user_query})
    message(user_query, is_user=True, key=str(len(st.session_state.messages) - 1))

    # Get response from LangChain agent
    with st.spinner("Thinking..."):
        response = agent.run(user_query)

    # Show agent's response
    st.session_state.messages.append({"role": "ai", "content": response})
    message(response, key=str(len(st.session_state.messages) - 1))
