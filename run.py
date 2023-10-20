import torch
cud=torch.cuda.is_available()
dev=torch.cuda.get_device_properties(0).name
print(f"Cuda:{cud}, Device:{dev}")
from ultralytics import YOLO
model=YOLO('yolov5n.pt')
res=model(source="0",show=True)
def infer(model=YOLO('yolov5nu.pt')):
    import cv2

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, frame = cap.read()
        if success:
            #cv2.imshow("YOLOv5 Inference", model(frame)[0].plot())
            out=model(frame)[0].plot()
            yield(b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + out.tobytes() + b'\r\n\r\n')
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
           break

    cap.release()
    cv2.destroyAllWindows()