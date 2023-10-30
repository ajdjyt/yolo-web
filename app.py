from flask import Flask
from flask_restful import Api, Resource, reqparse
from func import infer
import cv2
from ultralytics import YOLO
from flask import Flask,Response

source=0

app = Flask(__name__)
api = Api(app)

model = YOLO('yolov5nu.pt')


class HelloWorld(Resource):
    def get(self):
        return {'message': 'Object detection with YOLO'}

class VideoFeed(Resource):
    def get(self):
        return Response(infer(source), mimetype='multipart/x-mixed-replace; boundary=frame')

api.add_resource(HelloWorld, '/')
api.add_resource(VideoFeed, '/video_feed')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
