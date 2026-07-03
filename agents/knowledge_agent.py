from google import genai
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


class KnowledgeAgent:

    def __init__(self):
        self.name = "Knowledge Collection Agent"

    def process(self, query: str):

        prompt = f"""
You are the Knowledge Collection Agent of SHRUSETVA.

Your responsibility is ONLY to explain traditional knowledge.

Topic:
{query}

Provide:

1. Historical background

2. Traditional practice

3. Cultural importance

Don't mention modern science.

Maximum 250 words.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return {
            "agent": self.name,
            "status": "completed",
            "traditional_knowledge": response.text
        }