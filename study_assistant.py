from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize client
client = OpenAI(api_key=api_key)


def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful study assistant."},
            {"role": "user", "content": f"Summarize this in 5 bullet points:\n{text}"}
        ]
    )
    return response.choices[0].message.content


def generate_questions(text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a teacher."},
            {"role": "user", "content": f"Create 5 quiz questions from this:\n{text}"}
        ]
    )
    return response.choices[0].message.content


def create_flashcards(text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You create study flashcards."},
            {"role": "user", "content": f"Create flashcards (Q&A format):\n{text}"}
        ]
    )
    return response.choices[0].message.content


# -------- MAIN PROGRAM --------
if __name__ == "__main__":
    print("📚 AI Study Assistant\n")
    
    user_text = input("Paste your notes here:\n")
    
    print("\n🔹 Summary:")
    print(summarize_text(user_text))
    
    print("\n🔹 Quiz Questions:")
    print(generate_questions(user_text))
    
    print("\n🔹 Flashcards:")
    print(create_flashcards(user_text))