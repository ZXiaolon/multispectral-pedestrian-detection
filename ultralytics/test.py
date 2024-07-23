from ultralytics import YOLO

# Load a model
model = YOLO("yolov8m.yaml")  # build a new model from scratch
model = YOLO("yolov8m.pt")  # load a pretrained model (recommended for training)

img_path = r'C:\Workplace\DL\dataset\val'
results=model.predict(source=img_path,
                      device=0,
                      conf=0.5,
                      iou=0.45,
                      save=True,
                      save_txt=True,
                      save_conf=True,
                      classes=0
                      )

