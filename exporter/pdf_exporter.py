from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PIL import Image
import os

def images_to_pdf(images_dir, output_pdf):
    images = sorted([
        os.path.join(images_dir, img)
        for img in os.listdir(images_dir)
        if img.endswith(".jpg")
    ])

    if not images:
        return

    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    for img_path in images:
        img = Image.open(img_path)
        img_width, img_height = img.size

        ratio = min(width/img_width, height/img_height)
        img_width *= ratio
        img_height *= ratio

        c.drawImage(
            img_path,
            (width - img_width)/2,
            (height - img_height)/2,
            img_width,
            img_height
        )
        c.showPage()

    c.save()
