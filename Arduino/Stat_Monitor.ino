//====================================
// Welcome to cpu temparature monitor
// Equipments: 1> 16x2 lcd display
//             2> Arduino Uno
//====================================
#include <LiquidCrystal_I2C.h>

// Set Pin lcd
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  // init LCD
  lcd.init();
  lcd.clear();
  lcd.backlight();

  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
}

void loop() {
  if (Serial.available() > 0) { // check if any data is available in serial port
    String serialReceive = Serial.readString();
    //    Serial.println(serialReceive); //returns data for debuging
    Display(serialReceive);
  }
}

// variables
String CPUstat;
String RAMstat;


void Display(String serialReceive) {
  lcd.clear();

  CPUstat = serialReceive.substring(0, 6);
  CPUstat = "CPU" + CPUstat;
  RAMstat = serialReceive.substring(6, 12);
  RAMstat = "RAM" + RAMstat;

  lcd.setCursor(0, 0);
  lcd.print(CPUstat);
  lcd.setCursor(0, 1);
  lcd.print(RAMstat);

}
