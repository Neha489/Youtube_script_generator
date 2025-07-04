# Youtube_script_generator

a YouTube Script Generator powered by a local large language model (Mistral 7B) using `llama-cpp-python`. No API key required.

---

## Features

-  Input: Title or Bullet Points
-  LLM-based script generation (Mistral 7B GGUF via `llama-cpp-python`)
-  Tone control: educational, entertaining, persuasive
-  Length control: short, medium, long
-  Multilingual support (English, Hindi, etc.)
-  Automatic sectioning: Introduction, Main Content, Conclusion
-  Script downloadable as `.txt`

---

## 🚀 Quickstart (Colab)


### Step 1: Download GGUF model
Replace the upload step with this code to download automatically:

```python
!mkdir -p models
!wget -O models/mistral.gguf https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q2_K.gguf
```

> You can also upload a `.gguf` file manually if preferred.

### Step 2: Run the Notebook
- Adjust input: title or bullet points
- Click run and generate the script
- Use the download button to save your script

---


## Example Input

```python
title = "Top 5 AI Tools Changing the World"
bullet_points = []
tone = "educational"
length = "medium"
language = "English"
```

---

## Output Sample

```
 Introduction:
In this video, we’re diving into the top 5 AI tools revolutionizing industries in 2025...

 Main Content:
1. ChatGPT-5: The latest generation of conversational AI...
2. MidJourney V6: Pushing the boundaries of visual creativity...

 Conclusion:
AI tools are shaping a new world of productivity and creativity. Let’s embrace the future.
```

---

## 🛠 Requirements

- Python 3.9+
- llama-cpp-python
- Optional: Streamlit / FastAPI if extending with frontend/backend

---

##  Notes

- You can switch to other `gguf` model quantizations (Q2_K, Q4_K_M, Q5_K_M)
- Tested in Google Colab CPU runtime (no GPU required)
