# Bike_Theft_Alert_System
Bike Theft Alert System using ESP32 and Telegram Bot

Overview

The Bike Theft Alert System is an IoT-based security project designed to protect a parked bike from theft. The system continuously monitors vibrations using an SW-420 vibration sensor. If unauthorized movement is detected, the ESP32 activates a buzzer and instantly sends a Telegram notification to the owner's smartphone over Wi-Fi.

This project demonstrates the use of IoT, embedded systems, and cloud messaging for real-time vehicle security.

---

Features

- Detects vibration using the SW-420 sensor.
- Instant Telegram alert when movement is detected.
- Audible alarm using an active buzzer.
- Wi-Fi connectivity with ESP32.
- Low-cost and easy-to-build hardware.
- Real-time theft notification.
- Built using MicroPython and Thonny IDE.

---

Components Used

Component| Quantity
ESP32 NodeMCU| 1
SW-420 Vibration Sensor| 1
Active Buzzer| 1
Breadboard| 1
Jumper Wires| As Required
USB Cable| 1

---

Circuit Connections

ESP32 Pin| Component
3.3V| SW-420 VCC
GND| SW-420 GND & Buzzer GND
GPIO14| SW-420 DO
GPIO27| Buzzer (+)

---

Software Requirements

- Thonny IDE
- MicroPython Firmware for ESP32
- Telegram Bot
- Wi-Fi Connection

---

How It Works

1. ESP32 connects to the Wi-Fi network.
2. The SW-420 sensor continuously monitors vibrations.
3. If movement is detected:
   - The buzzer sounds an alarm.
   - ESP32 sends a Telegram notification to the owner's phone.
4. The system continues monitoring after the alert.

---

Telegram Notification

Example notification:

BIKE THEFT ALERT!

Movement detected on your bike.
Please check immediately!

---

Installation

1. Flash MicroPython firmware to the ESP32.
2. Install Thonny IDE.
3. Upload the project files to the ESP32.
4. Configure the following values in "main.py":
   - Wi-Fi Name
   - Wi-Fi Password
   - Telegram Bot Token
   - Telegram Chat ID
5. Power on the ESP32.
6. Test the system by creating a vibration on the sensor.

---

Project Structure

Bike-Theft-Alert-System/
│── main.py
│── README.md
│── circuit_diagram.png
│── components.jpg
│── demo.mp4

---

Applications

- Motorcycle security
- Bicycle anti-theft system
- Vehicle monitoring
- Smart parking security
- IoT learning projects

---

Future Enhancements

- GPS location tracking
- GSM/SMS alerts
- Mobile application
- Battery backup
- Camera integration
- Cloud data logging

---

License

This project is released under the MIT License.

---

Author

Jayanth

Bachelor of Computer Applications (BCA)

Built as an IoT project using ESP32, MicroPython, and Telegram Bot for real-time bike theft detection.
