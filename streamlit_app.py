import streamlit as st
import openai

def check_openai_api_key(api_key):
    try:
        openai.api_key = api_key
        openai.Model.list()  # Test if the API key is valid by listing models
        return True
    except openai.AuthenticationError:
        return False

# Show title and description.
st.title("📄 Dhruv's Document Question Answering Chatbot for Lab 1")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

# Ask user for their OpenAI API key via `st.text_input`.
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:
    if check_openai_api_key(openai_api_key):
        st.success("Valid OpenAI API key.", icon="✅")

        # Let the user upload a file via `st.file_uploader`.
        uploaded_file = st.file_uploader(
            "Upload a document (.txt or .md)", type=("txt", "md")
        )

        # Ask the user for a question via `st.text_area`.
        question = st.text_area(
            "Now ask a question about the document!",
            placeholder="Can you give me a short summary?",
            disabled=not uploaded_file,
        )

        if uploaded_file and question:

            # Process the uploaded file and question.
            document = uploaded_file.read().decode()
