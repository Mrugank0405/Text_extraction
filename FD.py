import easyocr

# Initialize the reader with GPU enabled

# mr is for marathi.
reader = easyocr.Reader(['en','mr'], gpu=True)

# Perform OCR
result = reader.readtext("FD.jpg", detail=0)
print("Extracted Text:")
for line in result:
    print(line)
