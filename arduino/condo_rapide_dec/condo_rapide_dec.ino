/* charge d'un condensateur par réception de commandes envoyées par la bibiothèque pduino.py 
 * pour obtenir une charge rapide, les données sont stockées
 * et envoyées sur la liaison série après la boucle de mesures sous forme de float de 0 à 5,0 V
 * montage: - un condensateur en série avec une résistance relié au +5V par l'intermédiare d'un bouton
 *            constante de temps d'environ 22 ms avec les valeurs par défaut 
 *          - circuit de déclenchement sur pin 7  
 *          - pour la visualisation : - une led rouge (en série avec une résistance de 220 ohms) sur le pin 4
 *                                    - une led verte (en série avec une résistance de 220 ohms) sur le pin 5
                                   GND
                   Pin 7                 --+--               Pin 4   Pin 5
                     |    +----------+     |       GND         |       |
                     +----+ 100 k    +-----+       --+--      +++     +++
                     |    +----------+               |        | |     | |
       bouton        |                               |        | |     | |
          ++         |                        | |    |        +++     +++
         -++-        |  +----------+          | |    |         |       |
+5V  ----    ------+-+--+   R      +---+----+-+ +----+       --+--   --+--
                   |    +----------+   |    | | |C           \   /   \   /
                   |                   |    | | |             \ /     \ /
                   |                   |    |                 -+-     -+-
                   |                   |    |       ++         |       |
                   v                   v    |      -++-        |       |
                    A1                  A0  +------    --------+-     -+-
                                                  bouton      GND     GND
 * la tension aux bornes du condensateur est mesurée sur A0
 * la tension aux bornes du générateur est mesurée sur A1
 * les deux tensions sont renvoyées sous forme de float de 0 à 5,0 V
 * commande acceptée: charge
 */

#define TEMPS 164
#define N_PTS 50

const int pin_declenchement = 7;
// les leds permet de visualiser l'attente de declenchement et la charge
const int pin_led_verte = 5;
const int pin_led_rouge = 4;
const int nb = N_PTS;
unsigned long t_total = TEMPS;
unsigned long temps[nb];
int mesures[nb][2];
 
void setup() {
  for (int i=0; i<nb; i++)
    temps[i] = -1;
  t_total = t_total * 1000; //en µs
  pinMode(pin_declenchement, INPUT);
  pinMode(pin_led_verte, OUTPUT);
  pinMode(pin_led_rouge, OUTPUT);
  Serial.begin(9600);
  delay(1);
}

void get_mesures() {
  int n = 0;
  unsigned long dt = t_total / (N_PTS); //en µs
  // Attente de déclenchement
  digitalWrite(pin_led_verte, LOW);
  digitalWrite(pin_led_rouge, HIGH);
  String chaine = "";
  while (digitalRead(pin_declenchement)==LOW) {}
    // declenchement ok - le condensateur se charge
  digitalWrite(pin_led_verte, HIGH);
  digitalWrite(pin_led_rouge, LOW);
  unsigned long temps_depart = micros();
  unsigned long t = temps_depart;
  while (t - temps_depart <= t_total) {
    temps[n] = (micros() - temps_depart); // t en µs
    mesures[n][0] = analogRead(A0);
    mesures[n][1] = analogRead(A1);
    //Serial.println(t - temps_depart);
    //un delai personnalisé pour optimiser la rapidité
    while ((micros() - temps_depart) - long(n*dt) <= dt) {}
    n = n + 1;
    t = micros();
  }
  digitalWrite(pin_led_verte, LOW);
} 

void envoie_mesures() {
  int n = 0;
  for(int i=0 ; i<nb; i++) {
    if (temps[i] != -1) {
      // le temps est convertit en ms pour compatibilité avec le programe de charge lente condo.ino
      Serial.println(String(float(temps[i])/1000) + "," + String(mesures[i][1]*5.0/1024) + "," + String(mesures[i][0]*5.0/1024));
      n = n+1;
    }
    delay(1);
  }
  //Serial.println(n);
}

void loop() {
  if (Serial.available()) {
    String chaine = Serial.readString();
    if (chaine=="charge") {
      get_mesures();
      envoie_mesures();
      Serial.println("end");
    }
    else if (chaine!="") {;
      Serial.println("commande non reconnue");
    }
  } 
}
