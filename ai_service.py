import os
import base64
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def encode_image(file):
    return base64.b64encode(file.read()).decode("utf-8")


def run_ai(prompt, inputs, images=None):

    content = [
        {"type": "text", "text": f"{prompt}\n\n{inputs}"}
    ]

    # Handle uploaded images properly
    if images:
        for img in images:
            encoded = encode_image(img)
            content.append({
                "type": "input_image",
                "image_base64": encoded
            })

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[{
            "role": "user",
            "content": content
        }]
    )

    return response.output_text