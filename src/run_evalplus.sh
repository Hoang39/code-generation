#!/usr/bin/env bash
# Benchmark base vs fine-tuned v3 on HumanEval + HumanEval+ (EvalPlus, vLLM, greedy pass@1).
# v3 adapter was already merged into Qwen2.5-Coder-7B bf16 (src/merge_lora.py) and uploaded.
# Usage: HF_TOKEN=hf_xxx TP=1 bash src/run_evalplus.sh
set -euo pipefail

BASE=Qwen/Qwen2.5-Coder-7B
V3=hoangnh39/qwen2.5-coder-7b-opencode-hq10k-v3-merged
TP=${TP:-1}                 # number of GPUs for tensor parallel (use 2 on 2x16GB T4)
DTYPE=${DTYPE:-bfloat16}    # use float16 on T4 (no bf16)

pip install -q "evalplus[vllm]" --upgrade

echo "=== base ==="
evalplus.evaluate --model "$BASE" --dataset humaneval --backend vllm \
  --greedy --force-base-prompt --tp "$TP" --dtype "$DTYPE" | tee evalplus_base.log

echo "=== v3 ==="
evalplus.evaluate --model "$V3" --dataset humaneval --backend vllm \
  --greedy --tp "$TP" --dtype "$DTYPE" | tee evalplus_v3.log

grep -E "pass@1|humaneval" evalplus_base.log evalplus_v3.log
