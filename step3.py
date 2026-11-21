# step3.py - the same question, but to a second company (mock Claude)

from mock_claude import MockClaude

client = MockClaude()

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=200,
    messages=[{"role": "user", "content": "Tell me about coffee"}],
)

print("Reply:", response.content[0].text)
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
