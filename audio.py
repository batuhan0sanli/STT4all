from pydub import AudioSegment
import os
from tqdm import tqdm

class Audio:
    def __init__(self, source, buffer):
        self.source = source
        self.buffer = buffer * 1000  # works in milliseconds
        self.audio = self.convAudio()

    def convAudio(self):
        if self.source.endswith(".wav"):
            audio = AudioSegment.from_wav(self.source)
        elif self.source.endswith(".mp3"):
            audio = AudioSegment.from_mp3(self.source)
        elif self.source.endswith(".ogg"):
            audio = AudioSegment.from_ogg(self.source)
        elif self.source.endswith(".flv"):
            audio = AudioSegment.from_flv(self.source)
        elif self.source.endswith(".mp4"):
            audio = AudioSegment.from_file(self.source, "mp4")
        elif self.source.endswith(".wma"):
            audio = AudioSegment.from_file(self.source, "wma")
        elif self.source.endswith(".aiff"):
            audio = AudioSegment.from_file(self.source, "aac")
        elif self.source.endswith(".aac"):
            audio = AudioSegment.from_file(self.source, "aac")
        else:
            tqdm.write(f'Your {self.source} file does not supported!')
            audio = []
        return audio

    def splitList(self):
        maxBuffer = len(self.audio)
        l = list(range(0, maxBuffer, self.buffer)) + [maxBuffer]
        f1 = l[:-1]
        f2 = l[1:]
        self.splitSize = len(f1)
        return f1, f2

    def svTemp(self, t1, t2):
        temp = self.audio[t1:t2]
        temp.export('.temp.wav', format="wav")

    @staticmethod
    def rmTemp():
        os.remove('.temp.wav')



if __name__ == '__main__':
    a = Audio('example_files/test1.wav', 2)
    f1, f2 = a.splitList()
    print(a.splitSize)
    a.svTemp(0,5000)
    a.rmTemp()
