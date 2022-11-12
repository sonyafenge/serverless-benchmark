from time import time
import cv2
import os
import shutil

from flask import Flask, request

app = Flask(__name__)

def video_processing(blob_name, file_path):
    output_file_path = '/tmp/output-' + blob_name
    video = cv2.VideoCapture(file_path)
    
    width = int(video.get(3))
    height = int(video.get(4))
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file_path, fourcc, 20.0, (width, height))
    
    start = time()
    while(video.isOpened()):
        ret, frame = video.read()

        if ret:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            im = cv2.imwrite('/tmp/frame.jpg', gray_frame)
            gray_frame = cv2.imread('/tmp/frame.jpg')
            out.write(gray_frame)
        else:
            break
            
    latency = time() - start
    
    video.release()
    out.release()
    return latency, output_file_path

@app.route('/video-processing', methods=['GET'])
def function_handler():
    video_path = request.args.get('video','/app/videos/video.mp4')
    file_name = video_path.rsplit('/', 1)[1]
    latency, output_path = video_processing(file_name, video_path)
    dir_path = os.path.join('_output','videos')
    is_exist = os.path.exists(dir_path)
    if not is_exist:
        # Create a new directory because it does not exist 
        os.makedirs(dir_path)
    
    file_name = output_path.split('/')[2]
    shutil.copyfile(output_path, os.path.join(dir_path, file_name))

    return "latency : " + str(latency)
