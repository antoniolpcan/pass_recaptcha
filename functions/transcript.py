import speech_recognition as sr
from pydub import AudioSegment
import io

def transcription(file):
     """
     Transcreve o audio capturado do recaptcha
     """
     sound=AudioSegment.from_file_using_temporary_files(file)
     sound_export = io.BytesIO()
     sound.export(sound_export,format='wav')
     
     r=sr.Recognizer()
     with sr.AudioFile(sound_export) as source:
          audio=r.record(source)
     return r.recognize_google(audio,language='en-US')
