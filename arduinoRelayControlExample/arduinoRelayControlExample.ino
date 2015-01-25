int delayTime = 20; // this is in milliseconds

void setup() {
  for (int pin = 4; pin <=12; pin++) //loop through pins 4 incrementing to 12
  {
    digitalWrite(pin, HIGH); // digital HIGH means relay off
    pinMode(pin, OUTPUT); // set the pin as output after, so it doesn't turn on yet
  }
}

void loop() {
  for (int pin = 4; pin <=12; pin++)
  {
    digitalWrite(pin, LOW); // turn on the relay
    delay(delayTime); //wait for the specified time
    digitalWrite(pin, HIGH); // turn off the relay
    delay(delayTime);
  }
}
