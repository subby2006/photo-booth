#include <Keyboard.h>

const int flash1 = 38;
const int flash2 = 39;
const int capButton = 48;
const int selectButton = 43;
const int upButton = 19;
const int downButton = 18;
const int onboardLED = 13;
int capButtonState;
int lastCapButtonState = HIGH;
int selectButtonState;
int lastSelectButtonState = HIGH; 
int upButtonState;
int lastUpButtonState = HIGH;
int downButtonState;
int lastDownButtonState = HIGH;
// unsigned long lastDebounceTime = 0;  // last time the button state was toggled
// unsigned long debounceDelay = 50;    // debounce time in milliseconds


void setup() {
  // put your setup code here, to run once:
  pinMode(flash1, OUTPUT);
  pinMode(flash2, OUTPUT);
  pinMode(capButton, INPUT_PULLUP);
  pinMode(selectButton, INPUT_PULLUP);
  pinMode(upButton, INPUT_PULLUP);
  pinMode(downButton, INPUT_PULLUP);
  Serial.begin(9600); // debug
  pinMode(onboardLED, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  capButtonState = digitalRead(capButton);
  selectButtonState = digitalRead(selectButton);
  upButtonState = digitalRead(upButton);
  downButtonState = digitalRead(downButton);
  digitalWrite(flash1, HIGH); // deinitialize the flash on first start
  digitalWrite(flash2, HIGH);
  
  if (capButtonState == LOW) {
    Serial.print("CAPTURE");
    digitalWrite(onboardLED, HIGH);
    digitalWrite(flash1, LOW);
    digitalWrite(flash2, LOW);
    delay(1000);
    digitalWrite(flash1, HIGH);
    digitalWrite(flash2, HIGH);
    delay(500);
    digitalWrite(flash1, LOW);
    digitalWrite(flash2, LOW);
    Keyboard.write('S'); // change all the keyboard writes to their respective keypresses defined in the python script
    delay(250);
    digitalWrite(flash1, HIGH);
    digitalWrite(flash2, HIGH);
  }
  // lastCapButtonState = capButtonState;

  if (selectButtonState == LOW) {
    Serial.print("SELECT");
    // Keyboard.write('Z');
    delay(500); // debounce
  }

  if (upButtonState == LOW) {
    Serial.print("UP");
    // Keyboard.write('U');
    delay(500); // debounce
  }

  if (downButtonState == LOW) {
    Serial.print("DOWN");
    // Keyboard.write('D');
    delay(500); // debounce
  }
}


  // maybe use a resisitor instead of overcomplicated debounce scripts
  /* if (selectButtonState != lastSelectButtonState) {
    lastDebounceTime = millis();

    if (selectButtonState == LOW) {
      Serial.print("SELECT");
      // Keyboard.write('V') 
    }
  }
  lastSelectButtonState = selectButtonState;

  if ((millis() - lastDebounceTime) > debounceDelay) {
    lastDebounceTime = 0; // Reset debounce time
  }

}
*/
