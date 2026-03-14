SnapQuery is an AI-powered image analysis system that identifies objects, extracts text, and answers user questions about the contents of an image. The system allows users to upload an image and interact through a chat-style interface to retrieve information about visual elements present in the image.

Features

Object detection from images using YOLOv8

Image–text understanding using CLIP

Text extraction using Tesseract OCR

Chat-based interface to ask questions about images

Fast response time for visual query processing

Tech Stack

Python

YOLOv8

CLIP

Tesseract OCR

OpenCV

PyTorch

How It Works

User uploads an image.

The system processes the image using YOLOv8 for object detection.

CLIP analyzes visual context for semantic understanding.

Tesseract OCR extracts any text present in the image.

Users can ask questions through a chat interface, and the system returns answers based on detected objects and extracted information.

Example Queries

What objects are present in the image?

What is the color of the dot in the image?

Is there any text in the image?

Installation

Clone the repository

git clone https://github.com/your-username/snapquery.git

Install dependencies

pip install -r requirements.txt

Run the project

python app.py
Project Highlights

Achieved 90%+ object detection accuracy

Implemented real-time image query responses (<2 seconds)

Combined computer vision and NLP techniques for interactive image understanding

Author

Anuragh
