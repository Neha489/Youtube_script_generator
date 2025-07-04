from llama_cpp import Llama
import os

model_path = os.path.join("models", "mistral-7b-instruct-v0.1.Q4_K_M.gguf")
llm = Llama(model_path=model_path, n_ctx=2048)

def generate_script(title, bullet_points, tone, length, language):
    system_prompt = f"""You are a professional YouTube scriptwriter.
Generate a {length} length, {tone} tone script in {language}.
Structure: Introduction, Main Content, Conclusion."""

    bullet_text = ", ".join(bullet_points) if bullet_points else "None"
    user_prompt = f"\nTitle: {title or 'None'}\nBullet Points: {bullet_text}\n\nScript:\n"

    full_prompt = f"[INST] {system_prompt} {user_prompt} [/INST]"
    result = llm(full_prompt, max_tokens=1024, stop=["</s>"])
    return result["choices"][0]["text"].strip()
