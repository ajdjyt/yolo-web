from ultralytics import YOLO
def infer(video,model=YOLO('yolov5nu.pt')):
    
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
    