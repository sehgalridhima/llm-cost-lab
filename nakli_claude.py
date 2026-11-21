# nakli_claude.py
# Ye asli Claude nahi hai. Ye doosri company ka nakli (mock) version hai.
# Dhyan do: iska tareeka nakli OpenAI se ALAG hai, jaise asli duniya mein hota hai.
# Abhi is file ko padhna zaroori nahi hai.

from types import SimpleNamespace

JAANE_HUE_MODELS = ["claude-haiku-5-5", "claude-sonnet-5-5"]


def _tokens_gino(text):
    # Mota hisaab: 3 shabd lagbhag 4 tokens ke barabar hote hain
    shabd = len(text.split())
    return max(1, round(shabd * 4 / 3))


class _Messages:
    def create(self, model, max_tokens, messages):
        if model not in JAANE_HUE_MODELS:
            raise ValueError(f"Model '{model}' nahi mila. Naam check karo.")

        sawaal = messages[-1]["content"]
        jawab_text = f"[nakli {model}] Aapne kaha: '{sawaal}'. Ye mera nakli jawab hai."

        return SimpleNamespace(
            model=model,
            content=[SimpleNamespace(type="text", text=jawab_text)],
            usage=SimpleNamespace(
                input_tokens=_tokens_gino(sawaal),
                output_tokens=_tokens_gino(jawab_text),
            ),
        )


class NakliClaude:
    def __init__(self):
        self.messages = _Messages()
