# classes pessoais
import funcoes
import arduino
import input


#instancia da classe
funcoes = funcoes.Funcoes
arduino = arduino.Arduinos 
input = input.Input 





#arduino.temArduino() # verifica se tem arduino
funcoes.comprimento() #gerador de voz

class Main:
    try:
        input.comandoVoz() #caso tenha um microfone, ativa o microfone
    except:
        input.comandoTerminal() #caso não tenha microfone, ativa o terminal