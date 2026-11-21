# step1.py - my first API call (with the mock OpenAI client)

from mock_openai import MockOpenAI

client = MockOpenAI()

response = client.responses.create(
    model="gpt-6.1-sol",
    input="Tell me about coffee",
)

print("Reply:", response.output_text)
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
