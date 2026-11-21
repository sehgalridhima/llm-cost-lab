# step3.py - wahi sawaal, par doosri company (nakli Claude) se

from nakli_claude import NakliClaude

client = NakliClaude()

jawab = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=200,
    messages=[{"role": "user", "content": "mujhe coffee ke baare mei btao"}],
)

print("Jawab:", jawab.content[0].text)
print("Input tokens:", jawab.usage.input_tokens)
print("Output tokens:", jawab.usage.output_tokens)
