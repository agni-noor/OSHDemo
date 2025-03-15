import vertexai
import streamlit as st
import os
from vertexai.preview.generative_models import (
    GenerationConfig,
    GenerativeModel
)
from dotenv import load_dotenv

load_dotenv()
project_id = os.getenv("project_id")
project_region = os.getenv("region")

# Authenticate with Vertex AI
vertexai.init(project=project_id, location=project_region)

# Load the model
model = GenerativeModel("gemini-1.0-pro")

def user_interfaces():
    st.set_page_config(page_title="VertexAI Demo")
    st.header("VertexAI Local Demo")

    user_question = st.text_input("Ask me anything...")
    
    if user_question:
        response = model.generate_content(user_question, stream=True)
        
        # Stream the response correctly
        st.write_stream(res.text for res in response)

if __name__ == "__main__":
    user_interfaces()
