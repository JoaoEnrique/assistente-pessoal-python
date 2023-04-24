'''
 Blog Eletrogate - Como conectar o Arduino com Python
 Miguel Sena
 blog.eletrogate.com
'''

import serial #Importa a biblioteca

while True: #Loop para a conexão com o Arduino
    #try:  #Tenta se conectar, se conseguir, o loop se encerra
        arduino = serial.Serial('COM3', 9600)
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