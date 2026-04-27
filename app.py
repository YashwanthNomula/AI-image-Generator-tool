import streamlit as st
from backend.pipeline import run_pipeline
from backend.utils import load_prompt
from models.schema import PipelineState
from services.parser import parse_amazon

st.set_page_config(layout="wide")

st.title("🛒 AI Ecommerce Image Automation")

# -----------------------
# INPUTS
# -----------------------

url = st.text_input("Amazon URL (optional)")
manual_text = st.text_area("Manual product input (optional)")
images = st.file_uploader("Upload product images", accept_multiple_files=True)

# -----------------------
# LOAD PROMPTS
# -----------------------

prompts = {
    "strategy": load_prompt("prompts/strategy.txt"),
    "main": load_prompt("prompts/main_images.txt"),
    "secondary": load_prompt("prompts/secondary_images.txt"),
    "generation": load_prompt("prompts/generation.txt"),
}

# -----------------------
# RUN
# -----------------------

if st.button("🚀 Run Automation"):

    state = PipelineState()

    if url:
        state.product_data = parse_amazon(url)
    else:
        state.product_data = {"manual": manual_text}

    st.subheader("📦 Product Data")
    st.json(state.product_data)

    state = run_pipeline(state, prompts, images)

    st.subheader("🧠 Strategy Output")
    st.json(state.strategy)

    st.subheader("✍️ Prompts Output")
    st.json({
        "main": state.main_prompts,
        "secondary": state.secondary_prompts
    })

    st.subheader("🎨 Image Generation Status")
    st.json(state.generated_images)

    if images:
        st.subheader("🖼️ Uploaded Images")
        cols = st.columns(4)
        for i, img in enumerate(images):
            cols[i % 4].image(img)