#include <MPU9250_asukiaaa.h>
#include <SPI.h>
#include <SD.h>
#include <Wire.h>

MPU9250_asukiaaa mySensor;
File dataFile;

const int chipSelect = 10;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  mySensor.setWire(&Wire);
  mySensor.beginAccel();

  // Initialize SD card
  if (!SD.begin(chipSelect)) {
    Serial.println("SD initialization failed!");
    while (1);
  }
  Serial.println("SD card initialized.");

  dataFile = SD.open("dat.txt", FILE_WRITE);
  if (!dataFile) {
    Serial.println("Error opening dat.txt");
    while (1);
  }

  Serial.println("Logging started...");
}

void loop() {
  mySensor.accelUpdate();

  float ax = mySensor.accelX();
  float ay = mySensor.accelY();
  float az = mySensor.accelZ();

  // Print to Serial Monitor
  Serial.print("accelX: "); Serial.println(ax);
  Serial.print("accelY: "); Serial.println(ay);
  Serial.print("accelZ: "); Serial.println(az);

  // Log to SD card
  dataFile.print(ax); dataFile.print(",");
  dataFile.print(ay); dataFile.print(",");
  dataFile.println(az);

  dataFile.flush(); // Ensure data is written
  delay(50); // Adjust sampling rate as needed
}
