import streamlit as st
import requests

st.title("🎬 YouTube Script Generator")

input_type = st.radio("Input Type", ["Title", "Bullet Points"])
tone = st.selectbox("Tone", ["educational", "entertaining", "persuasive"])
length = st.selectbox("Length", ["short", "medium", "long"])
language = st.selectbox("Language", ["English", "Hindi", "Spanish"])

title = ""
bullets = []

if input_type == "Title":
    title = st.text_input("Enter Title")
else:
    bullets_raw = st.text_area("Enter bullet points (one per line)")
    bullets = bullets_raw.splitlines()

if st.button("Generate Script"):
    with st.spinner("Generating..."):
        payload = {
            "title": title,
            "bullet_points": bullets,
            "tone": tone,
            "length": length,
            "language": language
        }
        try:
            response = requests.post("http://127.0.0.1:8000/generate-script/", json=payload)
            response.raise_for_status()
            result = response.json()["script"]
            st.success("Script generated successfully!")
            st.text_area("📄 Script Output", result, height=300)
            st.download_button("📥 Download Script", result, file_name="youtube_script.txt")
        except Exception as e:
            st.error(f"Error: {e}")
