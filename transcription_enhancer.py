from transformers import pipeline
import speech_recognition as sr

recognizer = sr.Recognizer()
language_model = pipeline("text-generation", model="gpt2")

def transcribe_audio(audio_file):
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        transcription = recognizer.recognize_google(audio)
        print("Original Transcription:", transcription)
        return transcription
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def improve_transcription(transcription):
    improved_text = language_model(transcription, max_length=200, num_return_sequences=1)[0]['generated_text']
    print("Improved Transcription:", improved_text)
    return improved_text

# Example call
audio_file = "hema_audio.wav"
transcription = transcribe_audio(audio_file)
if transcription:
    improve_transcription(transcription)
