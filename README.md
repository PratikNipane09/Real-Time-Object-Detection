# Real-Time-Object-Detection
This project implements a real-time color detection and tracking system using OpenCV and Python. It specifically identifies yellow objects in a webcam feed, generates a binary mask, and draws a bounding box around the detected object.

🚀 Features
Real-Time Tracking: Captures video at 720p resolution.
HSV Color Segmentation: Uses the HSV color space for robust detection under varying lighting conditions.
Dynamic Bounding Box: Utilizes the Pillow library’s getbbox() method for efficient object localization.
Interactive Interface: Mirrors the camera for a natural user experience and includes safe exit triggers.

💻 How it Works
Color Definition: The target color is defined in BGR format (e.g., [0, 255, 255] for Yellow).
HSV Conversion: The frame is converted from BGR to HSV.
Masking: The cv2.inRange function creates a binary image where only pixels matching the target color range are white.
Localization: The script converts the mask to a PIL Image to utilize getbbox(), which identifies the x1, y1 (top-left) and x2, y2 (bottom-right) coordinates of the white pixels.
Visualization: A green rectangle is drawn on the original frame around the detected object.

📂 Project Structure
main.py: The core script for webcam capture and tracking.
Utilities.py: Contains get_limits() for calculating HSV threshold boundaries.
README.md: Project documentation.
