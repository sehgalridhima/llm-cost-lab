# step2.py - working out the cost of one question

from mock_openai import MockOpenAI

# gpt-6.1-sol prices: dollars per 1 million tokens
INPUT_PRICE = 0.10
OUTPUT_PRICE = 1.00

client = MockOpenAI()

response = client.responses.create(
    model="gpt-6.1-sol",
    input="Tell me about coffee",
)

input_tokens = response.usage.input_tokens
output_tokens = response.usage.output_tokens

cost = (input_tokens * INPUT_PRICE + output_tokens * OUTPUT_PRICE) / 1_000_000

print("Input tokens:", input_tokens)
print("Output tokens:", output_tokens)
print(f"Cost: ${cost:.6f}")
