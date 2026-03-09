import sys
import os
import streamlit as st
from PIL import Image

# Fix module import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import project modules
from modules.ocr_utils import extract_text
from modules.solver import solve_equation


# Page Configuration
st.set_page_config(
    page_title="AI Math Tutor",
    page_icon="🧮",
    layout="centered"
)

# Title
st.title("🧮 AI Math Tutor")
st.subheader("Solve Algebra Problems from Images")

st.write(
    "Upload a photo of an algebra equation and the system will extract the equation and solve it step-by-step."
)

st.divider()

# Image Upload
uploaded_file = st.file_uploader(
    "Upload Algebra Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    # Show Uploaded Image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Save image temporarily
    temp_path = "temp_equation.png"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("Processing image...")

    # OCR Extraction
    text = extract_text(temp_path)

    st.subheader("Recognized Equation")
    st.code(text)

    st.write("Raw OCR Output:")
    st.write(text)

    st.divider()

    # Solve Button
    if st.button("Solve Problem"):

        with st.spinner("Solving equation..."):

            solution = solve_equation(text)

        st.success("Solution")

        st.write(solution)

        st.divider()

        st.subheader("Explanation")

        st.write(
            """
            The system extracted the algebra equation from the image using OCR, 
            then solved the equation using symbolic mathematics.
            """
        )

else:
    st.info("Please upload an algebra problem image to begin.")