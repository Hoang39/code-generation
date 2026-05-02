import json
import os

def analyze_json(file_path):
    if not os.path.exists(file_path):
        return None
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total_tasks = len(data)
    passed_tasks = sum(1 for task in data if task.get('correct_count', 0) > 0)
    pass_rate = (passed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    total_time = sum(task.get('time_taken', 0) for task in data)
    avg_time = total_time / total_tasks if total_tasks > 0 else 0
    
    return {
        'total': total_tasks,
        'passed': passed_tasks,
        'pass_rate': pass_rate,
        'total_time': total_time,
        'avg_time': avg_time,
        'task_results': {task['task_id']: task.get('correct_count', 0) > 0 for task in data}
    }

zero_shot_file = r'f:\code-generation\data\results_zero_shot_updated.json'
few_shot_file = r'f:\code-generation\data\results_few_shot_updated.json'

zero_stats = analyze_json(zero_shot_file)
few_stats = analyze_json(few_shot_file)

print("--- Zero-shot Analysis ---")
print(f"Total Tasks: {zero_stats['total']}")
print(f"Passed Tasks: {zero_stats['passed']}")
print(f"Pass Rate: {zero_stats['pass_rate']:.2f}%")
print(f"Total Time: {zero_stats['total_time']:.2f}s")
print(f"Avg Time per Task: {zero_stats['avg_time']:.2f}s")

print("\n--- Few-shot Analysis ---")
print(f"Total Tasks: {few_stats['total']}")
print(f"Passed Tasks: {few_stats['passed']}")
print(f"Pass Rate: {few_stats['pass_rate']:.2f}%")
print(f"Total Time: {few_stats['total_time']:.2f}s")
print(f"Avg Time per Task: {few_stats['avg_time']:.2f}s")

# Comparison
only_zero = []
only_few = []
both_passed = []
both_failed = []

for task_id in zero_stats['task_results']:
    z_pass = zero_stats['task_results'][task_id]
    f_pass = few_stats['task_results'].get(task_id, False)
    
    if z_pass and f_pass:
        both_passed.append(task_id)
    elif not z_pass and not f_pass:
        both_failed.append(task_id)
    elif z_pass and not f_pass:
        only_zero.append(task_id)
    elif not z_pass and f_pass:
        only_few.append(task_id)

print("\n--- Comparison ---")
print(f"Both Passed: {len(both_passed)}")
print(f"Both Failed: {len(both_failed)}")
print(f"Only Zero-shot Passed: {len(only_zero)}")
print(f"Only Few-shot Passed: {len(only_few)}")

if only_zero:
    print(f"\nTasks only Zero-shot passed (first 5): {only_zero[:5]}")
if only_few:
    print(f"Tasks only Few-shot passed (first 5): {only_few[:5]}")
