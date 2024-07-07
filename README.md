
# Langchain Query Interface with Streamlit

Welcome to the Langchain Query Interface. This application leverages the capabilities of Langchain, OpenAI's GPT-4 model, and Streamlit to create an interactive environment for querying databases and performing mathematical computations.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
- [Configuration](#configuration)
- [License](#license)

## Introduction

This application allows users to upload an SQLite database and query it using natural language. It also supports mathematical queries through the integrated Math Chain. The interface is built with Streamlit, providing a user-friendly experience.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/paras55/Chat-with-DB.git
   cd Chat-with-DB
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Add env variables when deploying on streamlit cloud in advanced settings option:
     ```
     [secrets]
     OPENAI_API_KEY = "your_openai_api_key"
     ```

## Usage

1. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

2. **Upload your SQLite database:**
   - Use the file uploader in the Streamlit interface to upload your database file (`.db`).

3. **Query the database:**
   - Enter your query in natural language in the provided text input field and click the "Ask" button.

## Components

### Langchain Components
- **LLMMathChain:** Handles mathematical queries using the GPT-4 model.
- **SQLDatabase:** Manages connections to the SQLite database.
- **SQLDatabaseChain:** Facilitates querying the database using natural language.
- **OpenAI:** The LLM used for processing and generating responses.

### Streamlit Components
- **st.title:** Displays the title of the application.
- **st.file_uploader:** Allows users to upload their SQLite database files.
- **st.markdown:** Provides a link to download a sample database.
- **st.text_input:** Captures the user's query.
- **st.button:** Triggers the processing of the user's query.
- **st.text:** Displays the response from the agent.

## Configuration

- **Environment Variables:**
  Ensure that the OpenAI API key is set in the Streamlit secrets configuration file (`.streamlit/secrets.toml`).

```toml
[secrets]
OPENAI_API_KEY = "your_openai_api_key"
```

- **Default Database:**
  If no database is uploaded, the application uses a default example database (`chinook.db`).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize and expand this application as needed for your specific use case. If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/your-repo/langchain-query-interface/issues).
