import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def convert_to_latex(text):

    prompt = f"""
    Convert the following math equation into LaTeX format.

    Equation:
    {text}

    Only return the LaTeX expression.
    """

    response = model.generate_content(prompt)

    return response.text