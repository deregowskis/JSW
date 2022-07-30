import cv2
import json
import math

input_path = "/Users/bilibala/Desktop/work/dataset/wozy_film_dataset/Film_POC.mp4"
frame_output_path = "/Users/bilibala/Desktop/work/dataset/wozy_film_dataset/frame_output/v1/"
def get_video_info(videoPath):
    vidcap = cv2.VideoCapture(videoPath)
    fps = vidcap.get(5)
    print(fps)
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(frame_count)
    duration = frame_count / fps
    unit_second = math.floor(1 * fps)
    print(duration)

# get_video_info(input_path)

def tmp(videoPath):
    frame_list = []
    frame_id = 0
    vidcap = cv2.VideoCapture(videoPath)
    fps = vidcap.get(5)
    print(fps)
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(frame_count)
    duration = frame_count / fps
    unit_second = math.floor(1 * fps)
    print(duration)
    while vidcap.isOpened():
        current_frame = vidcap.get(cv2.CAP_PROP_POS_FRAMES)
        # print(current_frame)
        ret, frame = vidcap.read()
        if frame is None:
            break
        if current_frame % (1*unit_second) == 0:
            frame_id += 1
            img_name = f"{frame_output_path}{frame_id}.png"
            cv2.imwrite(img_name, frame)
            frame_list.append({
                "frameID": frame_id,
                "frameStamp": current_frame,
                "estTime": current_frame/fps,
                "image_name": img_name
            })
            # json_obj = json.dumps(emotion_list, indent=4)
    # jsonContent["emotions"] = emotion_list
    with open('/Users/bilibala/Desktop/work/dataset/wozy_film_dataset/frame_output/v1/v1_frames.json', 'w') as f:
        json.dump(frame_list, f, indent=4, ensure_ascii=False)
    json_obj = frame_list
    print(json_obj)
    vidcap.release()

tmp(input_path)