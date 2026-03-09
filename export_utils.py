from reportlab.pdfgen import canvas

def export_pdf(filename, content):

    c = canvas.Canvas(filename)

    y = 800

    for line in content.split("\n"):
        c.drawString(50, y, line)
        y -= 20

    c.save()