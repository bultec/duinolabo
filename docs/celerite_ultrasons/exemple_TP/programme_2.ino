const float VITESSE_SON = ...;               // Vitesse du son en m/s
const int pin_Trigger = 4;
const int TIMEOUT = (6/VITESSE_SON)*1e6;       // TIMEOUT en µs (pour 6,0m aller/retour)
const int pin_led_verte = 9;
const int pin_led_rouge = 7;
const int pin_buzzer = 8;

/* Renvoie la distance mesurée en cm */
float getDistance() {
  unsigned long temps1;
  unsigned long duree_ar;
  pinMode(pin_Trigger, OUTPUT);
  digitalWrite(pin_Trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(pin_Trigger, LOW);
  pinMode(pin_Trigger, INPUT);
  while (digitalRead(pin_Trigger) == LOW) { }
  temps1 = micros();
  while (digitalRead(pin_Trigger) == HIGH and micros() - temps1 < TIMEOUT) { }
  // durée aller retour en mètres
  duree_ar = micros() - temps1;
   // Distance en mètres
  float distance = duree_ar* 1e-6 * VITESSE_SON / 2; 
  return distance;
}

void setup() {
  pinMode(pin_Trigger, OUTPUT);
  pinMode(pin_buzzer, OUTPUT);
  pinMode(pin_led_rouge, OUTPUT);
  pinMode(pin_led_verte, OUTPUT);
  Serial.begin(9600);
  delay(1);
}

void loop() {
    float distance;
    distance = getDistance(); 
    /* distance inférieure à 50cm */
    if(distance < ...) {
      digitalWrite(pin_led_rouge, ...);
      digitalWrite(pin_led_verte, ...);
      tone(pin_buzzer,600,125);
      delay(...);
    }
    /* distance comprise entre 0.50m et 1.0m*/
    else { 
      if(distance < ...) {
        digitalWrite(pin_led_rouge, ...);
        digitalWrite(pin_led_verte, ...);
        tone(pin_buzzer,600,125);
        delay(...);
      }
      else {
      /* distance supérieure à 1.0m*/
      digitalWrite(pin_led_rouge, ...);
      digitalWrite(pin_led_verte, ...);
      delay(125);
    }
  } 
}
