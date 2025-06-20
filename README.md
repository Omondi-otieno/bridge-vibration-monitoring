# bridge-vibration-monitoring
This project demonstrates structural health monitoring (SHM) of the Nzoia Bridge using low-cost wireless vibration sensors and signal processing via Python. Accelerometer data was collected using an MPU9250 sensor and Arduino, then analyzed using Continuous Wavelet Transform (CWT) to assess frequency response and potential resonance risk.

📊 Vibration Monitoring: Arduino + Python
This project collects vibration data using an MPU9250 sensor with Arduino and analyzes the data using Python with Continuous Wavelet Transform (CWT).

🔧 Arduino
The Arduino sketch logs accelerometer data (X, Y, Z) from the MPU9250 sensor onto an SD card.

📁 arduino/
• CVS_590_Sensor_code.ino

Requires libraries: MPU9250_asukiaaa, SD, SPI, Wire

🐍 Python
The Python script reads the logged data and applies CWT to extract average peak frequencies over time.

📁 python/
• cwt_peak_frequency.py

Requires: numpy, matplotlib, pywt (PyWavelets)

📈 Output
Plots the average peak frequency over time, and highlights the maximum and minimum values.
