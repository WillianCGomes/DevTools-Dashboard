import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure API key
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

class GeminiAPI:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')

    def list_models(self):
        return genai.list_models()

    def generate_content(self, prompt):
        return self.model.generate_content(prompt)

    def start_chat(self):
        return self.model.start_chat(history=[])

    def embed_content(self, content, task_type, title=None):
        return genai.embed_content(model='models/embedding-001', content=content, task_type=task_type, title=title)

    def count_tokens(self, content):
        return self.model.count_tokens(content)
