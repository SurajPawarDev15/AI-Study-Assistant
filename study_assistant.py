from openai import OpenAI
from dotenv import load_dotenv
import os
import sys

# ---------------- LOAD ENV ----------------
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ ERROR: OPENAI_API_KEY not found in .env file")
    sys.exit()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# ---------------- SAFE REQUEST FUNCTION ----------------
def safe_request(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ API Error: {e}"

# ---------------- FEATURES ----------------
def summarize_text(text):
    return safe_request([
        {"role": "system", "content": "You are a helpful study assistant."},
        {"role": "user", "content": f"Summarize this in 5 bullet points:\n{text}"}
    ])


def generate_questions(text):
    return safe_request([
        {"role": "system", "content": "You are a teacher."},
        {"role": "user", "content": f"Create 5 quiz questions from this:\n{text}"}
    ])


def create_flashcards(text):
    return safe_request([
        {"role": "system", "content": "You create study flashcards."},
        {"role": "user", "content": f"Create flashcards (Q&A format):\n{text}"}
    ])

# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    print("📚 AI Study Assistant\n")

    user_text = input("Paste your notes here:\n")

    if not user_text.strip():
        print("❌ Please enter valid text.")
        sys.exit()

    print("\n⏳ Generating results...\n")

    print("🔹 Summary:")
    print(summarize_text(user_text))

    print("\n🔹 Quiz Questions:")
    print(generate_questions(user_text))

    print("\n🔹 Flashcards:")
    print(create_flashcards(user_text))