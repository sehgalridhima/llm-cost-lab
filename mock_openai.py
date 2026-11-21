# mock_openai.py
# This is not the real OpenAI. It is a mock version that answers like the real
# client, but never goes to the internet and costs nothing.

from types import SimpleNamespace

# Models the mock OpenAI "knows" (names from the real pricing page)
KNOWN_MODELS = ["gpt-6-luna", "gpt-6.1-terra", "gpt-6.1-sol", "gpt-6-astra"]


def _count_tokens(text):
    # Rough estimate: 3 words are about 4 tokens
    words = len(text.split())
    return max(1, round(words * 4 / 3))


class _Responses:
    def create(self, model, input):
        if model not in KNOWN_MODELS:
            raise ValueError(f"Model '{model}' not found. Check the name.")

        reply_text = f"[mock {model}] You said: '{input}'. This is my mock reply."

        return SimpleNamespace(
            model=model,
            output_text=reply_text,
            usage=SimpleNamespace(
                input_tokens=_count_tokens(input),
                output_tokens=_count_tokens(reply_text),
            ),
        )


class MockOpenAI:
    def __init__(self):
        self.responses = _Responses()
