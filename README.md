# Object Detection using YOLOv8 and Streamlit

This project is an **Object Detection application** built using **YOLOv8n** and a **Streamlit web interface**.

The user uploads an image through the Streamlit UI, and the application:
1. Converts the image to **grayscale**
2. Performs **object detection using YOLOv8n**
3. Displays the **grayscale image with detected objects highlighted**

---

## 🚀 Features
- YOLOv8n for fast and efficient object detection
- Streamlit-based user interface
- Image upload support (`jpg`, `png`, `jpeg`)
- Grayscale image processing
- Bounding boxes and class labels on detected objects
- Modular code structure using `utils.py`

---

## 🗂️ Project Structure

```text
obj_detect/
│
├── app.py           # Streamlit application
├── utils.py         # Model loading and object detection functions
├── obj_detect.py    # Object detection logic (if separated)
├── requirements.txt
├── README.md
└── runs/             # YOLO output directory (auto-generated)
