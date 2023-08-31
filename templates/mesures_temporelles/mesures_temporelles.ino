/* Commentaires
 */

#define TEMPS 7000
#define N_PTS 50

unsigned long t_total = TEMPS;

// constantes (pins utilisés)
const int ...;

void setup() {
  ...
  Serial.begin(9600);
  delay(1);
}

void mesures(String chaine) {
  unsigned long dt = t_total / (N_PTS - 1); //en ms
  unsigned long temps_depart = millis();
  unsigned long t_mesure;
  //à modifier
  int ma_mesure;
  if (chaine == "...") {
    ...
  }
  if (chaine == "...") {
    ...
  }
  while (millis() - temps_depart <= t_total) {
    t_mesure = (millis() - temps_depart);
    ma_mesure = ...; 
    Serial.println(String(t_mesure)+","+String(ma_mesure)+...);
    //un delai personnalisé pour optimiser la mesure du temps
    while ((millis() - temps_depart) - t_mesure < dt) {}
  }
  ...
  Serial.println("end");
}

void loop() {
  /* la boucle attend une commande reçue sur la liaison série,
   * réagit en conséquence 
   * et renvoie une donnée ou un message (indispensable car la bibliothèque pduino attend une réponse)
   */
  if (Serial.available()) {
    String chaine = Serial.readString();
    if ((chaine=="...") or (chaine=="...")) {
      mesures(chaine);
    }
    else {
      Serial.println("Commande non reconnue");
    }   
  }
}
