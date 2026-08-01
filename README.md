# 📚 AI Study Assistant

An AI-powered study companion that turns your notes into concise summaries, quiz questions, and flashcards using OpenAI. The project includes both a Streamlit web interface and a command-line workflow.

## Features

- Generate a summary and quiz questions from pasted notes in the Streamlit app.
- Generate five-point summaries, quiz questions, and Q&A flashcards from the command line.
- Load the OpenAI API key securely from a `.env` file.
- Use OpenAI's `gpt-4.1-mini` model for responses.

## Project Structure

```text
.
├── app.py                 # Streamlit web application
├── study_assistant.py     # Command-line study assistant and reusable functions
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment configuration
└── .gitignore             # Excludes the local .env file
```

## Requirements

- Python 3.9 or newer
- An OpenAI API key

## Setup

1. Clone or download this repository.
2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

   You can use `.env.example` as a template. Never commit your real API key to source control.

## Run the Streamlit App

Start the web interface with:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, paste your study notes, and select **Generate**.

## Run the Command-Line Assistant

Run the command-line version with:

```bash
python study_assistant.py
```

Paste your notes when prompted. The script will print:

- A five-bullet summary
- Five quiz questions
- Q&A flashcards

## Notes

- Each request uses the OpenAI API and may incur usage charges according to your OpenAI account and model pricing.
- The application expects `OPENAI_API_KEY` to be available in the environment loaded from `.env`.
- Avoid pasting confidential, personal, or sensitive information into the application.

## License

No license has been specified for this project yet.
