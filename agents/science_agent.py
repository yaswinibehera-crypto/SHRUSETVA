from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


class ScienceAgent:

    def __init__(self):
        self.name = "Scientific Verification Agent"

    def process(self, query: str):

        prompt = f"""
You are a scientific researcher.

Your ONLY responsibility is to explain the modern scientific understanding of this traditional practice.

Topic:
{query}

Your response MUST contain:

## Scientific Explanation

## Active Compounds (if applicable)

## Modern Research Findings

## Biological / Chemical Mechanism

## Limitations of Current Research

Do NOT discuss history.

Do NOT discuss culture.

Keep the response under 350 words.

Return Markdown.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return {
            "agent": self.name,
            "status": "completed",
            "evidence": response.text
        }