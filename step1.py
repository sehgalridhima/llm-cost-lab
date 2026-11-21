# step1.py - hamara pehla API call (nakli OpenAI ke saath)

from nakli_openai import NakliOpenAI

client = NakliOpenAI()

jawab = client.responses.create(
    model="gpt-6.1-sol",
    input="mujhe coffee ke baare mei btao",
)

print("Jawab:", jawab.output_text)
print("Input tokens:", jawab.usage.input_tokens)
print("Output tokens:", jawab.usage.output_tokens)
