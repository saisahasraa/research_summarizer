import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure with your key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class SummaryGenerationAgent:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def generate_summary(self, paper):
        print(f"Summarizing: {paper['title']}")
        prompt = f"Summarize this academic paper in simple terms:\n\n{paper['clean_text'][:3000]}"

        try:
            response = self.model.generate_content(prompt)
            paper['summary'] = response.text
        except Exception as e:
            paper['summary'] = f"[Gemini Error] {e}"
            print(f"⚠️ Gemini Exception: {e}")
        return paper
