import argparse
import os
import time
from datasets import load_dataset
from tqdm import tqdm
import json

from src.generator import DeepSeekGenerator
from src.evaluator import exec_code, calculate_pass_at_k
from src.prompts import PROMPT_TEMPLATES
from src.utils import clean_code, save_results

def main():
    parser = argparse.ArgumentParser(description="Evaluate improvements on specific HumanEval tasks")
    parser.add_argument("--model", type=str, default="qwen2.5-coder:1.5b", help="Model name in Ollama")
    parser.add_argument("--samples", type=int, default=1, help="Number of samples (n) per task")
    parser.add_argument("--k", type=int, default=1, help="k in pass@k")
    args = parser.parse_args()

    # The 16 tasks that failed in all 3 modes
    target_tasks = [
        'HumanEval/10', 'HumanEval/19', 'HumanEval/26', 'HumanEval/32', 
        'HumanEval/38', 'HumanEval/46', 'HumanEval/69', 'HumanEval/70', 
        'HumanEval/75', 'HumanEval/77', 'HumanEval/83', 'HumanEval/87', 
        'HumanEval/90', 'HumanEval/91', 'HumanEval/93', 'HumanEval/95'
    ]

    print(f"Loading HumanEval dataset for {len(target_tasks)} targeted tasks...")
    dataset = load_dataset("openai_humaneval", split="test")
    
    # Filter the dataset
    eval_dataset = [item for item in dataset if item["task_id"] in target_tasks]
    
    generator = DeepSeekGenerator(model_name=args.model)
    template_name = "hybrid"
    prompt_template = PROMPT_TEMPLATES[template_name]

    print(f"\n===== Evaluating Targeted Improvements: {template_name} =====")
    results = []
    total_pass_at_k = 0
    
    for item in tqdm(eval_dataset):
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
            "task_name": entry_point,
            "samples": cleaned_codes,
            "correct_count": correct_count,
            "n": args.samples,
            "pass@k": pass_at_k,
            "time_taken": time_taken
        })
        
    avg_pass_at_k = total_pass_at_k / len(eval_dataset)
    print(f"\nResults for Targeted Tasks ({len(eval_dataset)}):")
    print(f"Avg pass@{args.k}: {avg_pass_at_k:.4f}")
    
    # Save results
    filename = f"data/results_improved_targeted.json"
    save_results(results, filename)
    print(f"Results saved to {filename}")

if __name__ == "__main__":
    main()
