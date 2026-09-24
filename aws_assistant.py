import os
import sys
from google import genai

if not os.environ.get("GEMINI_API_KEY"):
    print("Error: Pehle apni API key set karein: export GEMINI_API_KEY='your_key'")
    sys.exit(1)

client = genai.Client()
user_question = " ".join(sys.argv[1:])
prompt = f"You are an expert AWS CLI assistant.\nUser task: {user_question}\nProvide ONLY the exact AWS CLI command to achieve this. Do not include any explanations, markdown code blocks, or extra text. Just the raw command."

try:
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    print("\n✅ Yeh rahi aapki AWS Command:\n")
    print(response.text.strip())
    print("\n" + "-" * 50)
except Exception as e:
    print(f"Kuch gadbad hui: {e}")