import os

import ffmpeg

def webm_to_wav(webm_path, wav_path, sampling_rate, channel):
    """
    webm 2 wav
    :param webm_path: input
    :param wav_path: output
    :param sampling_rate: sample rate
    :param channel: channels
    :return: .wav file

    """
    if os.path.exists(wav_path):
        os.remove(wav_path)
    command = "ffmpeg -loglevel quiet -i {} -ac {} -ar {} {}".format(webm_path, channel, sampling_rate, wav_path)
    os.system(command)
    # ffmpeg.input(webm_path).output(wav_path).run()

if __name__ == '__main__':
    webm_path = "E:/UX_Mining/Audio_samples/351.webm"
    wav_path = "E:/UX_Mining/Audio_samples/351newnewnw.wav"
    sampling_rate = 48000
    channel = 2
    webm_to_wav(webm_path, wav_path, sampling_rate, channel)
