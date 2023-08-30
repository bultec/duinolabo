/* Commentaires
 */

// constantes (pins utilisés)
const int ...;

// initialisations
void setup() {
  ...
  Serial.begin(9600);
  delay(1);
}

/* fonction de mesure 
on peut choiser les types int, float ou unsigned long (par exemple)
*/

int get_mesure() {
  int ma_mesure;
  ...
  ma_mesure = ...;
  ...
  return ma_mesure;
}

void loop() {
  /* la boucle attend une commande reçue sur la liaison série,
   * réagit en conséquence 
   * et renvoie une donnée ou un message (indispensable car la bibliothèque pduino attend une réponse)
   */
  if (Serial.available()) {
    String chaine = Serial.readString();
    int ok = 0;
    if (chaine=="mesure") {
      ok = 1;
      int une_mesure = get_mesure();
      Serial.println(une_mesure);      
    }
    if (chaine=="...") {
      ok = 1;
      ...;       
    }
    if (chaine=="...") {
      ok = 1;
      ...;        
    }
    if (ok==0) 
      Serial.println("Commande non reconnue");   
  }
}
