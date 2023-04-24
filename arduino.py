#conexao com arduino
import pyfirmata #Importamos a biblioteca PyFirmata que realiza a comunicação entre Python e Arduino
import time #Importamos a biblioteca PyFirmata que realiza a comunicação entre Python e Arduino
import voice #Importamos a biblioteca PyFirmata que realiza a comunicação entre Python e Arduino

voice = voice.Voice

board = None

servo_pin1 = 9
servo_pin2 = 10
servo_pin3 = 11
servo_pin4 = 12

servo1 = None
servo2 = None
servo3 = None
servo4 = None
# Pino conectado ao servo



class Arduinos:
    def temArduino():
        try:
            global board  # Indicar que vamos utilizar a variável global
            global servo1
            global servo2
            global servo3
            global servo4
            #voice.speak("Tem algum arduino Conectado? (Sim ou Não): ")
            #try:
            #respostaArduino =  input("Tem algum arduino Conectado? (S ou N): ").lower()
            respostaArduino = "s"
            board = pyfirmata.Arduino("COM3")
            if(respostaArduino == "s" or respostaArduino == "sim" or respostaArduino == "ss"):
                arduinoConectado =  True
                                                    
                pinRele = 2 #Definimos para o Python que nosso pino é o 13.
                
                # Configuração do pino do servo
                servo1 = board.get_pin('d:{}:s'.format(servo_pin1))
                servo2 = board.get_pin('d:{}:s'.format(servo_pin2))
                servo3 = board.get_pin('d:{}:s'.format(servo_pin3))
                servo4 = board.get_pin('d:{}:s'.format(servo_pin4))
                
                
                #port = input("Porta do Arduino: ").upper() #Configuramos a porta como a porta COM4. Esta configuração deve ser alterada caso sua placa não se configure nesta porta.
                #board = pyfirmata.Arduino(port) #Criamos a variável board que realizará os comandos a partir daqui
                
                board.digital[pinRele].write(1)#desliga rele
                servo1.write(180)#fecha garra
                return True
            else:
                arduinoConectado = True
                return True
        except:
           temArduino =  False
           arduinoConectado = False
           return False
        #    voice.speak("Não Foi possivel conectar com Arduino")
        
    def triste():
        global board
        board.digital[2].write("triste")
        print("Fiquei triste")
        
    def digitalWrite(pin, state):
        global board  # Indicar que vamos utilizar a variável global
        board.digital[pin].write(state)
        
    def analogWrite(pin, state):
        global board  # Indicar que vamos utilizar a variável global
        board.analog[pin].write(state)

    def digitalRead(pin):
        global board  # Indicar que vamos utilizar a variável global
        return board.digital[pin].read()
    
    
        
    def abrirGarra():
        global servo1
        servo1.write(0)
        print("Abriu")
        
    def fecharGarra():
        global servo1
        servo1.write(180)
        print("Fechou")
        
        
    def direitaGarra():
        global servo2
        servo2.write(0)
        print("Direita")
        
    def esquerdaGarra():
        global servo2
        servo2.write(180)
        print("Esquerda")
        
        
    def cimaGarra():
        global servo3
        servo3.write(90)
        print("Subiu")
        
    def baixoGarra():
        global servo3
        servo3.write(0)
        print("Desceu")