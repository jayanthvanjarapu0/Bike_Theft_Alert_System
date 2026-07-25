import network
import urequests
import time
from machine import Pin

# -----------------------
# Wi-Fi Credentials
# -----------------------
SSID = "YOUR_WIFI_NAME"
PASSWORD = "YOUR_WIFI_PASSWORD"

# -----------------------
# Telegram Bot Details
# -----------------------
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

# -----------------------
# Hardware Pins
# -----------------------
sensor = Pin(14, Pin.IN)      # SW420 DO
buzzer = Pin(27, Pin.OUT)     # Active Buzzer

# -----------------------
# Connect to Wi-Fi
# -----------------------
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

if not wifi.isconnected():
    print("Connecting to Wi-Fi...")
    wifi.connect(SSID, PASSWORD)

    while not wifi.isconnected():
        time.sleep(1)
        print(".", end="")

print("\nWi-Fi Connected")
print("IP:", wifi.ifconfig()[0])

# -----------------------
# Send Telegram Message
# -----------------------
def send_telegram(message):

    url = "https://api.telegram.org/bot{}/sendMessage".format(BOT_TOKEN)

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        response = urequests.post(url, json=data)
        response.close()
        print("Telegram Alert Sent")
    except Exception as e:
        print("Error:", e)

# -----------------------
# Main Program
# -----------------------

print("Bike Theft Alert System Running...")

last_alert = 0
cooldown = 20  # seconds

while True:

    if sensor.value() == 1:

        print("Movement Detected!")

        # Alarm
        for i in range(10):
            buzzer.on()
            time.sleep(0.2)
            buzzer.off()
            time.sleep(0.2)

        current = time.time()

        if current - last_alert > cooldown:

            send_telegram(
                "🚨 BIKE THEFT ALERT!\n\n"
                "Movement detected on your bike.\n"
                "Please check immediately!"
            )

            last_alert = current

        while sensor.value() == 1:
            time.sleep(0.1)

    time.sleep(0.1)