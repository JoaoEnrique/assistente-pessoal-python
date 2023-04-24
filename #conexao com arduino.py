#conexao com arduino
import pyfirmata #Importamos a biblioteca PyFirmata que realiza a comunicação entre Python e Arduino
import time #Importamos a biblioteca PyFirmata que realiza a comunicação entre Python e Arduino
import voice #Importamos a biblioteca PyFirmata que realiza a comunicação entre Python e Arduino

voice = voice.Voice

board = None
class Arduinos:
    def temArduino():
        global board  # Indicar que vamos utilizar a variável global
        #voice.speak("Tem algum arduino Conectado? (Sim ou Não): ")
        #try:
        #respostaArduino =  input("Tem algum arduino Conectado? (S ou N): ").lower()
        respostaArduino = "n"
        board = pyfirmata.Arduino("COM3")
        if(respostaArduino == "s" or respostaArduino == "sim" or respostaArduino == "ss"):
            arduinoConectado =  True
                                                
            pinRele = 2 #Definimos para o Python que nosso pino é o 13.
            port = input("Porta do Arduino: ").upper() #Configuramos a porta como a porta COM4. Esta configuração deve ser alterada caso sua placa não se configure nesta porta.
            board = pyfirmata.Arduino(port) #Criamos a variável board que realizará os comandos a partir daqui
            board.digital[pinRele].write(1)
            return True
        else:
            arduinoConectado = True
            return True
        #except:
        #    temArduino =  False
        #    voice.speak("Não Foi possivel conectar com Arduino")
        
    
    def digitalWrite(pin, state):
        global board  # Indicar que vamos utilizar a variável global
        board.digital[pin].write(state)
        
    def analogWrite(pin, state):
        global board  # Indicar que vamos utilizar a variável global
        board.analog[pin].write(state)

    def digitalRead(pin):
        global board  # Indicar que vamos utilizar a variável global
        return board.digital[pin].read()

    def analogRead(pin):
        global board  # Indicar que vamos utilizar a variável global
        return board.analog[pin].read()

    def dispositivos(dispositivo):
        dis = {
            'lampada': 2,
            'alarme': 3
        }

    def ligarAlarme():
        board.write("ligarAlarme".encode())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#TESTE

'''
 Blog Eletrogate - Como conectar o Arduino com Python
 Miguel Sena
 blog.eletrogate.com
'''

import serial #Importa a biblioteca

while True: #Loop para a conexão com o Arduino
    #try:  #Tenta se conectar, se conseguir, o loop se encerra
        arduino = serial.Serial('COM3', 115200)
        print('Arduino conectado')
        break

    #except:
     #   pass

while True: #Loop principal
    cmd = input('Digite "l" para ligar e "d" para desligar. ') #Pergunta ao usuário se ele deseja ligar ou desligar o led

    if cmd == 'desligaRele': #Se a resposta for "l", ele envia este comando ao Arduino
        arduino.write('desligaRele'.encode())

    elif cmd == 'ligaRele': #Senão, envia o "d"
        arduino.write('ligaRele'.encode())
        
        
        
    elif cmd == 'abrirGarra': #Senão, envia o "d"
        arduino.write('abrirGarra'.encode())
        
    elif cmd == 'fecharGarra': #Senão, envia o "d"
        arduino.write('fecharGarra'.encode())
        
        
    elif cmd == 'cimaGarra': #Senão, envia o "d"
        arduino.write('cimaGarra'.encode())
        
    elif cmd == 'baixoGarra': #Senão, envia o "d"
        arduino.write('baixoGarra'.encode())
        
        
    elif cmd == 'frenteGarra': #Senão, envia o "d"
        arduino.write('frenteGarra'.encode())
        
    elif cmd == 'trasGarra': #Senão, envia o "d"
        arduino.write('trasGarra'.encode())
        
        
    elif cmd == 'direitaGarra': #Senão, envia o "d"
        arduino.write('direitaGarra'.encode())
        
    elif cmd == 'esquerdaGarra': #Senão, envia o "d"
        arduino.write('esquerdaGarra'.encode())
        
    elif cmd == 'sim': #Senão, envia o "d"
        arduino.write('sim'.encode())
        
    elif cmd == 'nao': #Senão, envia o "d"
        arduino.write('nao'.encode())

    arduino.flush() #Limpa a comunicação