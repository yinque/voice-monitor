import time

import pyaudio
import threading
from queue import Queue

config = {
    "delay": 1  # unit(second)
}

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100


def create_stream(is_input=True):
    return pyaudio.PyAudio().open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  input=is_input,
                                  output=not is_input,
                                  frames_per_buffer=CHUNK)


stream_in = create_stream()
stream_out = create_stream(is_input=False)

frames = Queue()


def play():
    time.sleep(config["delay"])
    print("playing")
    while True:
        stream_out.write(frames.get())


print("current config:", config)
threading.Thread(target=play, name="1").start()

print("recording")
while True:
    data = stream_in.read(CHUNK)
    frames.put(data)
