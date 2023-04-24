#conexao com arduino
#import pyfirmata #Importamos a biblioteca PyFirmata que realiza a comunicação entre Python e Arduino
import time #Importamos a biblioteca PyFirmata que realiza a comunicação entre Python e Arduino
import voice #Importamos a biblioteca PyFirmata que realiza a comunicação entre Python e Arduino
import serial #Importa a biblioteca
voice = voice.Voice

board = None
class Arduinos:
    def temArduino():
        global board  # Indicar que vamos utilizar a variável global
        #voice.speak("Tem algum arduino Conectado? (Sim ou Não): ")
        #try:
        #respostaArduino =  input("Tem algum arduino Conectado? (S ou N): ").lower()
        respostaArduino = "n"
        if(respostaArduino == "s" or respostaArduino == "sim" or respostaArduino == "ss"):
                                                
            pinRele = 2 #Definimos para o Python que nosso pino é o 13.
            port = input("Porta do Arduino: ").upper() #Configuramos a porta como a porta COM4. Esta configuração deve ser alterada caso sua placa não se configure nesta porta.
            
            arduino = serial.Serial('COM3', 9600)
            print('Arduino conectado')
            return True
        else:
            arduinoConectado = True
            return True
        #except:
        #    temArduino =  False
        #    voice.speak("Não Foi possivel conectar com Arduino")
        
    
    def digitalWrite(pin, state):
        global arduino
        arduino.write('l'.encode())
        
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