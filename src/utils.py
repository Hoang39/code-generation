import json
import re

def clean_code(generated_text):
    # Regex to extract code between ```python and ```
    match = re.search(r"```python\s*(.*?)\s*```", generated_text, re.DOTALL)
    if match:
        return match.group(1)
    
    # Fallback to general block
    match = re.search(r"```\s*(.*?)\s*```", generated_text, re.DOTALL)
    if match:
        return match.group(1)
        
    return generated_text.strip()

def save_results(results, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
