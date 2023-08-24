/* Mesure de l'angle d'un pendule pesant en fonction du temps par réception de commande envoyée
 * par la bibiothèque pyduino.py 
 * montage: - un pendule pesant avec capteur d'angle analogique sur le pin 2 
 *          - pour la visualisation, une led (en série avec une résistance de 220 ohms) sur le pin 5                                                                               
                   Pin 2

                   |
                   |  <---- Curseur

GND  ---------- +-++-+ -------  +5V
                | || |
                | || | <-------  Potentiomètre
                +-++-+
                  ||
                  ||
                  ||
                  ||
                  ||
                  ||    <-------  Pendule pesant
                  ||
                  ||
                  ||
                  ||
  x               ||
  xxx           +-++-+           xx
    xxxxx       | ++ |        x xx
         xxxxx  |    | xxxxx x
                +----+
*/        

#define TEMPS 2000
#define N_PTS 75

unsigned long t_total = TEMPS;
const int pin_led = 5;

void setup() {
    pinMode(pin_led, OUTPUT);
    Serial.begin(9600);
    delay(1);
}

void mesures() {
  int teta = 0;
  unsigned long dt = t_total / N_PTS; //en ms
  unsigned long temps_depart = millis();
  unsigned long t_mesure;
  digitalWrite(pin_led, HIGH);
  while (millis() - temps_depart <= t_total) {
    t_mesure = (millis() - temps_depart);
    teta = analogRead(A2);
    Serial.println(String(t_mesure)+","+String(teta));
    //un delai personnalisé pour optimiser la mesure du temps
    while ((millis() - temps_depart) - t_mesure < dt) {}
  }
  digitalWrite(pin_led, LOW);
  Serial.println("end");
}

void loop() {
  if (Serial.available()) {
    String chaine = Serial.readString();
    String message = "";
    if (chaine=="mesures") {
      mesures();          
    }
    else {
      Serial.println("commande non reconnue");
    } 
  }
}
