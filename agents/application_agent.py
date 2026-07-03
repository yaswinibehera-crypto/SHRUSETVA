from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


class ApplicationAgent:

    def __init__(self):
        self.name = "Modern Application Agent"

    def process(self, query: str):

        prompt = f"""
You are an innovation and sustainability expert.

Traditional Practice:
{query}

Suggest practical modern applications.

Organize your answer into:

## Healthcare

## Agriculture

## Environment

## Education

## Technology

## Future Opportunities

Be practical.

Return Markdown only.

Maximum 300 words.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return {
            "agent": self.name,
            "status": "completed",
            "applications": response.text
        }