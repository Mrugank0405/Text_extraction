import easyocr

# Initialize the reader with GPU enabled
reader = easyocr.Reader(['en'], gpu=True)

# Perform OCR
result = reader.readtext("ID_card.jpg")
print("Extracted Text:")
for line in result:
    print(line)
