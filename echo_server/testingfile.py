import time
import machine
import network
import urequests
from machine import Pin

# Replace with your network credentials
ssid = "Tifac-Core"
password = "Tifac@akg321#"

# Initialize Telegram BOT
BOTtoken = "6683085522:AAHwpdWC5Y3kcV9Qnfdvnp3MMHZcahrogYk"  # your Bot Token (Get from Botfather)
CHAT_ID = "837909618"

# Initialize LED
ledPin = Pin(2, Pin.OUT)
ledState = 0
ledPin.value(ledState)

# Create Wi-Fi connection
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    print("Connecting to WiFi...")
    time.sleep(1)
print("Connected to WiFi")

# Function to send a message via Telegram Bot
def send_message(chat_id, message):
    url = f"https://api.telegram.org/bot{BOTtoken}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = urequests.post(url, json=data)
    response.close()

def main():
    #last_time_bot_ran = 0
    #bot_request_delay = 1  # 1 second

    while True:
        url = f"https://api.telegram.org/bot{BOTtoken}/getUpdates"
        response = urequests.get(url)
        updates = response.json().get("result", [])
        response.close()

        if updates:
            message = updates[-1]
            text = message.get("message", {}).get("text", "")

            if text == "/start":
                ledState = 1
                ledPin.value(ledState)
            else:
                ledState = 0
                ledPin.value(ledState)
        
        

if __name__ == "__main__":
    main()

