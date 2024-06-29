import speech_recognition as sr

def recognize_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the source for input
    with sr.Microphone() as source:
        print("Please say something...")
        # Listen for the first phrase and extract it into audio data
        audio_data = recognizer.listen(source)
        print("Recognizing...")

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

# Example usage
if __name__ == "__main__":
    recognized_text = recognize_speech()
    if recognized_text is not None:
        print("Recognized Text:", recognized_text)

