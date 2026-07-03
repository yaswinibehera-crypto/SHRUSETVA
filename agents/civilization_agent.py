from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


class CivilizationAgent:

    def __init__(self):
        self.name = "Civilization Comparison Agent"

    def process(self, query: str):

        prompt = f"""
You are an expert anthropologist and historian.

Your ONLY responsibility is to compare this traditional practice across civilizations.

Topic:
{query}

Find similar practices from civilizations such as:

- India
- China
- Egypt
- Persia
- Greece
- Indigenous cultures
- Africa
- Mesopotamia

For each civilization provide:

• Civilization Name

• Similar Practice

• Short Explanation

DO NOT discuss modern science.

Return the answer in clean Markdown.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return {
            "agent": self.name,
            "status": "completed",
            "comparison": response.text
        }