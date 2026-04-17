import argparse
import os
import time
from datasets import load_dataset
from tqdm import tqdm

from src.generator import DeepSeekGenerator
from src.evaluator import exec_code, calculate_pass_at_k
from src.prompts import PROMPT_TEMPLATES
from src.utils import clean_code, save_results

def main():
    parser = argparse.ArgumentParser(description="Evaluate LLM on HumanEval")
    parser.add_argument("--model", type=str, default="qwen2.5-coder:1.5b", help="Model name in Ollama")
    parser.add_argument("--samples", type=int, default=1, help="Number of samples (n) per task")
    parser.add_argument("--tasks", type=int, default=5, help="Number of tasks to evaluate (for testing)")
    parser.add_argument("--k", type=int, default=1, help="k in pass@k")
    args = parser.parse_args()

    print("Loading HumanEval dataset...")
    try:
        dataset = load_dataset("openai_humaneval", split="test")
    except Exception as e:
        print(f"Could not load openai_humaneval. Check your connection. Details: {e}")
        return

    eval_dataset = dataset.select(range(min(args.tasks, len(dataset))))
    generator = DeepSeekGenerator(model_name=args.model)
    
    os.makedirs("data", exist_ok=True)

    # Loop through each template for comparison
    for template_name, prompt_template in PROMPT_TEMPLATES.items():
        print(f"\n===== Evaluating Template: {template_name} =====")
        results = []
        total_pass_at_k = 0
        
        for idx, item in enumerate(tqdm(eval_dataset)):
            task_id = item["task_id"]
            prompt = item["prompt"]
            test_cases = item["test"]
            entry_point = item["entry_point"]
            
            # 1. Generate code
            start_time = time.time()
            raw_samples = generator.generate(prompt_template, prompt, num_samples=args.samples)
            time_taken = time.time() - start_time
            
            # 2. Extract and Evaluate
            correct_count = 0
            cleaned_codes = []
                
            for raw_text in raw_samples:
                code = clean_code(raw_text)
                eval_code = code + "\n" + test_cases + f"\ncheck({entry_point})\n"
                
                passed = exec_code(code, eval_code, timeout=5)
                if passed:
                    correct_count += 1
                
                cleaned_codes.append({
                    "raw": raw_text,
                    "extracted": code,
                    "passed": passed
                })
                
            pass_at_k = calculate_pass_at_k(args.samples, correct_count, args.k)
            total_pass_at_k += pass_at_k
            
            results.append({
                "task_id": task_id,
                "task_name": entry_point, # Added task name field
                "samples": cleaned_codes,
                "correct_count": correct_count,
                "n": args.samples,
                "pass@k": pass_at_k,
                "time_taken": time_taken
            })
            
        avg_pass_at_k = total_pass_at_k / len(eval_dataset)
        avg_time = sum(r["time_taken"] for r in results) / len(results)
        print(f"Template [{template_name}] - Avg pass@{args.k}: {avg_pass_at_k:.4f} - Avg time: {avg_time:.2f}s/it")
        
        # Save separate results for each template
        filename = f"data/results_{template_name}.json"
        save_results(results, filename)
        print(f"Results saved to {filename}")

if __name__ == "__main__":
    main()
