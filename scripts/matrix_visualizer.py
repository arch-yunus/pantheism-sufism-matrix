import csv
import os

def generate_markdown_table(csv_path):
    """Reads a CSV and returns a Markdown table string."""
    if not os.path.exists(csv_path):
        return "Error: CSV file not found."
    
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    if not rows:
        return "Error: CSV is empty."
    
    headers = rows[0]
    data = rows[1:]
    
    # Create MD Header
    md = "| " + " | ".join(headers) + " |\n"
    md += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    
    # Create MD Rows
    for row in data:
        md += "| " + " | ".join(row) + " |\n"
    
    return md

def generate_mermaid_comparison(csv_path):
    """Generates a Mermaid Class Diagram string for visual comparison."""
    if not os.path.exists(csv_path):
        return "Error: CSV file not found."
    
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    mermaid = "classDiagram\n"
    mermaid += "    class Pantheism {\n"
    for row in data:
        param = row['Parameter'].replace(" ", "_")
        val = row['Pantheism (Spinozist)'].split("(")[0].strip()
        mermaid += f"        +{param}: {val}\n"
    mermaid += "    }\n"
    
    mermaid += "    class Sufism {\n"
    for row in data:
        param = row['Parameter'].replace(" ", "_")
        val = row['Vahdet-i Vucud (Sufism)'].split("(")[0].strip()
        mermaid += f"        +{param}: {val}\n"
    mermaid += "    }\n"
    
    return mermaid

import random

def get_random_quote(quotes_path):
    """Returns a formatted random quote from the CSV."""
    if not os.path.exists(quotes_path):
        return "Quotes collection not found."
    
    with open(quotes_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        quotes = list(reader)
    
    if not quotes:
        return "No quotes found."
    
    q = random.choice(quotes)
    return f"\n> \"{q['Quote (Original/Translation)']}\"\n> — **{q['Source']}** ({q['Theme']})\n"

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_file = os.path.join(base_path, "data", "comparative_matrix.csv")
    quotes_file = os.path.join(base_path, "data", "quotes_collection.csv")
    
    print("\n--- GENERATED COMPARATIVE MATRIX (MARKDOWN) ---\n")
    print(generate_markdown_table(csv_file))
    
    print("\n--- GENERATED MERMAID DIAGRAM ---\n")
    print(generate_mermaid_comparison(csv_file))
    
    print("\n--- RANDOM WISDOM ---\n")
    print(get_random_quote(quotes_file))
    
    print("\n--- END OF SCRIPT ---\n")
