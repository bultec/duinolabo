/* mesures de pressions par réception de commandes envoyées par la bibiothèque pduino.py 
 * montage: capteur pression grove sur A1, ref sur 5,0 V
 * commande acceptée: mesure
*/

int pin_capteur_pression;

void setup() {
  Serial.begin(9600);
  pin_capteur_pression=A1;
}

void loop() {
  if (Serial.available()) {
    if (Serial.readString()="mesure") {
       int value = analogRead(pin_capteur_pression);
       float uref = 5.0;
       float k = 0.114;
       float u = value / 1024 * uref;
       float p = (u-k)*7000 / (uref-k);
       Serial.println(p);         
    }
  }     
}
