import ultralytics
import os
from ultralytics import YOLO

def train(name="yolov8n.pt"):
    model = YOLO(name)

    # Use the model
    base='/content/drive/MyDrive/dataset'
    model.train(data=os.path.join(base,'custom.yaml'),imgsz=224, epochs=50)
    metrics = model.val()

# !scp -r /content/runs '/content/drive/MyDrive/dataset'

# !rm -r '/content/runs/detect'

def test():
    model = YOLO("/content/drive/MyDrive/dataset/runs/detect/train/weights/best.pt")
    results = model.predict(source="/content/drive/MyDrive/dataset/images/test", save=True)  # predict on an image

# !scp -r /content/runs/detect/predict '/content/drive/MyDrive/dataset/runs/detect'

if __name__ == "__main__":
    train()
    test()
