from ultralytics import YOLO
import cv2
def infer(source,model=YOLO('yolov5nu.pt')):
    video = cv2.VideoCapture(source)
    while True:
        success, frame = video.read()
        if success:
            out=model(frame)[0].plot()
            ret, out = cv2.imencode('.jpg', out)
            out=out.tobytes()
            #time.sleep(1)
            yield(b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + out + b'\r\n\r\n')
        else:
           break

    video.release()
    