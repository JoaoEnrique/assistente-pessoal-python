//#include <VarSpeedServo.h>//controlar servo motor com velocidade


// define pinos dos servos
#define pinServ1 5//garra
#define pinServ2 6//cima, baixo
#define pinServ3 7//frente, tras
#define pinServ4 8//direita, esquerda

//VarSpeedServo serv1,serv2,serv3,serv4;  // nomeia os servos, biblioteca com velocidade

char cmd;
int pinRele = 2;
int posicao;
void setup() {
  Serial.begin(9600);         //Inicia o Monitor Serial
  pinMode(pinRele, OUTPUT);         //Define o pino como saída
  digitalWrite(pinRele, LOW);

  // atribui pinos dos servos
  //serv1.attach(pinServ1);
  //serv2.attach(pinServ2);
  //serv3.attach(pinServ3);
  //serv4.attach(pinServ4);

  //serv4.slowmove(90, 100);
}
/*
void sim(){
  serv3.slowmove(90, 100);
  delay(300);
  serv3.slowmove(130, 100);
  delay(300);
  serv3.slowmove(90, 100);
  delay(300);
  serv3.slowmove(130, 100);
  delay(300);
}

void nao(){
  serv4.slowmove(0, 100);
  delay(300);
  serv4.slowmove(180, 100);
  delay(300);
  serv4.slowmove(0, 100);
  delay(300);
  serv4.slowmove(180, 100);
  delay(300);
  serv4.slowmove(90, 100);
}*/
String text;

void loop() {
  //serv2.slowmove(0, 100);
  //delay(300);
  //serv2.slowmove(180, 100); 
  //delay(300);

  if (Serial.available() > 0) {
    text = Serial.readString(); //Realiza a leitura do serial
    text.trim(); // Remove espaços em branco e caracteres extras
    Serial.println(text);

    if (text.equals("desligaRele")) { //Se o comando for "LIGA", liga o rele
      digitalWrite(pinRele, LOW);
    }

    if (text.equals("ligaRele")) { //Se o comando for "DESLIGA", desliga o rele
      digitalWrite(pinRele, HIGH);
    }

    if (text.equals("abrirGarra")) { //Se o comando for "DESLIGA", desliga o rele
      //serv1.slowmove(0, 100);
    }
    if (text.equals("fecharGarra")) { //Se o comando for "DESLIGA", desliga o rele
      //serv1.slowmove(180, 100);
    }


    if (text.equals("cimaGarra")) { //Se o comando for "DESLIGA", desliga o rele
      //serv3.slowmove(180, 100);
    }
    if (text.equals("baixoGarra")) { //Se o comando for "DESLIGA", desliga o rele
     // serv3.slowmove(0, 100);
    }

    if (text.equals("frenteGarra")) { //Se o comando for "DESLIGA", desliga o rele
      //serv2.slowmove(0, 100);
    }
    if (text.equals("trasGarra")) { //Se o comando for "DESLIGA", desliga o rele
      //serv2.slowmove(180, 100);
    }

    if (text.equals("direitaGarra")) { //Se o comando for "DESLIGA", desliga o rele
     // serv2.slowmove(0, 100);
    }
    if (text.equals("esquerdaGarra")) { //Se o comando for "DESLIGA", desliga o rele
     // serv2.slowmove(180, 100);
    }

    if (text.equals("nao")) { //Se o comando for "DESLIGA", desliga o rele
      delay(300);
     // serv4.slowmove(0, 100);
      delay(300);
     // serv4.slowmove(180, 100);
      delay(300);
    //  serv4.slowmove(0, 100);
      delay(300);
    //  serv4.slowmove(180, 100);
      delay(300);
    //  serv4.slowmove(90, 100);
    }
    if (text.equals("sim")) { //Se o comando for "DESLIGA", desliga o rele
   //   serv2.slowmove(90, 100);
      delay(500);
   //   serv3.slowmove(100, 100);
      delay(500);
  //    serv3.slowmove(180, 100);
      delay(500);
  //    serv3.slowmove(100, 100);
      delay(500);
  //    serv3.slowmove(180, 100);
      delay(500);
      //serv3.slowmove(90, 100);
    }

    if (text.equals("lerRele")) { //Se o comando for "DESLIGA", desliga o rele
      Serial.println("z\dcfsdfasdf  ");
    }
  }
}