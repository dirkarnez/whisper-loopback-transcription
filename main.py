import soundcard as sc
# import soundfile as sf

import queue
import pywhispercpp.constants
from pywhispercpp.model import Model
from multiprocessing import Process
import numpy as np

channels = 1
samplerate = pywhispercpp.constants.WHISPER_SAMPLE_RATE

OUTPUT_FILE_NAME = "out.wav"    # file name.
SAMPLE_RATE = 48000              # [Hz]. sampling rate.
RECORD_SEC = 5                  # [sec]. duration recording audio.

q = queue.Queue(maxsize=20)
audio_data = np.array([])

pwcpp_model = Model('tiny.en', print_realtime=True, print_progress=False, print_timestamps=False, single_segment=True)

# pwccp_model = Model(model,
#                             ,
#                             **model_params)


#         audio = np.frombuffer(data[:], np.float32)
#         audio = audio.reshape((audio.size, 1)) / 2 ** 5

def transcribe_process():
    pwcpp_model.transcribe(audio_data, n_processors=None, new_segment_callback=_new_segment_callback)

def _new_segment_callback(seg):
    print(seg)

with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
    # record audio with loopback from default speaker.
    while True:
        data = mic.record()
        audio_data = np.append(audio_data, data)
        # print(audio_data.size)
        # p1.start()

        if (audio_data.size > (samplerate * 100)): 
            # p1 = Process(target=transcribe_process)
            # p1.start()
            transcribe_process()
            # audio_data = np.array([])

    
    # # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
    # sf.write(file=OUTPUT_FILE_NAME, data=data, samplerate=SAMPLE_RATE)
