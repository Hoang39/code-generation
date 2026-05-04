import json
import ast
import re
import os
from datasets import load_dataset
from tqdm import tqdm

class MagicoderFilter:
    def __init__(self, output_file="magicoder_python_samples.jsonl"):
        self.output_file = output_file
        self.python_count = 0
        self.valid_syntax_count = 0
        self.system_prompt = self._load_system_prompt()
    
    def _load_system_prompt(self):
        prompt_path = os.path.join(os.path.dirname(__file__), "system_prompt.json")
        with open(prompt_path, "r") as f:
            return json.load(f)["system_prompt"]

    def extract_python_code(self, text):
        pattern = r"```python\n(.*?)\n```"
        matches = re.findall(pattern, text, re.DOTALL)
        if matches:
            return "\n\n".join(matches)
        
        pattern_generic = r"```\n(.*?)\n```"
        generic_matches = re.findall(pattern_generic, text, re.DOTALL)
        for code in generic_matches:
            if self.is_valid_python(code):
                return code
        
        return None

    def is_valid_python(self, code):
        if not code or not isinstance(code, str):
            return False
        try:
            ast.parse(code)
            return True
        except SyntaxError:
            return False

    def is_python_task(self, sample):
        return sample.get("lang", "").lower() == "python"

    def run(self, num_samples=None):
        dataset = load_dataset("ise-uiuc/Magicoder-OSS-Instruct-75K", split="train")
        
        # If num_samples is provided, limit the processing for testing
        if num_samples:
            dataset = dataset.select(range(min(num_samples, len(dataset))))

        print(f"Processing {len(dataset)} samples...")
        
        with open(self.output_file, "w", encoding="utf-8") as f:
            for sample in tqdm(dataset):
                instruction = sample.get("problem", "")
                response = sample.get("solution", "")
                
                # Filter for python tasks
                if not self.is_python_task(sample):
                    continue
                
                self.python_count += 1
                
                # Extract code and check syntax
                code = self.extract_python_code(response)
                
                if not code:
                    if self.is_valid_python(response):
                        code = response
                
                if code and self.is_valid_python(code):
                    self.valid_syntax_count += 1
                    
                    # Prepare the sample
                    formatted_sample = {
                        "messages": [
                            {"role": "system", "content": self.system_prompt},
                            {"role": "user", "content": instruction},
                            {"role": "assistant", "content": code.strip()}
                        ]
                    }
                    f.write(json.dumps(formatted_sample, ensure_ascii=False) + "\n")

        print(f"\nProcessing complete!")
        print(f"Total Python tasks found: {self.python_count}")
        print(f"Samples with valid syntax: {self.valid_syntax_count}")
        print(f"Results saved to: {self.output_file}")

if __name__ == "__main__":
    filter_tool = MagicoderFilter(output_file="magicoder_python_samples.jsonl")
    filter_tool.run(num_samples=4000)
