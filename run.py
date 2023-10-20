import torch
cud=torch.cuda.is_available()
dev=torch.cuda.get_device_properties(0).name
print(f"Cuda:{cud}, Device:{dev}")
from ultralytics import YOLO
model=YOLO('yolov5n.pt')
res=model(source="0",show=True)