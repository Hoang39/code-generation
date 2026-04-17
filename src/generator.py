import requests

class DeepSeekGenerator:
    def __init__(self, model_name="qwen2.5-coder:1.5b", base_url="http://localhost:11434"):
        self.model_name = model_name
        self.base_url = base_url
        self.api_url = f"{base_url}/api/generate"

    def generate(self, prompt_template, task_prompt, num_samples=1):
        full_prompt = prompt_template.format(prompt=task_prompt)
        
        samples = []
        for _ in range(num_samples):
            payload = {
                "model": self.model_name,
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "temperature": 0.2, # Low temperature for coding task generally
                    "top_p": 0.95
                }
            }
            
            try:
                response = requests.post(self.api_url, json=payload)
                response.raise_for_status()
                result = response.json()
                samples.append(result.get("response", ""))
            except Exception as e:
                print(f"Error calling Ollama API: {e}")
                samples.append("")
                
        return samples
