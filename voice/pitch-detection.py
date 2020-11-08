import pyaudio as pa
import
import wave
import numpy as np

'''
Open the wave file and extract useful information.
'''

chunk = 2048

wf = wave.open('test/file2.wav', 'rb')
swidth = wf.getsampwidth()
R = wf.getframerate()

w = np.blackman(chunk)

p = pa.PyAudio()
stream = p.open(format =
                p.get_format_from_width(swidth),
                channels = wf.getnchannels(),
                rate = R,
                output = True)

data = wf.readframes(chunk)

while(len(data) == chunk*swidth):
    stream.write(data)
    indata = np.array(wave.struct.unpack("%dh" % (len(data)/swidth),data))*w

    fftData = abs(np.fft.rfft(indata))**2

    which = fftData[1:].argmax() + 1

    if(which != len(fftData)-1):
        y0, y1, y2 = np.log(fftData[which-1:which+2])
        x1 = (y2 - y0)*0.5 / (2*y1 - y2 - y0)

        freq = (which + x1)*R/chunk
    else:
        thefreq = which*RATE/chunk
    print ("%f Hz." % (freq))
    data = wf.readframes(chunk)
if data:
    stream.write(data)
stream.close()
p.terminate()
 
