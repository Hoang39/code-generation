from huggingface_hub import HfApi, create_repo
import os

def upload_to_hf(file_path, repo_name, token):
    api = HfApi()
    
    print(f"Creating/Checking repository {repo_name}...")
    try:
        create_repo(repo_name, token=token, repo_type="dataset", exist_ok=True)
    except Exception as e:
        print(f"Repo creation failed or already exists: {e}")

    print(f"Uploading {file_path} to Hugging Face...")
    api.upload_file(
        path_or_fileobj=file_path,
        path_in_repo="dataset.jsonl",
        repo_id=repo_name,
        repo_type="dataset",
        token=token
    )
    print("Upload successful!")

if __name__ == "__main__":
    FILE_PATH = "magicoder_python_samples.jsonl"
    REPO_NAME = "hoangnh39/magicoder_samples_qwen2.5-coder"
    TOKEN = os.getenv("HF_TOKEN")
    
    if TOKEN:
        upload_to_hf(FILE_PATH, REPO_NAME, TOKEN)
    else:
        print("HF_TOKEN not found in environment variables. Please set it to upload.")
