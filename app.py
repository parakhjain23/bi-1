import streamlit as st
from langchain import LLMMathChain, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
import os
from langchain.llms import OpenAI
from langchain.chains import LLMMathChain
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

# Set environment variables
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]


# Initialize LLM with OpenAI API
llm = ChatOpenAI(model="gpt-4o", openai_api_key= OPENAI_API_KEY)

# Initialize Math Chain
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

# Streamlit User Interface
st.title("Chat with your Database")

# File uploader for the database
db_file = st.file_uploader("Upload your SQLite database", type=["db"])
if db_file is not None:
    # Save uploaded file to a temporary file if needed
    with open("temp_uploaded_db.db", "wb") as f:
        f.write(db_file.getbuffer())
    db_path = "sqlite:///temp_uploaded_db.db"
else:
    # Provide a default or example database if no file is uploaded
    db_path = "sqlite:///chinook.db"  # Example path

# Connect to the database
db = SQLDatabase.from_uri(db_path)

# Create the database chain
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# Define the tools available for the agent
tools = [
    Tool(
        name="MathTool",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math"
    ),
    Tool(
        name="Product_Database",
        func=db_chain.run,
        description="useful for when you need to answer questions about products."
    )
]

# Create the agent
agent = initialize_agent(
    tools=tools, llm=llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)

st.markdown(
    '<a href="https://drive.google.com/file/d/1EFxg66ffoRuEMc1mixbHhuzaKkv7kENn/view" download="sample_database.db">Download a sample database</a>',
    unsafe_allow_html=True
)

# User input for querying the agent
query = st.text_input("Enter your question:", "What is the post of Andrew Adams?")
if st.button("Ask"):
    if db_file is not None or 'chinook.db':  # Ensure there's a database available
        response = agent.run(query)
        st.text(response)
    else:
        st.warning("Please upload a database file to proceed.")

st.header('Detailed Blog Post')

st.image('llm.png', caption='Talking to the Database')


st.subheader("Check out this [Medium blog I wrote](https://medium.com/@parasmadan.in/langchain-connecting-llms-to-your-database-8dd28a98e4f3)")