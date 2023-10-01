/* Commentaires
 */

#define TEMPS 200
#define N_PTS 50

unsigned long t_total = TEMPS;
const int nb = N_PTS;
unsigned long temps[nb];
int mesures[nb][...]; /* nombres de voies à mesurer */

// constantes (pins utilisés)
/* Suprimer les commentaires si declenchement 
const int pin_declenchement = 7;
const int pin_led_dec = 13;
*/

const int ...;
 
void setup() {
  for (int i=0; i<nb; i++)
    temps[i] = -1;
  t_total = t_total * 1000; //en µs
  /* Suprimer les commentaires si declenchement
  pinMode(pin_declenchement, INPUT);
  pinMode(pin_led_dec, OUTPUT);
  */
  ...
  Serial.begin(9600);
  delay(1);
}

void get_mesures() {
  int n = 0;
  unsigned long dt = t_total / (N_PTS); //en µs
  /* Suprimer les commentaires si declenchement
  digitalWrite(pin_led_dec, HIGH);
  while (digitalRead(pin_declenchement)==LOW) {}
  digitalWrite(pin_led_dec, LOW);
  */
  unsigned long temps_depart = micros();
  unsigned long t = temps_depart;
  while (t - temps_depart <= t_total) {
    temps[n] = (micros() - temps_depart); // t en µs
    mesures[n][0] = ...;
    mesures[n][1] = ...;
    ...
    //un delai personnalisé pour optimiser la rapidité
    while ((micros() - temps_depart) - long(n*dt) <= dt) {}
    n = n + 1;
    t = micros();
  }
} 

void envoie_mesures() {
  int n = 0;
  for(int i=0 ; i<nb; i++) {
    if (temps[i] != -1) {
      // le temps est convertit en ms pour compatibilité avec les programes lents
      /* par exemple
      Serial.println(String(float(temps[i])/1000) + "," + String(mesures[i][0]*5.0/1024) + "," + String(mesures[i][1]*5.0/1024));
      */
      Serial.println(String(float(temps[i])/1000) + "," + String(mesures[i][...]*...) + "," + String(mesures[i][...]*...));
      n = n+1;
    }
    delay(1);
  }
}

void loop() {
  if (Serial.available()) {
    String chaine = Serial.readString();
    if (chaine=="...") {
      get_mesures();
      envoie_mesures();
      Serial.println("end");
    }
    else if (chaine!="") {;
      Serial.println("commande non reconnue");
    }
  } 
}
