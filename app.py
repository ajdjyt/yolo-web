import torch
cud=torch.cuda.is_available()
dev=torch.cuda.get_device_properties(0).name
print(f"Cuda:{cud}, Device:{dev}")
from ultralytics import YOLO
model=YOLO('yolov5n.pt')

import cv2
video = cv2.VideoCapture(0)

from flask import Flask,Response
from func import infer

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Object detection with yolo, please head to /video_feed</p>"

@app.route('/video_feed')
def video_feed():
    global video
    return Response(infer(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)