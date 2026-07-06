from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image
import pytesseract

# Change this path if Tesseract is installed in a different location
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

Tk().withdraw()

file_path = askopenfilename(
    title="Select Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

if file_path:
    image = Image.open(input("Add path: "))

    text = pytesseract.image_to_string(image)

    print("Extracted Text:")
    print(text)

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("Text saved successfully in output.txt")
else:
    print("No image selected.")