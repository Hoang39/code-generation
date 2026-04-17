ZERO_SHOT_PROMPT = """You are an expert Python programmer. Write the implementation for the following problem.
Do not output anything else but the code block.

Problem:
{prompt}

Code:
"""

FEW_SHOT_PROMPT = """You are an expert Python programmer. You will be provided some examples, and then a problem to solve.
Do not output anything else but the code block.

Example 1:
Problem:
def add(a, b):
    \"\"\"Return the sum of a and b.\"\"\"

Code:
```python
def add(a, b):
    \"\"\"Return the sum of a and b.\"\"\"
    return a + b
```

Example 2:
Problem:
def is_even(n):
    \"\"\"Check if a number is even.\"\"\"

Code:
```python
def is_even(n):
    \"\"\"Check if a number is even.\"\"\"
    return n % 2 == 0
```

Problem:
{prompt}

Code:
"""

COT_PROMPT = """You are an expert Python programmer. Solve the following problem by thinking step-by-step.
First, provide a brief explanation of your logic, then provide the code block.

Problem:
{prompt}

Solution:
"""

HYBRID_PROMPT = """You are an expert Python programmer. 
Every implementation must start with a `# Logic:` comment describing the algorithm in 1 sentence.

Example 1:
Problem:
def transform_string(s: str) -> str:
    \"\"\"Convert words to uppercase and join with hyphens.
    >>> transform_string('hello world')
    'HELLO-WORLD'
    \"\"\"
Code:
```python
def transform_string(s: str) -> str:
    # Logic: Convert each word to uppercase and join them using hyphens as delimiters.
    return '-'.join(word.upper() for word in s.split())
```

Example 2:
Problem:
def get_unique_sorted(nums: list) -> list:
    \"\"\"Return sorted unique elements.
    >>> get_unique_sorted([3, 1, 2, 1])
    [1, 2, 3]
    \"\"\"
Code:
```python
def get_unique_sorted(nums: list) -> list:
    # Logic: Convert the list to a set to remove duplicates, then sort it.
    return sorted(list(set(nums)))
```

Problem:
{prompt}

Instruction:
1. Examine the docstring examples (>>>) to identifying the exact return type and edge cases.
2. Start the code block with a `# Logic:` comment.

Code:
"""

OPTIMIZED_PROMPT = """You are an expert Python programmer. Write the implementation for the given problem.

Strict Rule:
- Output ONLY the code block. Do not output anything else. No explanations, no markdown outside the code block.

Example 1:
Problem:
def add(a, b):
    \"\"\"Return the sum of a and b.\"\"\"

Code:
```python
def add(a, b):
    return a + b
```

Example 2:
Problem:
def below_zero(operations: list) -> bool:
    \"\"\"Detect if at any point the balance of account falls below zero.\"\"\"

Code:
```python
def below_zero(operations: list) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```

Example 3:
Problem:
def truncate_number(number: float) -> float:
    \"\"\"Return the decimal part of the number.\"\"\"

Code:
```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

Problem:
{prompt}

Code:
"""

# Dictionary to manage all templates
PROMPT_TEMPLATES = {
    # "zero_shot": ZERO_SHOT_PROMPT,
    # "few_shot": FEW_SHOT_PROMPT,
    # "cot": COT_PROMPT,
    # "hybrid": HYBRID_PROMPT,
    "optimized": OPTIMIZED_PROMPT
}
