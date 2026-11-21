# mock_claude.py
# This is not the real Claude. It is a mock version of a second AI company.
# Note: its interface is DIFFERENT from the mock OpenAI, just like in the real world.

from types import SimpleNamespace

KNOWN_MODELS = ["claude-haiku-5-5", "claude-sonnet-5-5"]


def _count_tokens(text):
    # Rough estimate: 3 words are about 4 tokens
    words = len(text.split())
    return max(1, round(words * 4 / 3))


class _Messages:
    def create(self, model, max_tokens, messages):
        if model not in KNOWN_MODELS:
            raise ValueError(f"Model '{model}' not found. Check the name.")

        question = messages[-1]["content"]
        reply_text = f"[mock {model}] You said: '{question}'. This is my mock reply."

        return SimpleNamespace(
            model=model,
            content=[SimpleNamespace(type="text", text=reply_text)],
            usage=SimpleNamespace(
                input_tokens=_count_tokens(question),
                output_tokens=_count_tokens(reply_text),
            ),
        )


class MockClaude:
    def __init__(self):
        self.messages = _Messages()
