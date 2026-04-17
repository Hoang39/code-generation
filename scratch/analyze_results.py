import json
import os

def analyze_results(file_path):
    if not os.path.exists(file_path):
        return None
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total_tasks = len(data)
    passed_tasks = sum(1 for task in data if any(sample['passed'] for sample in task['samples']))
    total_time = sum(task['time_taken'] for task in data)
    avg_time = total_time / total_tasks if total_tasks > 0 else 0
    
    failed_task_ids = [task['task_id'] for task in data if not any(sample['passed'] for sample in task['samples'])]
    
    return {
        "total": total_tasks,
        "passed": passed_tasks,
        "pass_rate": (passed_tasks / total_tasks) * 100 if total_tasks > 0 else 0,
        "total_time": total_time,
        "avg_time": avg_time,
        "failed_ids": failed_task_ids
    }

files = {
    "Zero-shot": "f:/code-generation/data/results_zero_shot.json",
    "Few-shot": "f:/code-generation/data/results_few_shot.json",
    "CoT": "f:/code-generation/data/results_cot.json"
}

results = {}
for name, path in files.items():
    results[name] = analyze_results(path)

print(json.dumps(results, indent=4))

# Intersection of failures
if all(results.values()):
    common_failures = set(results["Zero-shot"]["failed_ids"]) & \
                      set(results["Few-shot"]["failed_ids"]) & \
                      set(results["CoT"]["failed_ids"])
    print(f"\nCommon Failures ({len(common_failures)}):")
    print(sorted(list(common_failures)))
