import os
from openai import OpenAI

class OpenAIClient:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("No OpenAI API key found in environment variables")

        self.openai = OpenAI(api_key=api_key)

    def send_prompt(
            self,
            prompt,
            debug=False,
            user="user",
            model="gpt-4-1106-preview",
            max_tokens=50):
        try:
            response = self.openai.chat.completions.create(
                messages=[
                    {
                        "role": user,
                        "content": prompt,
                    }
                ],
                model=model,
                max_tokens=max_tokens,
            )

            if debug:
                print("Response: " + response + "\n")

            return response
        except Exception as e:
            print(f"Error sending prompt: {e}")
            return None
