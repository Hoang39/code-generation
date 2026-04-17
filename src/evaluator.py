import math
import multiprocessing

def run_eval(code, test_code, queue):
    local_scope = {}
    try:
        exec(code, local_scope)
        exec(test_code, local_scope)
        queue.put(True)
    except Exception:
        queue.put(False)

def exec_code(code, test_code, timeout=5):
    """Executes the code and the test, returning True if passes, False otherwise using multiprocessing"""
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=run_eval, args=(code, test_code, queue))
    p.start()
    p.join(timeout)
    
    if p.is_alive():
        p.terminate()
        p.join()
        return False
        
    return queue.get() if not queue.empty() else False

def calculate_pass_at_k(n, c, k):
    """
    Calculate pass@k metric.
    n: total samples
    c: correct samples
    k: k in pass@k
    """
    if n - c < k:
        return 1.0
    
    if c == 0:
        return 0.0
    try:
        return 1.0 - (math.comb(n - c, k) / math.comb(n, k))
    except ValueError:
        return 0.0
