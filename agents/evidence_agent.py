from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


class EvidenceAgent:

    def __init__(self):
        self.name = "Evidence Evaluation Agent"

    def process(self, query: str):

        prompt = f"""
You are an evidence evaluation specialist.

Evaluate this traditional practice:

{query}

Your task is NOT to explain history.

Your task is ONLY to classify the evidence.

Return your answer using EXACTLY this format:

## Evidence Status

Choose ONE:

- Scientifically Supported
- Partially Supported
- Cultural Practice
- Insufficient Evidence

---

## Confidence Score

Give a percentage.

---

## Reason

Explain why.

---

## Cautions

Mention limitations or situations where more evidence is needed.

Return Markdown only.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return {
            "agent": self.name,
            "status": "completed",
            "evaluation": response.text
        }