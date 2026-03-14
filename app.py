from detector import detect_objects
from ocr_module import extract_text

def main():
    image_path = input("Enter image path: ")
    question = input("Ask a question about the image: ")

    objects = detect_objects(image_path)
    text = extract_text(image_path)

    print("Detected Objects:", objects)
    print("Extracted Text:", text)
    print("Answer: Based on detected objects and text, processing query...")

if __name__ == "__main__":
    main()