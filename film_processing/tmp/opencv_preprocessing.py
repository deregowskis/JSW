import cv2
from pydub import AudioSegment,silence
from .macro_model import *
import imutils
import json
import math

# Loading the face recognizor from opencv
cascade_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

EMOTIONS = ['angry', 'disgusted', 'fearful', 'happy', 'sad', 'surprised', 'neutral']

def format_image(image):
    if len(image.shape) > 2 and image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = cascade_classifier.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

    if not len(faces) > 0:
        print("len(faces)>0")
        return None, None
    max_are_face = faces[0]

    for face in faces:
        if face[2] * face[3] > max_are_face[2] * max_are_face[3]:
            max_are_face = face

    face_coor = max_are_face
    image = image[face_coor[1]:(face_coor[1] + face_coor[2]), face_coor[0]:(face_coor[0] + face_coor[3])]
    try:
        image = cv2.resize(image, (48, 48), interpolation=cv2.INTER_CUBIC)
    except Exception:
        print("problem during resize")
        return None, None

    return image, face_coor


def demo(videoPath, voice_url, testerId, modelPath):
    print("Entered function facial analyzing")
    startTime = 0
    negative = 0
    fearful = 0
    happy = 0
    surprise = 0
    neutral = 0
    json_obj = []

    # myaudio = AudioSegment.from_wav(voice_url)
    # dBFS = myaudio.dBFS
    # silence_p = []
    print("Starting to detect silence")
    # silence_p = silence.detect_silence(myaudio, min_silence_len=500, silence_thresh=dBFS - 5)
    print("Silence part detected")
    # silence_p = [((start / 1000), (stop / 1000)) for start, stop in silence_p]  # in sec
    print("Silence part converted")
    print("Silence global value assigned")



    vidcap = cv2.VideoCapture(videoPath)
    fps = vidcap.get(5)
    fps = 24.8785115
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(frame_count)
    print(frame_count)
    print(frame_count)

    duration = frame_count / fps
    unit_second = math.floor(1 * fps)
    face_x = tf.placeholder(tf.float32, [None, 2304])
    # probs = tf.global_variables_initializer()
    y_conv = deepnn(face_x)
    print("The value of y_conv")
    print(y_conv)
    probs = tf.nn.softmax(y_conv)
    print("The value of probs")
    print(probs)

    saver = tf.train.Saver()
    ckpt = tf.train.get_checkpoint_state(modelPath)
    sess = tf.Session()
    tmp = tf.global_variables_initializer()
    sess.run(tmp)

    if ckpt and ckpt.model_checkpoint_path:
        saver.restore(sess, ckpt.model_checkpoint_path)
    else:
        print("false")
    result = None
    emotion_list = []
    jsonContent = {}
    jsonContent["version"] = "1.0.0"
    jsonContent["testerId"] = testerId
    jsonContent["videoType"] = "With OR Without Silence"
    while vidcap.isOpened():
        current_frame = vidcap.get(cv2.CAP_PROP_POS_FRAMES)
        # print(current_frame)

        ret, frame = vidcap.read()
        if frame is None:
            break
        frame = imutils.resize(frame, 680)

        detected_face, face_coor = format_image(frame)

        if (current_frame % unit_second == 0):
            print("While loop")
            print(current_frame)
            startTime += 1
            if detected_face is not None:
                print("Photo Captured")
                tensor = image_to_tensor(detected_face)
                result = sess.run(probs, feed_dict={face_x: tensor})
                json_flag = 1
        if result is not None:
            for index, emotion in enumerate(EMOTIONS):
                if index == 0:
                    angry = result[0][0]
                if index == 1:
                    disgusted = result[0][1]
                if index == 2:
                    fearful = result[0][2]
                if index == 3:
                    happy = result[0][3]
                if index == 4:
                    sad = result[0][4]
                if index == 5:
                    surprise = result[0][5]
                if index == 6:
                    neutral = result[0][6]
            if json_flag is not None:
                emotion_list.append({
                    "isDisplayed": 1,
                    "StartTime": startTime,
                    "Angry": angry.tolist(),
                    "Disgusted": disgusted.tolist(),
                    "Fear": fearful.tolist(),
                    "Happy": happy.tolist(),
                    "Surprise": surprise.tolist(),
                    "Sad": sad.tolist(),
                    "Neutral": neutral.tolist(),
                })
                # json_obj = json.dumps(emotion_list, indent=4)
                json_flag = None
    jsonContent["emotions"] = emotion_list
    json_obj = jsonContent
    # print(json_obj)
    vidcap.release()
    return json_obj