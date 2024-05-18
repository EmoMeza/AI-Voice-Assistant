import pyaudio
import wave
import threading
import os

class AudioRecorder:
    def __init__(self, filename, channels=1, sample_rate=44100, chunk_size=1024, format=pyaudio.paInt16):
        self.filename = filename
        self.channels = channels
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.format = format
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.format,
                                      channels=self.channels,
                                      rate=self.sample_rate,
                                      input=True,
                                      frames_per_buffer=self.chunk_size)
        self.frames = []
        self.is_recording = False

    def _record_audio(self):
        self.is_recording = True
        while self.is_recording:
            data = self.stream.read(self.chunk_size)
            self.frames.append(data)

    def record(self):
        self.record_thread = threading.Thread(target=self._record_audio)
        self.record_thread.start()

    def stop_recording(self):
        self.is_recording = False
        self.record_thread.join()

    def save_to_file(self):
        with wave.open(self.filename, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.audio.get_sample_size(self.format))
            wf.setframerate(self.sample_rate)
            wf.writeframes(b''.join(self.frames))

    def clear_file(self):
        # Open the file in write mode to truncate it (clear its contents)
        os.remove(self.filename)
