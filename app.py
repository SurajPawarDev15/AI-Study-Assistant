import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("📚 AI Study Assistant")

user_input = st.text_area("Paste your notes here:")

if st.button("Generate"):
    if user_input:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a helpful study assistant."},
                {"role": "user", "content": f"Summarize this and create quiz questions:\n{user_input}"}
            ]
        )
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter some text!")