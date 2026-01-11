from ultralytics import YOLO
# Load model
def load_model():
    model = YOLO("yolov8n.pt") 
    return model

# Detects image and returns object detected image.
def obj_detect(file_path):
    model=load_model()
    result=model(file_path,show=True)
    annoted_img= result[0].plot()
    return annoted_img