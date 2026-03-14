from ultralytics import YOLO

def detect_objects(image_path):
    model = YOLO("yolov8n.pt")
    results = model(image_path)
    detected = []
    for r in results:
        for c in r.boxes.cls:
            detected.append(int(c))
    return detected