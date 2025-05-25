import os
from groq import Groq

client = Groq(api_key="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")

completion = client.chat.completions.create(
    model="mixtral-8x7b-32768",
    messages=[
        {
            "role": "user",
            "content": "where do we get vitamin D ?"
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

response = ""

for chunk in completion:
    response += (chunk.choices[0].delta.content or "")

print(response)