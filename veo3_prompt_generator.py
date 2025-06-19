
import streamlit as st
import random

st.set_page_config(page_title="Veo 3 Prompt Generator", layout="centered")
st.title("🎬 Veo 3 Prompt Generator")

# Built-in options
subjects = ["A giant dragon", "A ballet dancer", "A humanoid robot", "A futuristic sports car"]
actions = ["flying across the sky", "dancing gracefully", "battling a monster", "transforming into a spaceship"]
scenes = ["over snowy mountains", "in a rainy cyberpunk city", "underwater", "on Mars"]
moods = ["epic and majestic", "melancholic and quiet", "full of energy and cheerful", "tense and dramatic"]
styles = ["in realistic 3D", "in Pixar-style animation", "with retro VHS effects", "like a Van Gogh painting"]
cameras = ["with an aerial shot", "in a cinematic close-up", "with slow camera movement", "from a first-person perspective"]
lightings = ["sunset lighting", "colored neon lights", "dark silhouette", "moonlight glow"]

# Form input
st.subheader("🎨 Select Elements for Your Prompt")

custom_subject = st.text_input("Custom Subject (optional)")
subject = st.selectbox("Choose a Subject", subjects)

action = st.selectbox("Action", actions)
scene = st.selectbox("Scene", scenes)
mood = st.selectbox("Mood", moods)
style = st.selectbox("Visual Style", styles)
camera = st.selectbox("Camera Style", cameras)
lighting = st.selectbox("Lighting", lightings)

# Generate prompt
if st.button("✨ Generate Prompt"):
    final_subject = custom_subject.strip() if custom_subject.strip() else subject
    prompt = f"{final_subject} {action} {scene}, {mood}, {style}, {camera}, {lighting}."
    st.text_area("🎬 Generated Prompt", prompt, height=120)

    # Download prompt
    st.download_button(
        label="📥 Download Prompt as .txt",
        data=prompt,
        file_name="veo3_prompt.txt",
        mime="text/plain"
    )
