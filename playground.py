import os
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd
from tabulate import tabulate
from itertools import product

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ==== Parameters to test ====
temperatures = [0.0, 0.7, 1.2]
max_tokens_list = [50, 150, 300]
presence_penalties = [0.0, 1.5]
frequency_penalties = [0.0, 1.5]

# ==== Prompt settings ====
system_prompt = "You are a professional product marketing specialist. Create compelling, accurate product descriptions."
user_prompt = "Create a product description for: Iphone 13 pro."
model = "gpt-3.5-turbo"  # or gpt-4

# ==== Store results ====
results = []

# ==== Iterate over all parameter combinations ====
for temp, max_tok, presence_pen, frequency_pen in product(
    temperatures, max_tokens_list, presence_penalties, frequency_penalties
):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=temp,
            max_tokens=max_tok,
            presence_penalty=presence_pen,
            frequency_penalty=frequency_pen,
        )

        output = response.choices[0].message.content.strip()

        results.append({
            "Temperature": temp,
            "Max Tokens": max_tok,
            "Presence Penalty": presence_pen,
            "Frequency Penalty": frequency_pen,
            "Output": output,
        })

        print(f"✅ Done: temp={temp}, max_tok={max_tok}, presence_pen={presence_pen}, freq_pen={frequency_pen}")

    except Exception as e:
        print(f"❌ Error: {e}")

# ==== Export to CSV ====
df = pd.DataFrame(results)
df.to_csv("playground.csv", index=False)

# ==== Print markdown-style table preview ====
print("\nMarkdown Table Preview:")
print(tabulate(df.head(10), headers="keys", tablefmt="github"))  # Show only first 10 for preview