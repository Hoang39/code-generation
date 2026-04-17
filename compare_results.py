import json
import os
import glob

def calculate_metrics(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Calculate for all tasks in the file
    total_tasks = len(data)
    passed_tasks = sum(1 for item in data if item.get('pass@k', 0) > 0)
    avg_pass = passed_tasks / total_tasks if total_tasks > 0 else 0
    
    # Calculate for just the first 54 tasks (for direct comparison)
    data_54 = data[:54]
    total_54 = len(data_54)
    passed_54 = sum(1 for item in data_54 if item.get('pass@k', 0) > 0)
    avg_pass_54 = passed_54 / total_54 if total_54 > 0 else 0
    
    # Avg time
    avg_time = sum(item.get('time_taken', 0) for item in data) / total_tasks if total_tasks > 0 else 0
    
    return {
        "file": os.path.basename(filepath),
        "total_tasks": total_tasks,
        "pass@1_all": avg_pass * 100,
        "pass@1_first54": avg_pass_54 * 100,
        "avg_time": avg_time
    }

files = glob.glob('data/results_*.json')
for file in files:
    metrics = calculate_metrics(file)
    if metrics:
        print(f"--- {metrics['file']} ---")
        print(f"Total Tasks: {metrics['total_tasks']}")
        print(f"Pass@1 (All Tasks): {metrics['pass@1_all']:.2f}%")
        print(f"Pass@1 (First 54 Tasks): {metrics['pass@1_first54']:.2f}%")
        print(f"Avg Time: {metrics['avg_time']:.2f}s")
        print()
