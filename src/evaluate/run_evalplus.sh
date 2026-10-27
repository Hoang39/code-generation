#!/usr/bin/env bash
# Benchmark base vs model fine-tune ChatML trên HumanEval(+) và MBPP(+) (EvalPlus, vLLM, greedy pass@1).
# Giao thức: model ChatML phải eval bằng chat template (KHÔNG --force-base-prompt); base được đo cả hai cách
# (base-prompt = mốc tốt nhất của base, chat = so cùng giao thức với model fine-tune).
# Model fine-tune đã merge LoRA (src/finetune/merge_lora.py) và có chat_template + generation_config eos gồm <|im_end|>.
# Usage: FT=hoangnh39/qwen2.5-coder-7b-opencode-hq10k-v4-merged HF_TOKEN=hf_xxx TP=1 bash src/evaluate/run_evalplus.sh
set -euo pipefail

BASE=Qwen/Qwen2.5-Coder-7B
FT=hoangnh39/qwen2.5-coder-7b-opencode-hq10k-v4-merged
TP=${TP:-1}                 # number of GPUs for tensor parallel (use 2 on 2x16GB T4)
DTYPE=${DTYPE:-bfloat16}    # use float16 on T4 (no bf16)

pip install -q "evalplus[vllm]" --upgrade

# EvalPlus chỉ dùng chat template khi tokenizer có chat_template; thiếu thì âm thầm chạy prompt base
python - "$FT" <<'PY'
import sys
from transformers import AutoTokenizer, GenerationConfig
ft = sys.argv[1]
tok = AutoTokenizer.from_pretrained(ft)
assert tok.chat_template, f"{ft}: tokenizer thiếu chat_template -> EvalPlus sẽ eval bằng prompt base"
print("chat_template: OK | generation_config eos:", GenerationConfig.from_pretrained(ft).eos_token_id)
PY

run() {  # run <tên> <model> <dataset> [flags...]
  local name=$1 model=$2 dataset=$3; shift 3
  echo "=== $name / $dataset ==="
  evalplus.evaluate --model "$model" --dataset "$dataset" --backend vllm \
    --greedy --tp "$TP" --dtype "$DTYPE" "$@" | tee "evalplus_${name}_${dataset}.log"
}

for ds in humaneval mbpp; do
  run base_baseprompt "$BASE" "$ds" --force-base-prompt
  run base_chat       "$BASE" "$ds"
  run ft_chat         "$FT"   "$ds"
done

grep -HE "pass@1|humaneval|mbpp" evalplus_*.log
