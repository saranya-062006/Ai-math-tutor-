import sympy as sp
import re

def clean_equation(text):
    """
    Convert OCR output into valid algebra expression
    """

    # remove unwanted spaces
    text = text.replace(" ", "")

    # Fix OCR patterns
    text = re.sub(r"Integer\((\d+)\)", r"\1", text)
    text = re.sub(r"Symbol\('([a-zA-Z])'\)", r"\1", text)

    # convert 2x → 2*x
    text = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", text)

    return text


def solve_equation(equation):

    equation = clean_equation(equation)

    if "=" not in equation:
        return "Invalid equation format"

    left, right = equation.split("=")

    x = sp.symbols('x')

    expr = sp.Eq(sp.sympify(left), sp.sympify(right))

    solution = sp.solve(expr, x)

    return solution