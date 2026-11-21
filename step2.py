# step2.py - ek sawaal ka kharcha nikaalna

from nakli_openai import NakliOpenAI

# gpt-6.1-sol ke daam: 10 lakh (1,000,000) tokens ke dollars mein
INPUT_DAAM = 0.10
OUTPUT_DAAM = 1.00

client = NakliOpenAI()

jawab = client.responses.create(
    model="gpt-6.1-sol",
    input="mujhe coffee ke baare mei btao",
)

input_tokens = jawab.usage.input_tokens
output_tokens = jawab.usage.output_tokens

kharcha = (input_tokens * INPUT_DAAM + output_tokens * OUTPUT_DAAM) / 1_000_000

print("Input tokens:", input_tokens)
print("Output tokens:", output_tokens)
print(f"Kharcha: ${kharcha:.6f}")
