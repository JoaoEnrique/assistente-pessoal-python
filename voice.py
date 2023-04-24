import pyttsx3 #para gerar voz

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# male_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# engine.setProperty('voice', male_voice_id)
# engine.say("Olá, meu nome é David e sou uma voz de homem.")
# engine.runAndWait()

engine = pyttsx3.init()



#velocidade
rate = engine.getProperty("rate")
engine.setProperty("rate", 220)

class Voice:
    #função para falar
    def speak(speech):
        #print("Você disse: ", speech)
        engine.say(speech)
        engine.runAndWait()
        print("JARVIS: ", speech, "")
        #saveAudio(speech)

    def saveAudio(speech):
        # Salva o áudio em formato WAV
        engine.save_to_file(speech, 'audio.wav')
        engine.runAndWait()

        # # Carrega o arquivo WAV e converte para MP3
        # audio = AudioSegment.from_wav("audio.wav")

        # # Salva o arquivo MP3 com a qualidade desejada (bitrate)
        # audio.export("audio.mp3", format="mp3", bitrate="192k")
