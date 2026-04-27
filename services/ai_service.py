from backend.config import USE_OPENAI

def run_ai(prompt, inputs, images=None):

    if not USE_OPENAI:
        return {
            "status": "OPENAI_DISABLED",
            "prompt_preview": prompt[:200],
            "note": "AI execution will happen later"
        }

    # FUTURE:
    # integrate OpenAI here
    pass