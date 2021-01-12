import speech_recognition as sr
import pyaudio
import wave
import unidecode


def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 7
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("**** recording ****")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("**** done recording ****")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def parse_audio():
    global input_text_cleansed
    input_audio = sr.AudioFile('output.wav') # Read WAV file and convert to text
    r = sr.Recognizer()

    with input_audio as source:
        audio = r.record(source)

    input_text_parsed = r.recognize_google(audio, language="es-US")
    input_text_cleansed = unidecode.unidecode(input_text_parsed) # Normalize text. (Convert text with accents to regular letters)

    print(input_text_parsed)
    print("Parsed: ",input_text_parsed)
    print("Cleansed (no accent): ", input_text_cleansed)





# if (input_text_cleansed.lower() == "el perro esta corriendo en la calle"):
#     print("Congrats! You got the correct word!")
# else:
#     print("Sorry, that was the wrong answer. You are STUPID!")
