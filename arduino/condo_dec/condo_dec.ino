/* charge d'un condensateur par réception de commandes envoyées par la bibiothèque pduino.py 
 * montage: - un condensateur en série avec une résistance relié au +5V par l'intermédiare d'un bouton
 *            constante de temps d'environ 1,1 s avec les valeurs par défaut 
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

#define TEMPS 7000
#define N_PTS 50

unsigned long t_total = TEMPS;
const int pin_declenchement = 7;
// les leds permet de visualiser l'attente de declenchement et la charge
const int pin_led_verte = 5;
const int pin_led_rouge = 4;


void setup() {
    pinMode(pin_declenchement, INPUT);
    pinMode(pin_led_verte, OUTPUT);
    pinMode(pin_led_rouge, OUTPUT);
    Serial.begin(9600);
    delay(1);
}

void mesures() {
  float uc = 0;
  float E = 0;
  unsigned long dt = t_total / (N_PTS - 1); //en ms
  unsigned long temps;
  // Attente de déclenchement
  bool ok = true;
  digitalWrite(pin_led_verte, LOW);
  digitalWrite(pin_led_rouge, HIGH);
  while (ok and (digitalRead(pin_declenchement)==LOW)) {
    /*
    String chaine = lit_chaine();
    if (chaine =="stop") {
      ok = false;
      digitalWrite(pin_led_rouge, LOW);
    }
    */
  }
  if (ok) {
    // declenchement ok - le condensateur se charge
    digitalWrite(pin_led_verte, HIGH);
    digitalWrite(pin_led_rouge, LOW);
    unsigned long temps_depart = millis();
    unsigned long t = temps_depart;
    while (millis() - temps_depart <= t_total) {
    temps = (millis() - temps_depart);
      uc = analogRead(A0)*5.0/1024;
      E = analogRead(A1)*5.0/1024; 
      Serial.println(String(temps)+","+String(E)+","+String(uc));
      //un delai personnalisé pour optimiser la mesure du temps
      while ((millis() - temps_depart) - temps < dt) {}
    }
    digitalWrite(pin_led_verte, LOW);
  } 
}  

void loop() {
  if (Serial.available()) {
    String chaine = Serial.readString();
    if (chaine=="charge") {
      mesures();
      Serial.println("end");
    }
    else if (chaine!="") {
      Serial.println("commande non reconnue");
    } 
  }
}
