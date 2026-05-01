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
    """Generates a Mermaid pie/bar/radar (hypothetical) or simple text visualization."""
    # Since Mermaid doesn't have a direct 'matrix comparison' chart, 
    # we can generate a Mermaid Class Diagram or Entity Relationship to show connections.
    # For now, let's just stick to a clean Markdown output that can be injected.
    pass

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_file = os.path.join(base_path, "data", "comparative_matrix.csv")
    
    print("\n--- GENERATED COMPARATIVE MATRIX (MARKDOWN) ---\n")
    print(generate_markdown_table(csv_file))
    print("\n--- END OF MATRIX ---\n")
