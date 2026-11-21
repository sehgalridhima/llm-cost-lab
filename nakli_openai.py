# nakli_openai.py
# Ye asli OpenAI nahi hai. Ye ek nakli (mock) version hai jo asli jaisa hi
# jawab deta hai, par internet par kahin nahi jaata aur paisa nahi lagta.
# Abhi is file ko padhna zaroori nahi hai. Hum ise baad mein kholenge.

from types import SimpleNamespace

# Wo models jo nakli OpenAI "jaanta" hai (asli pricing page ke naam)
JAANE_HUE_MODELS = ["gpt-6-luna", "gpt-6.1-terra", "gpt-6.1-sol", "gpt-6-astra"]


def _tokens_gino(text):
    # Mota hisaab: 3 shabd lagbhag 4 tokens ke barabar hote hain
    shabd = len(text.split())
    return max(1, round(shabd * 4 / 3))


class _Responses:
    def create(self, model, input):
        if model not in JAANE_HUE_MODELS:
            raise ValueError(f"Model '{model}' nahi mila. Naam check karo.")

        jawab_text = f"[nakli {model}] Aapne kaha: '{input}'. Ye mera nakli jawab hai."

        return SimpleNamespace(
            model=model,
            output_text=jawab_text,
            usage=SimpleNamespace(
                input_tokens=_tokens_gino(input),
                output_tokens=_tokens_gino(jawab_text),
            ),
        )


class NakliOpenAI:
    def __init__(self):
        self.responses = _Responses()
