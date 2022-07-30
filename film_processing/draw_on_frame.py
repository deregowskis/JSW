from time import sleep

import cv2
import math
import json
from PIL import Image

input_path = "/Users/bilibala/Desktop/work/dataset/wozy_film_dataset/video/Film_POC.mp4"
output_path = "/Users/bilibala/Desktop/work/dataset/wozy_film_dataset/video/processed_Film_POC_opencv.mp4"
json_merged_path = '/Users/bilibala/Desktop/work/dataset/wozy_film_dataset/frame_output/v1_JSON_merged/merged.json'

with open(f"{json_merged_path}", 'r') as json_obj_file:
    json_obj_list = json.load(json_obj_file)

def write_video(file_path, frames, fps, width, height):
    """
    Writes frames to an mp4 video file
    :param file_path: Path to output video, must end with .mp4
    :param frames: List of PIL.Image objects
    :param fps: Desired frame rate
    """
    w = int(width)
    h = int(height)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    writer = cv2.VideoWriter(file_path, fourcc, fps, (w, h))

    for frame in frames:
        writer.write(frame)
    writer.release()

def tmp(videoPath):
    frame_list = []
    rec_coor = []
    frame_id = 0
    vidcap = cv2.VideoCapture(videoPath)
    fps = vidcap.get(5)
    print(fps)
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(frame_count)
    duration = frame_count / fps
    unit_second = math.floor(1 * fps)
    print(duration)
    width = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # print("be ready")
    # cv2.waitKey(5000)
    # print("start")
    a = 0
    while vidcap.isOpened():
        current_frame = vidcap.get(cv2.CAP_PROP_POS_FRAMES)
        # print(current_frame)
        ret, frame = vidcap.read()
        if frame is None:
            break
        if current_frame % (1*unit_second) == 0:
            class_name = json_obj_list[frame_id]['class_prediction']
            class_confidence = json_obj_list[frame_id]['class_confidences']
            load_name = json_obj_list[frame_id]['loads_prediction']
            loads_confidence = json_obj_list[frame_id]['loads_confidences']
            digit = json_obj_list[frame_id]['digits']
            if digit == "":
                digit = "unknown"
            [x, y, w, h] = json_obj_list[frame_id]["boxes"]
            left = int(width * x)
            right = int(width * y)
            top = int(height * w)
            bottom = int(height * h)
            text_coor = int(width - 400)
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 0), 2)
            cv2.putText(frame, class_name, (text_coor, 0 * 30 + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, str(class_confidence), (text_coor, 1 * 30 + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, load_name, (text_coor, 2 * 30 + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, str(loads_confidence), (text_coor, 3 * 30 + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, digit, (text_coor, 4 * 30 + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            # cv2.putText(frame, str(frame_id+1), (text_coor, 5 * 30 + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            frame_id += 1
            # for i in range(3):
            #     frame_list.append(frame)
            cv2.imshow('Wozy_JSW_POC', frame)
            key = cv2.waitKey(200)
        if ret is True:
            cv2.imshow('Wozy_JSW_POC', frame)
            if a == 0:
                key = cv2.waitKey(5000)
                a = 1
            frame_list.append(frame)
            # key = cv2.waitKey(50)
    vidcap.release()
    print("write to video")
    write_video(output_path, frame_list, fps, width, height)

tmp(input_path)