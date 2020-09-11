import subprocess
subprocess.call(['ffmpeg', '-i', 'song.mp3',
                   'file.wav'])

from pydub import AudioSegment
t1 = 1 * 1000
t2 = 3 * 1000

newAudio = AudioSegment.from_wav("file.wav")
newAudio = newAudio[t1:t2]
newAudio.export('file2.wav', format = "wav")
