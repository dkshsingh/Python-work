import sounddevice
from scipy.io.wavfile import write

fps = 44100
duration = 10
print("Recording...")
Recording = sounddevice.rec(int(duration*fps), samplerate=fps, channels=2)
sounddevice.wait()
print("Done!")

write("output.wav", fps, Recording)

