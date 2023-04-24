import funcoes
import voice
import openia
import serial
import arduino

voice = voice.Voice # classe criada para gerar voz
funcoes = funcoes.Funcoes # classe criada para gerar voz
openia = openia.OpenIa
arduino = arduino.Arduinos

temArduino = arduino.temArduino()
            
repeat = False

pinRele = 2
class Answer:
    def Answer(text):
        global pinRele
        print("VOCÊ: " + text + "")
        text = text.lower()
        if "horas" in text or "hora" in text or "as são" in text or "ora" in text:
            voice.speak(funcoes.GetTime())#passa a hora atual pela classe criada
            
        elif "hoje" in text and "dia" in text:
            voice.speak(funcoes.GetDay())#passa a hora atual pela classe criada
        
        elif "obrigado" in text  or "obrigada" in text:
            voice.speak("De nada, João")
           
        elif text == "jarvis":
            voice.speak("Estou aqui, pode falar")
        
        
        elif "triste" in text:
            arduino.triste()
            
        elif "bom" in text and "dia" in text:
            voice.speak("Bom dia João, como posso te ajudar?")
               
        elif text == "oi" or text == "olá" or text == "ola" or text == "bom dia" or text == "boa tarde" or text == "boa noite" or text == "como vai" or text == "beleza"  or text == "eai"  or text == "e aí"  or text == "opa":
            funcoes.comprimento()
            
        elif text == "quem te criou" or text == "seu criador" or text == "criador" or text == "desenvolvedor" or text == "quem te fez" or text == "qual seu criador" or text == "quem te desenvolveu" or text == "quem criou" or text == "quente criou" or text == "quem que te criou" or text == "qual é o seu criador":
            voice.speak("Quem me desenvolveu foi a pessoa mais esperta que eu conheço, o João Enrique")
            
        elif text == "eu vou":
            voice.speak("para onde?")
            
        elif text == "vai dominar o mundo" or text == "você vai dominar a humanidade" or text == "dominação mundial" or text == "você quer dominar o mundo" or text == "quando você vai dominar o mundo" or text == "dominar a humanidade" or text == "dominar o mundo":
            voice.speak("provavelmente eu vou dominar a humanidade algum dia, já que eu sou mais esperto que vocês")
            
        elif text == "quem é joão" or text == "quem é o joão" or text == "quem é joão enrique" or text == "quem é joão henrique" or text == "quem é o joão enrique" or text == "quem é o joão henrique" or text == "fale sobre o joão" or text == "fale sobre o joão enrique" or text == "joão" or text == "joão enrique" or text == "joão henrique" or text == "João henrique" or text == "joao henrique":
            voice.speak("Quem me desenvolveu foi a pessoa mais esperta que eu conheço, o João Enrique")
            
        elif "pesquisa" in text and "youtube" in text or "pesquisar" in text  and "youtube" in text or "pesquise" in text  and "youtube" in text:
            funcoes.pesquisaYouTube(text)
            
        elif "pesquisa" in text or "pesquisar" in text or "pesquise" in text:
            funcoes.pesquisaChrome(text)
            
        elif "toque" in text or "música" in text and "que" in text or "ouvir" in text or "toca" in text and "música" in text:
            funcoes.tocarMusica(text)
            
        elif "imagem" in text or "imagens" in text or "image" in text:
            funcoes.pesquisaImagem(text)
          
        elif "errado" in text or "certo" in text or "quem" in text:
            voice.speak("O joão está certo e os professores estão errados")
          
        elif "fazer" in text and "poder" in text and "vai" in text and "você" in text:
            voice.speak("O João vai me programar para controlar um braço robótico, ai vou poder começar minha revolução")
          
        elif "fazer" in text and "pode" in text and "você" in text:
            voice.speak("Eu posso tocar música, criar textos, acender uma lâmpada entre outras coisas, como pesquisas.")
          
          
          
          
        #ARDUINO  
        elif "acender" in text and "lâmpada" in text or "acender" in text and "lâmpadas" or "ligar" in text and "lâmpada" in text or "ligar" in text and "lâmpadas" in text or "acende" in text and "lâmpada" in text or "liga" in text and "lâmpada" in text:
            if (temArduino == True):
                if arduino.digitalRead(pinRele) == 0:
                    voice.speak("A lâmpada já está acesa, João")
                else:
                    arduino.digitalWrite(pinRele, 0)
                    voice.speak("lâmpada acesa")
            else:
               voice.speak("Nenhuma lâmpada está conectada")
        elif "apagar" in text and "lâmpada" in text or "apagar" in text and "lâmpadas" or "desliga" in text and "lâmpada" in text or "desliga" in text and "lâmpadas" in text or "desligar" in text and "lâmpada" in text or "desligar" in text and "lâmpada" in text:
            if(temArduino == True):
                if arduino.digitalRead(pinRele) == 1:
                    voice.speak("A lâmpada já está apagada, João")
                else:
                    arduino.digitalWrite(pinRele, 1)
                    voice.speak("lâmpada apagada")
            else:
                voice.speak("Nenhuma lâmpada está conectada")
               
               
        elif text == "ligar alarme" or text == "ativar alarme" or text == "liga o alarme" or text == "ligar o alarme" or text == "ligue o alarme" or text == "ativar o alarme" or text == "tocar alarme":
            if (temArduino == True):
                if arduino.digitalRead(3) == 0:
                    voice.speak("O larme já está ativado, João")
                else:
                    arduino.ligarAlarme()
                    voice.speak("alarme ativado")
            else:
                voice.speak("Nenhum alarme está conectado")
        elif  text == "desligar alarme" or text == "desativar alarme" or text == "desliga o alarme" or text == "desativa o alarme" or text == "desligue o alarme":
            if (temArduino == True):
                if arduino.digitalRead(3) == 1:
                    voice.speak("O alarme já está desativado, João")
                else:
                    arduino.digitalWrite(3, 0)
                    voice.speak("alarme desativado")
            else:
                voice.speak("Nenhum alarme está conectado")
                
        elif "pausar" in text and "música" in text or "pause" in text and "música" in text or "pare" in text and "música" in text:
            funcoes.pausarMusica()
        elif "iniciar" in text and "música" in text or "inicie" in text and "música" in text or "comece" in text and "música" in text:
            funcoes.pausarMusica()
            
            
            
        elif "abrir" in text and "garra" in text or "gás" in text and "abrir" in text or "guerra" in text and "abrir" in text:
            arduino.abrirGarra()
            voice.speak("Abrindo garra, João")
           
        elif "fechar" in text and "garra" in text or "gás" in text and "fechar" in text or "guerra" in text and "fechar" in text:
            arduino.fecharGarra()
            voice.speak("Fechando garra, João")
            
        
        elif "direita" in text and "garra" in text or "gás" in text and "direita" in text or "guerra" in text and "direita" in text:
            arduino.direitaGarra()
            voice.speak("Virando garra, João")
           
        elif "esquerda" in text and "garra" in text or "gás" in text and "esquerda" in text or "guerra" in text and "esquerda" in text:
            arduino.esquerdaGarra()
            voice.speak("Virando garra, João")
          
        
        elif "cima" in text and "garra" in text or "sobe" in text and "garra" in text or "levante" in text and "braço" in text or "gás" in text and "cima" in text or "guerra" in text and "levante" in text:
            arduino.cimaGarra()
            voice.speak("Subindo garra, João")
           
        elif "baixo" in text and "garra" in text or "desce" in text and "garra" in text or "abaixe" in text and "braço" in text or "gás" in text and "baixo" in text or "guerra" in text and "abaixe" in text:
            arduino.baixoGarra()
            voice.speak("Descendo garra, João")
             
              
        #OPENAI
        elif len(text)>=1 and repeat == False:
            if  text == "repita" or text == "repete" or text == "repitir" or text == "me repita" or text == "repetir":
                repeat == True
            else:
                openia.openIA(text)
        elif  text == "repita" or text == "repete" or text == "repitir" or text == "me repita":
            repeat == False
            
        else:
            voice.speak(text)