import os
import csv
from dotenv import load_dotenv
from groq import Groq
from pdf import create_pdf

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def read_data(filename):
    prices = []
    totals = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                prices.append(int(row["Price"]))
                totals.append(int(row["Total"]))
            except:
                continue

    return prices, totals


def analyze_with_llm(prices, totals):
    prompt = f"""
You are a calculator.

Prices: {prices}
Totals: {totals}

Calculate:
- Sum of totals
- Average of prices
- Maximum price

IMPORTANT:
Return ONLY the final answer.
Do NOT explain.
Do NOT add any text.
Do NOT show steps.

Output must be EXACTLY in this format (no extra lines):

Sum: <number>
Average: <number>
Max: <number>
"""

    response = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


prices, totals = read_data("products.csv")

result = analyze_with_llm(prices, totals)

print(result)

create_pdf(result, "report.pdf")