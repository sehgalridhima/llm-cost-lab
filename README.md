# LLM Cost Lab

Small experiments on what makes AI models expensive, and how to reduce the cost.

## What I found

- **Hinglish costs a little more than English.** Across 10 everyday sentence pairs, Hinglish used about **1.3x** the tokens of English on average (range 0.6x to 2.0x). Hinglish that mixes in English words (like "working day" or "coffee") stays cheap. My first test on a single sentence showed 2.1x, which shows why one example is not enough.
- **Long chats get expensive fast.** AI does not remember earlier messages, so the app resends the whole chat history every time. A 30-message chat used about **15.5x** more tokens than the same 30 messages sent without history.
- **Trimming history saves a lot.** Keeping only the last 5 messages cut that chat from 23,250 to 7,000 tokens, a saving of about **70%**. The trade-off: the AI forgets older details.

## Files

- `hinglish_test.py` + `pairs.csv`: the Hinglish vs English token test
- `chat_cost.py`: chat history cost, with and without trimming
- `step1.py` to `step3.py`: practice API calls with mock OpenAI and Claude clients

## How to run

    pip install tiktoken
    python3 hinglish_test.py
    python3 chat_cost.py

## Limitations

- 10 sentence pairs is a small sample; some pairs differ in length and style.
- The chat cost test assumes every message is 50 tokens.

## Tools

Python, tiktoken (OpenAI's tokenizer), Git and GitHub
