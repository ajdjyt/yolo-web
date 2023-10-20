# Yolo web
An implementation of yolov5 accessible via web  
designed to run on a raspberrypi,  

## Dependencies  
```
pip install -r requirements.txt
```

## Running
You can run the app either with the flask cli
```
flask run
```
Or you can run the file directly with python
```
python app.py
```

## Docker
The project comes with Dockerfiles and docker-compose files, when working in docker the camera device has to be provided using --device
```
docker run -p 8080:8080 --device /dev/video0 ghcr.io/ajdjyt/yolo-web
```