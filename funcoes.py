import datetime
import random
import voice
from datetime import datetime
import webbrowser

try:
    import pywhatkit #abrir youtube no primeiro video (musica)
except:
    #CASO NÃO TENHA INTERNET
    pass

#pausar musica usando espaco
import pyautogui
import time


voice = voice.Voice

class Funcoes:
    escutando = True
    def comprimento():
        hoje = datetime.today()

        if hoje.hour >= 4 and hoje.hour <= 11:
            comprimento = "Bom dia, João Enrique"
        elif hoje.hour >= 12 and hoje.hour <= 17:
            comprimento = "Boa tarde, João Enrique"
        else:
            comprimento ="Boa noite, João Enrique"
        
        TodosComprimentos = [comprimento, "Oi, Tudo bem com você?", "Como vai?", "Tudo tranquilo", "Eu to de boa", "e aí, Beleza", "e aí", "Opa, tranquilo?", "Só na paz?", "De boa na lagoa?", "Tranquilidade"]        
        numero_aleatorio = random.randint(0, len(TodosComprimentos) -1)

        voice.speak(TodosComprimentos[numero_aleatorio])
        
        
    def GetTime():
        hoje = datetime.today()
        
        answer = "João, são {} hora e {} minutos!".format(hoje.hour, hoje.minute)
        return answer
            
    def GetDay():
        hoje = datetime.today()
        weekDay = hoje.weekday()
        numberMonth = hoje.month
        
        month = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio","junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        day = ["Sehunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sabado","Domindo"]
        
        answer = f"João, hoje é {day[weekDay]}, dia {hoje.day} de {month[numberMonth]} de {hoje.year}"
        return answer


    def AbrirYouTube():
        pass
    
    def AbrirChrome():
        pass

    def pesquisaYouTube(text):
        termo = ""
        for item in text.split():
            if item.lower() != "youtube" and  item != "por" and  item != "no" and  item != "pesquisa" and  item != "pesquisar" and  item != "pesquise":
                termo += " " + item
                print(termo)
                
        search_term = termo
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        voice.speak(f"Abrindo {search_term} no Youtube")
        answer = False 
        
    def pesquisaChrome(text):
        termo = ""
        for item in text.split():
            if item.lower() != "chrome" and  item != "por" and  item != "no" and  item != "pesquisa" and  item != "pesquisar" and  item != "pesquise":
                termo += " " + item
                print(termo)
                
        search_term = termo
        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.get().open(url)
        voice.speak(f"Abrindo {search_term} no Google")
        
    def pesquisaImagem(text):
        termo = ""
        for item in text.split():
            if item.lower() != "chrome" and  item != "por" and  item != "no" and  item != "pesquisa" and  item != "pesquisar" and  item != "pesquise":
                termo += " " + item
                print(termo)
                
        search_term = termo
        url = f"https://www.google.com/search?q={search_term}&tbm=isch"
        webbrowser.get().open(url)
        voice.speak(f"Abrindo imagem de {search_term}")
        
    def tocarMusica(text):
        termo = ""
        for item in text.split():
            if item.lower() != "toque":
                termo += " " + item
                print(termo)
        pywhatkit.playonyt(text + "musica")
        answer = False 
        voice.speak(f"Tocando {termo} no YouTube")

        
    def pausarMusica():
        pyautogui.press("space")
        voice.speak(f"Música pausada")
        
    def iniciarMusica():
        pyautogui.press("space")
        voice.speak(f"Música iniciada")
        
