import re
from flask import Flask, request, render_template
import os
import cv2
import easyocr

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'], gpu=True)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    name_input = request.form['name']
    reg_no_input = request.form['reg_no']
    file = request.files['id_card']
    
    if not file:
        return "No file uploaded", 400

    # Save the file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Extract text from the image using EasyOCR
    result = reader.readtext(file_path, detail=0)
    extracted_text = "\n".join(result)

    print("Extracted Text:\n", extracted_text)

    # Normalize input for comparison
    name_input_normalized = " ".join(name_input.strip().lower().split())
    reg_no_input_normalized = reg_no_input.strip()

    # Search for user input name and registration number directly in the extracted text
    name_found = name_input_normalized in extracted_text.lower()
    reg_no_found = reg_no_input_normalized in extracted_text

    print("User Input Name:", name_input_normalized)
    print("User Input Registration Number:", reg_no_input_normalized)
    print("Name Found in Text:", name_found)
    print("Registration Number Found in Text:", reg_no_found)

    # Verification
    if name_found and reg_no_found:
        return "Verification Successful! Redirecting..."
    else:
        return "Verification Failed. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
