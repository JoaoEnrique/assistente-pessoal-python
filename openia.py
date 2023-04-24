import voice
import requests
import json

voice = voice.Voice
class OpenIa:
    #Funcao que integra com a biblioteca da inteligencia artificial da OpenIa para fazer perguntas
    def openIA(text):
        # Insira sua chave API do OpenAI abaixo
        API_KEY = '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'

        # Configuração da solicitação
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": text}],
            "temperature": 0.7
        }

        # Enviar solicitação
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(data))
        content = response.json()
        result = content

        # Imprimir a resposta
        #print(response.json())

        #print("")
        print(result)
        voice.speak(result)