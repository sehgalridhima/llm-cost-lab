# hinglish_test.py - does Hinglish use more tokens than English?
# Counts tokens with tiktoken, the real tokenizer used by OpenAI models.

import csv
import tiktoken

tokenizer = tiktoken.get_encoding("o200k_base")

ratios = []

with open("pairs.csv") as file:
    for row in csv.DictReader(file, delimiter="|"):
        english_tokens = len(tokenizer.encode(row["english"]))
        hinglish_tokens = len(tokenizer.encode(row["hinglish"]))
        ratio = hinglish_tokens / english_tokens
        ratios.append(ratio)
        print(f"{english_tokens:>3} EN | {hinglish_tokens:>3} HI | {ratio:.2f}x | {row['hinglish']}")

print()
print(f"Pairs tested: {len(ratios)}")
print(f"Average: Hinglish uses {sum(ratios) / len(ratios):.2f}x the tokens of English")
print(f"Lowest: {min(ratios):.2f}x   Highest: {max(ratios):.2f}x")
