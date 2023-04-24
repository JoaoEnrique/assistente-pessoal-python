import azure.cognitiveservices.speech as speechsdk # reconhecedor de voz da Microsoft

# classes pessoais
import funcoes
import openia
import answer
import voice
import arduino
#import azure.cognitiveservices.speech as speechsdk # reconhecedor de voz da Microsoft


#instancia da classe
funcoes = funcoes.Funcoes
openia = openia.OpenIa 
answer = answer.Answer 
arduino = arduino.Arduinos 
voice = voice.Voice 

class Input:
    # def comandoVoz():  
    #     while True:      
    #         # Configurar a chave da API e a região
    #         speech_key = '6eb299d5c33843608369933deee528ca'
    #         service_region = 'brazilsouth'
        
        
    #         # Configurar o reconhecimento de fala
    #         speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language='pt-BR')
    #         audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    #         # Criar um reconhecedor de fala
    #         speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    #         # Iniciar o reconhecimento de fala e aguardar o resultado
    #         result = speech_recognizer.recognize_once_async().get()
    #         speech = result.text.lower()
            
    #         #tirar pontuação do texto falado
    #         speech = speech.replace(".", "")
    #         speech = speech.replace(",", "")
    #         speech = speech.replace("?", "")
    #         print(speech)
            
    #         # Chamar funções pela fala
    #         if speech == "gideon" or speech == "google" or speech == "jarvis" or speech == "harris" or speech == "jardins":
    #             escutando = True
    #             voice.speak("Estou aqui, João. Pode falar")
    #         if speech == "sair" or  speech == "tchau":
    #             voice.speak("Tchau, até mais")
    #             break
            
    #         text = speech.replace("jarvis","")
    #         if "jarvis" in speech or "jarbis" in speech or "jaque" in speech or "harris" in speech or "jardis" in speech or "chaves" in speech or "jardins" in speech:
    #             #tira nome do robo na fala
    #             text = text.replace("jarvis","")
    #             text = text.replace("jaque","")
    #             text = text.replace("harris","")
    #             text = text.replace("jarbis","")
    #             text = text.replace("jardis","")
    #             text = text.replace("jardins","")
    #             text = text.replace("chaves","")
                
    #             # cacho o primeiro caractere seja um espaco, remove
    #             if(len(text) >0 and text[0] == " "):
    #                 text = text[1:]
    #             print(text)
    #             answer.Answer(text)
                
                
    
    def comandoTerminal():
        erro = 0      
        while True:
            if erro <= 0:
                voice.speak("Nenhum microfone conectado")
                erro += 1
            #PROGRAMA USANDO O TERMINAL
            speech = input("VOCÊ: ").lower()
            
            #tirar pontuação do texto falado
            speech = speech.replace(".", "")
            speech = speech.replace(",", "")
            speech = speech.replace("?", "")
            print(speech)
            
            # Chamar funções pela fala
            if speech == "gideon" or speech == "google" or speech == "jarvis" or speech == "harris":
                escutando = True
                voice.speak("Estou aqui, João. Pode falar")
            if speech == "sair" or  speech == "tchau":
                voice.speak("Tchau, até mais")
                break
            
            text = speech.replace("jarvis","")
            #if "jarvis" in speech or "jarbis" in speech or "jaque" in speech or speech == "harris"or speech == "jardis" or speech == "jards":
                #tira nome do robo na fala
            text = text.replace("jarvis","")
            text = text.replace("jaque","")
            text = text.replace("harris","")
            text = text.replace("jarbis","")
            text = text.replace("jardis","")
            
            # cacho o primeiro caractere seja um espaco, remove
            if(len(text) >0 and text[0] == " "):
                text = text[1:]
            print(text)
            answer.Answer(text)
                
                
    #PROJETO USANDO O speech_recognition no lugar do reconhecedor de voz da microsoft
    def comandoVoz(): 
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as s:
            r.adjust_for_ambient_noise(s)
            while True:
                try:
                    audio = r.listen(s)
                    speech = r.recognize_google(audio, language='pt')
                    speech = speech.lower()
                    
                    speech = speech.replace(".", "")
                    speech = speech.replace(",", "")
                    speech = speech.replace("?", "")
                    print(speech)
                    
                    # Chamar funções pela fala
                    if speech == "gideon" or speech == "google" or speech == "jarvis" or speech == "harris":
                        escutando = True
                        voice.speak("Estou aqui, João. Pode falar")
                    if speech == "sair" or  speech == "tchau":
                        voice.speak("Tchau, até mais")
                        break
                    
                    text = speech.replace("jarvis","")
                    if "jarvis" in speech or "jarbis" in speech or "jaque" in speech or speech == "harris"or speech == "jardis" or speech == "jards":
                        #tira nome do robo na fala
                        text = text.replace("jarvis","")
                        text = text.replace("jaque","")
                        text = text.replace("harris","")
                        text = text.replace("jarbis","")
                        text = text.replace("jardis","")
                        
                        # cacho o primeiro caractere seja um espaco, remove
                        if(len(text) >0 and text[0] == " "):
                            text = text[1:]
                        print(text)
                        answer.Answer(text)


                    # escrita = input("Fala: ")
                    # if escrita == "gideon" or escrita == "google" or escrita == "jarvis":
                    #     funcoes.escutando = True
                    #     voice.speak("Estou aqui, pode falar")
                    
                    # if escrita == "sair" or  escrita == "tchau":
                    #     voice.speak("Tchau, até mais")
                    #     break
                
                    # text = escrita.replace("Jarvis","")
                    # if "Jarvis" in escrita or "Jarbis" in escrita:
                    #     text = escrita.replace("Jarvis","")
                    #     if(text[0] == " "):
                    #         text = text[1:]
                    #     print(text)
                    #     answer.Answer(text)
                except sr.UnknownValueError:
                    # voice.speak("Não entendi o que você disse")
                    pass
                except sr.RequestError as e:
                    voice.speak("Não foi possível acessar o serviço de reconhecimento de fala; {0}".format(e))
                